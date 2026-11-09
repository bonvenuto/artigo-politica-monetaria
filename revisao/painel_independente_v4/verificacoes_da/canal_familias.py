"""
Canal de juros das famílias (H2) — versão 4 (itens REV-32 a REV-35 do painel independente).

Com o MESMO choque-base (VAR(6) com sazonais, IC-Br em US$), LPs lineares para:
  J  = comprometimento com juros (SGS 29033)
  A  = comprometimento com amortização (SGS 29036)       [identidade: S = J + A, logo J - S = -A]
  S  = comprometimento com o serviço total (SGS 29034)
  S' = serviço total sem habitacional (SGS 29035)
  E  = endividamento (% renda 12m, SGS 29037)
  100 ln(J/E) (taxa efetiva implícita) e 100 ln E.
Robustez de H2 (J): estoque defasado como controle, Newey-West com h+3 defasagens (estrutura MA(2) da média
móvel trimestral da renda), EWC, amostra trimestral não sobreposta (fim de trimestre; 3 defasagens e dummies
trimestrais), amostra até 2023:12 (renda ancorada nas
Contas Nacionais) e assimetria entre surpresas positivas e negativas.

Autor: Ângelo Augusto Bonvenuto
"""

import os

import numpy as np
import pandas as pd

from comum import (DF, H_FAMILY, H_REPORT, RES_DIR, SEASONAL, build_system, ewc, holm, identify_shock,
                   lag_controls, ols_hac)

v = build_system()
shock, scale, _ = identify_shock(v)
sd = float(shock.std())
CTRL = pd.concat([lag_controls(v), SEASONAL], axis=1)
X0 = pd.concat([shock.rename('s'), CTRL], axis=1)

dep = {
    'J (29033)': DF['juros_divida'],
    'A (29036)': DF['amortizacao'],
    'S (29034)': DF['servico_divida'],
    "S sem habitacional (29035)": DF['servico_sem_hab'],
    'E (29037)': DF['endividamento'],
    '100 ln(J/E)': 100 * np.log(DF['juros_divida'] / DF['endividamento']),
    '100 ln E': 100 * np.log(DF['endividamento']),
}
ident_err = float((DF['juros_divida'] + DF['amortizacao'] - DF['servico_divida']).abs().max())


def lp(y, X=X0, h=0, maxlags=None, key='s'):
    o, d = ols_hac(y.shift(-h), X, h, maxlags)
    return o, d


tab = {}
for nm, y in dep.items():
    tab[nm] = {}
    for h in H_REPORT:
        o, d = lp(y, h=h)
        tab[nm][h] = dict(b=o.params['s'], se=o.bse['s'], p=o.pvalues['s'], pe=ewc(o, d, 's')[3])
    for h, x in zip(H_FAMILY, holm([tab[nm][h]['p'] for h in H_FAMILY])):
        tab[nm][h]['holm'] = x

J = DF['juros_divida']
rob = {}
# (a) estoque defasado como controle
XE = pd.concat([X0, lag_controls(DF[['endividamento']])], axis=1)
# (e) amostra trimestral não sobreposta: t em mar/jun/set/dez
qmask = pd.Series(DF.index.month.isin([3, 6, 9, 12]), index=DF.index)
for h in H_REPORT:
    r = {}
    o, d = lp(J, XE, h); r['estoque'] = (o.params['s'], o.pvalues['s'])
    o, d = lp(J, X0, h, maxlags=h + 3); r['nw_h3'] = (o.params['s'], o.pvalues['s'])
    o, d = lp(J, X0, h); r['ewc'] = (o.params['s'], ewc(o, d, 's')[3])
    yq = J.shift(-h).where(qmask)
    Xq = pd.concat([shock.rename('s'), lag_controls(v, 3), SEASONAL[['m_6', 'm_9', 'm_12']]], axis=1)
    o, d = ols_hac(yq, Xq, 0, maxlags=int(np.ceil((h + 1) / 3)) + 1); r['trim'] = (o.params['s'], o.pvalues['s'], len(d))
    y23 = J.shift(-h)
    y23[[t + pd.DateOffset(months=h) > pd.Timestamp('2023-12-01') for t in y23.index]] = np.nan
    o, d = ols_hac(y23, X0, h); r['ate2023'] = (o.params['s'], o.pvalues['s'], len(d))
    Xa = pd.concat([shock.clip(lower=0).rename('s_pos'), shock.clip(upper=0).rename('s_neg'), CTRL], axis=1)
    o, d = ols_hac(J.shift(-h), Xa, h)
    r['assim'] = (o.params['s_pos'], o.pvalues['s_pos'], o.params['s_neg'], o.pvalues['s_neg'],
                  float(o.wald_test('s_pos = s_neg', scalar=True).pvalue))
    rob[h] = r

out = os.path.join(RES_DIR, "canal_familias.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("=== CANAL DE JUROS DAS FAMÍLIAS — VERSÃO 4 (mesmo choque-base para todas as séries) ===\n")
    f.write(f"Choque +1 p.p. | d.p. = {sd:.4f} | identidade J + A = S: erro máximo {ident_err:.3f} p.p. "
            f"(arredondamento); logo a resposta de J - S é a resposta de -A\n")
    f.write("coef (p NW) {p EWC} [p Holm, h=3..24]\n")
    for nm in dep:
        f.write(f"\n[{nm}]\n")
        for h in H_REPORT:
            r = tab[nm][h]
            hh = f"{r['holm']:.3f}" if 'holm' in r else '  -  '
            f.write(f"h={h:2d} | {r['b']:+.4f} ({r['p']:.3f}) {{{r['pe']:.3f}}} [{hh}] | por 1 d.p. {r['b'] * sd:+.4f}\n")
    f.write("\n=== ROBUSTEZ DE H2 (J, SGS 29033): coef (p) ===\n")
    for h in H_REPORT:
        r = rob[h]
        f.write(f"h={h:2d} | + estoque defasado {r['estoque'][0]:+.3f} ({r['estoque'][1]:.3f}) | NW h+3 ({r['nw_h3'][1]:.3f}) | "
                f"EWC ({r['ewc'][1]:.3f}) | trimestral {r['trim'][0]:+.3f} ({r['trim'][1]:.3f}; N={r['trim'][2]}) | "
                f"até 2023:12 {r['ate2023'][0]:+.3f} ({r['ate2023'][1]:.3f}; N={r['ate2023'][2]}) | "
                f"b+ {r['assim'][0]:+.3f} ({r['assim'][1]:.3f}) b- {r['assim'][2]:+.3f} ({r['assim'][3]:.3f}) p sim {r['assim'][4]:.3f}\n")
    j = DF['juros_divida']; e = DF['endividamento']
    f.write(f"\nDescritivos: corr(J, Selic) = {j.corr(DF['selic']):.2f}; corr(J, E) = {j.corr(e):.2f}; "
            f"J/E média 2005 = {100 * (j / e).loc['2005'].mean():.1f}%, 2021 = {100 * (j / e).loc['2021'].mean():.1f}%, "
            f"ago/2026 = {100 * (j / e).iloc[-1]:.1f}%\n")
    f.write(f"J: fev/2026 {j.loc['2026-02-01']:.2f}, ago/2026 {j.loc['2026-08-01']:.2f}; Selic fev/2026 {DF['selic'].loc['2026-02-01']:.2f}, ago/2026 {DF['selic'].loc['2026-08-01']:.2f}\n")
    f.write(f"Episódio 2021-2023: J jan/2021 {j.loc['2021-01-01']:.2f}, máx. 2021-2023 {j.loc['2021':'2023'].max():.2f} "
            f"({j.loc['2021':'2023'].idxmax():%Y-%m}); Selic jan/2021 {DF['selic'].loc['2021-01-01']:.2f}, máx. {DF['selic'].loc['2021':'2023'].max():.2f}\n")
print(f"Salvo: {out}")
