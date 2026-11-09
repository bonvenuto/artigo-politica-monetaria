"""
Canal de juros das famílias (H2).

Com o MESMO choque-base (VAR(6) com sazonais, IC-Br em US$), LPs lineares para:
  J  = comprometimento com juros (SGS 29033)
  A  = comprometimento com amortização (SGS 29036)       [identidade: S = J + A, logo J - S = -A]
  S  = comprometimento com o serviço total (SGS 29034)
  S' = serviço total sem habitacional (SGS 29035)
  E  = endividamento (% renda 12m, SGS 29037)
  100 ln(J/E) (taxa efetiva implícita) e 100 ln E.
Cada série é estimada em duas versões: (i) controles do sistema (6 defasagens do VAR + sazonais), como em J;
(ii) idem mais 6 defasagens da própria variável dependente (padronização com J, que está no VAR).
Robustez de H2 (J): estoque defasado, Newey-West com h+3 defasagens (MA(2) da renda), EWC, amostra trimestral
não sobreposta (três fases de amostragem e choque agregado por trimestre), amostra até 2023:12.
Assimetria: s+/s-, com p_Holm da simetria, decomposição s e |s| e normalização pela resposta da Selic.
Choque alternativo: meta Selic de fim de mês (SGS 432) para H2 e para a LP linear da inflação.
Poder: efeito mínimo detectável (2,80 x EP) de S e de J - S (= -A); resposta de J por p.p. de Selic na trajetória.

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
J = DF['juros_divida']

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


def lp(y, X=X0, h=0, maxlags=None):
    return ols_hac(y.shift(-h), X, h, maxlags)


def own_lags(y, p=6):
    return pd.concat([y.shift(k).rename(f"own_l{k}") for k in range(1, p + 1)], axis=1)


def summarize(o, d, key='s'):
    e = ewc(o, d, key)
    return dict(b=o.params[key], se=o.bse[key], p=o.pvalues[key], se_ewc=e[1], pe=e[3])


# ---------- (1) Decomposição: controles do sistema (antiga) e com defasagens próprias (padronizada) ----------
tab = {'sistema': {}, 'propria': {}}
for ver in tab:
    for nm, y in dep.items():
        X = X0 if (ver == 'sistema' or nm.startswith('J (')) else pd.concat([X0, own_lags(y)], axis=1)
        tab[ver][nm] = {h: summarize(*lp(y, X, h)) for h in H_REPORT}
        for h, x in zip(H_FAMILY, holm([tab[ver][nm][h]['p'] for h in H_FAMILY])):
            tab[ver][nm][h]['holm'] = x
        for h, x in zip(H_FAMILY, holm([tab[ver][nm][h]['pe'] for h in H_FAMILY])):
            tab[ver][nm][h]['holm_ewc'] = x

# ---------- (2) Robustez de H2 ----------
XE = pd.concat([X0, lag_controls(DF[['endividamento']])], axis=1)


def quarterly(h, phase, aggregate=False):
    """Amostra trimestral não sobreposta. phase: mês de amostragem dentro do trimestre (1, 2 ou 3)."""
    months = [phase + 3 * k for k in range(4)]
    mask = pd.Series(DF.index.month.isin(months), index=DF.index)
    yq = J.shift(-h).where(mask)
    dums = pd.concat([pd.Series((DF.index.month == m).astype(float), index=DF.index, name=f'q_{m}') for m in months[1:]], axis=1)
    if aggregate:   # soma dos três choques mensais da janela t-2..t; controles pré-determinados (defasagens 3-5)
        sq = shock.rolling(3).sum().rename('s')
        Xq = pd.concat([sq, lag_controls(v, 3).shift(2), dums], axis=1)
    else:
        Xq = pd.concat([shock.rename('s'), lag_controls(v, 3), dums], axis=1)
    o, d = ols_hac(yq, Xq, 0, maxlags=int(np.ceil((h + 1) / 3)) + 1)
    return o.params['s'], o.pvalues['s'], len(d)


rob = {}
for h in H_REPORT:
    r = {}
    o, d = lp(J, XE, h); r['estoque'] = (o.params['s'], o.pvalues['s'])
    o, d = lp(J, X0, h, maxlags=h + 3); r['nw_h3'] = (o.params['s'], o.pvalues['s'])
    o, d = lp(J, X0, h); r['ewc'] = (o.params['s'], ewc(o, d, 's')[3])
    r['trim'] = {ph: quarterly(h, ph) for ph in (1, 2, 3)}
    r['trim_agg'] = {ph: quarterly(h, ph, True) for ph in (1, 2, 3)}
    y23 = J.shift(-h)
    y23[[t + pd.DateOffset(months=h) > pd.Timestamp('2023-12-01') for t in y23.index]] = np.nan
    o, d = ols_hac(y23, X0, h); r['ate2023'] = (o.params['s'], o.pvalues['s'], len(d))
    rob[h] = r

# ---------- (3) Assimetria ----------
asy = {}
selic = v['selic']
XA = pd.concat([shock.clip(lower=0).rename('s_pos'), shock.clip(upper=0).rename('s_neg'), CTRL], axis=1)
XM = pd.concat([shock.rename('s'), shock.abs().rename('abs_s'), CTRL], axis=1)
for h in H_REPORT:
    r = {}
    o, d = ols_hac(J.shift(-h), XA, h)
    r['bp'], r['pp'], r['bn'], r['pn'] = o.params['s_pos'], o.pvalues['s_pos'], o.params['s_neg'], o.pvalues['s_neg']
    r['psim'] = float(o.wald_test('s_pos = s_neg', scalar=True).pvalue)
    o, d = ols_hac(J.shift(-h), XM, h)
    r['a'], r['pa'], r['b'], r['pb'] = o.params['s'], o.pvalues['s'], o.params['abs_s'], o.pvalues['abs_s']
    # trajetória da Selic após s+ e s- (nível em t+h e média acumulada de t a t+h)
    o, d = ols_hac(selic.shift(-h), XA, h)
    r['sel_p'], r['sel_n'] = o.params['s_pos'], o.params['s_neg']
    o, d = ols_hac(selic.rolling(h + 1).mean().shift(-h), XA, h)
    r['selm_p'], r['selm_n'] = o.params['s_pos'], o.params['s_neg']
    asy[h] = r
for h, x in zip(H_FAMILY, holm([asy[h]['psim'] for h in H_FAMILY])):
    asy[h]['psim_holm'] = x

# ---------- (4) Choque com a meta Selic de fim de mês (SGS 432) ----------
v2 = build_system(policy='meta_selic')
shock2, scale2, _ = identify_shock(v2)
sd2 = float(shock2.std())
CTRL2 = pd.concat([lag_controls(v2), SEASONAL], axis=1)
X2 = pd.concat([shock2.rename('s'), CTRL2], axis=1)
meta = {}
for nm, y in [('J (29033)', v2['juros_divida']), ('IPCA livres', v2['ipca_livres']), ('Selic (meta)', v2['selic'])]:
    meta[nm] = {h: summarize(*lp(y, X2, h)) for h in H_REPORT}
    for h, x in zip(H_FAMILY, holm([meta[nm][h]['p'] for h in H_FAMILY])):
        meta[nm][h]['holm'] = x

# ---------- (5) Poder: MDE = 2,80 x EP ----------
# ---------- (6) J por p.p. de Selic na trajetória (choque-base, LP linear) ----------
traj = {}
for h in H_REPORT:
    o, d = lp(selic, X0, h); sel_h = o.params['s']
    ym = selic.rolling(h + 1).mean().shift(-h)
    o, d = ols_hac(ym, X0, h); selm = o.params['s']
    traj[h] = dict(sel=sel_h, selm=selm, j=tab['propria']['J (29033)'][h]['b'])

out = os.path.join(RES_DIR, "canal_familias.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("=== CANAL DE JUROS DAS FAMÍLIAS (mesmo choque-base para todas as séries) ===\n")
    f.write(f"Choque +1 p.p. | d.p. = {sd:.4f} | identidade J + A = S: erro máximo {ident_err:.3f} p.p. "
            f"(arredondamento); logo a resposta de J - S é a resposta de -A\n")
    for ver, rot in [('propria', 'COM defasagens da própria variável dependente (padronizada; em J já estão no VAR)'),
                     ('sistema', 'SÓ controles do sistema (especificação anterior, para comparação)')]:
        f.write(f"\n##### DECOMPOSIÇÃO — {rot} #####\n")
        f.write("coef (p NW) {p EWC} [p Holm NW | p Holm EWC, h=3..24]\n")
        for nm in dep:
            f.write(f"\n[{nm}]\n")
            for h in H_REPORT:
                r = tab[ver][nm][h]
                hh = f"{r['holm']:.3f} | {r['holm_ewc']:.3f}" if 'holm' in r else '  -  '
                f.write(f"h={h:2d} | {r['b']:+.4f} ({r['p']:.3f}) {{{r['pe']:.3f}}} [{hh}] | por 1 d.p. {r['b'] * sd:+.4f}\n")

    f.write("\n=== 100 ln(J/E): p Holm (família h=3..24), controles padronizados ===\n")
    for ver in ('propria', 'sistema'):
        r = tab[ver]['100 ln(J/E)']
        f.write(f"{ver:8s} | NW: " + ", ".join(f"h={h}: {r[h]['holm']:.4f}" for h in H_FAMILY)
                + f" | máx. {max(r[h]['holm'] for h in H_FAMILY):.4f}"
                + " | EWC: " + ", ".join(f"h={h}: {r[h]['holm_ewc']:.4f}" for h in H_FAMILY)
                + f" | máx. {max(r[h]['holm_ewc'] for h in H_FAMILY):.4f}\n")

    f.write("\n=== ROBUSTEZ DE H2 (J, SGS 29033): coef (p) ===\n")
    for h in H_REPORT:
        r = rob[h]
        f.write(f"h={h:2d} | + estoque defasado {r['estoque'][0]:+.3f} ({r['estoque'][1]:.3f}) | NW h+3 ({r['nw_h3'][1]:.3f}) | "
                f"EWC ({r['ewc'][1]:.3f}) | até 2023:12 {r['ate2023'][0]:+.3f} ({r['ate2023'][1]:.3f}; N={r['ate2023'][2]})\n")

    f.write("\n=== AMOSTRA TRIMESTRAL NÃO SOBREPOSTA: três fases (mês de amostragem 1/2/3 do trimestre) ===\n")
    f.write("Fase 1 = jan/abr/jul/out; fase 2 = fev/mai/ago/nov; fase 3 = mar/jun/set/dez (a reportada anteriormente)\n")
    f.write("(a) choque mensal do mês de amostragem: coef (p)\n")
    for h in H_REPORT:
        f.write(f"h={h:2d} | " + " | ".join(f"fase {ph}: {r_[0]:+.3f} ({r_[1]:.3f}; N={r_[2]})" for ph, r_ in rob[h]['trim'].items())
                + f" | média das fases {np.mean([r_[0] for r_ in rob[h]['trim'].values()]):+.3f}\n")
    f.write("(b) choque agregado por trimestre (soma dos 3 choques mensais; controles defasados antes da janela): coef (p)\n")
    for h in H_REPORT:
        f.write(f"h={h:2d} | " + " | ".join(f"fase {ph}: {r_[0]:+.3f} ({r_[1]:.3f}; N={r_[2]})" for ph, r_ in rob[h]['trim_agg'].items())
                + f" | média das fases {np.mean([r_[0] for r_ in rob[h]['trim_agg'].values()]):+.3f}\n")

    f.write("\n=== ASSIMETRIA DE H2 (exploratória) ===\n")
    f.write("(a) s+ / s-: b+ (p) | b- (p) | p simetria | p Holm da simetria (família h=3..24; h=0 fora da família)\n")
    for h in H_REPORT:
        r = asy[h]
        hh = f"{r['psim_holm']:.3f}" if 'psim_holm' in r else '  -  '
        f.write(f"h={h:2d} | b+ {r['bp']:+.3f} ({r['pp']:.3f}) | b- {r['bn']:+.3f} ({r['pn']:.3f}) | p sim {r['psim']:.3f} | p Holm {hh}\n")
    f.write("(b) decomposição J = a*s + b*|s| (|s| = magnitude da surpresa): a (p) | b (p)\n")
    for h in H_REPORT:
        r = asy[h]
        f.write(f"h={h:2d} | a {r['a']:+.3f} ({r['pa']:.3f}) | b {r['b']:+.3f} ({r['pb']:.3f})\n")
    f.write("(c) Selic após s+ e s- (nível em t+h; média de t a t+h) e J normalizada (b/Selic nível; b/Selic média):\n")
    for h in H_REPORT:
        r = asy[h]
        nrm = lambda b, s: f"{b / s:+.3f}" if abs(s) > 0.05 else "n.d."
        f.write(f"h={h:2d} | Selic s+: nível {r['sel_p']:+.2f}, média {r['selm_p']:+.2f} | Selic s-: nível {r['sel_n']:+.2f}, média {r['selm_n']:+.2f} | "
                f"J/Selic(nível) s+ {nrm(r['bp'], r['sel_p'])}, s- {nrm(r['bn'], r['sel_n'])} | "
                f"J/Selic(média) s+ {nrm(r['bp'], r['selm_p'])}, s- {nrm(r['bn'], r['selm_n'])}\n")

    f.write(f"\n=== CHOQUE COM A META SELIC DE FIM DE MÊS (SGS 432): LP linear, d.p. do choque = {sd2:.4f}; P55 = {scale2:.4f} ===\n")
    f.write("coef (p NW) {p EWC} [p Holm, h=3..24] | por 1 d.p.\n")
    for nm, r_ in meta.items():
        f.write(f"\n[{nm}]\n")
        for h in H_REPORT:
            r = r_[h]
            hh = f"{r['holm']:.3f}" if 'holm' in r else '  -  '
            f.write(f"h={h:2d} | {r['b']:+.4f} ({r['p']:.3f}) {{{r['pe']:.3f}}} [{hh}] | por 1 d.p. {r['b'] * sd2:+.4f}\n")

    f.write("\n=== PODER: efeito mínimo detectável (80%, 5%) = 2,80 x EP, em p.p. de comprometimento por +1 p.p. de Selic ===\n")
    f.write("J - S = -A (identidade); EP de NW e de EWC; especificação com defasagens próprias [só com controles do sistema]\n")
    for h in H_REPORT:
        s_, a_, j_ = tab['propria']['S (29034)'][h], tab['propria']['A (29036)'][h], tab['propria']['J (29033)'][h]
        s0, a0 = tab['sistema']['S (29034)'][h], tab['sistema']['A (29036)'][h]
        f.write(f"h={h:2d} | J: b {j_['b']:+.3f}, EP {j_['se']:.3f} | S: b {s_['b']:+.3f}, EP {s_['se']:.3f}, MDE {2.8 * s_['se']:.2f} "
                f"(EWC {2.8 * s_['se_ewc']:.2f}) [{2.8 * s0['se']:.2f}] | J-S (=-A): b {-a_['b']:+.3f}, EP {a_['se']:.3f}, MDE {2.8 * a_['se']:.2f} "
                f"(EWC {2.8 * a_['se_ewc']:.2f}) [{2.8 * a0['se']:.2f}]\n")

    f.write("\n=== RESPOSTA DE J POR p.p. DE SELIC NA TRAJETÓRIA (choque-base) ===\n")
    for h in H_REPORT:
        t_ = traj[h]
        f.write(f"h={h:2d} | J^h {t_['j']:+.3f} | Selic em t+h {t_['sel']:+.3f} | Selic média t..t+h {t_['selm']:+.3f} | "
                f"J/Selic(nível) {t_['j'] / t_['sel']:+.3f} | J/Selic(média) {t_['j'] / t_['selm']:+.3f}\n")
    th = traj[12]
    f.write(f"Escala do ciclo 2021-23 (Selic +{DF['selic'].loc['2021':'2023'].max() - DF['selic'].loc['2021-01-01']:.2f} p.p.; "
            f"J observado +{J.loc['2021':'2023'].max() - J.loc['2021-01-01']:.2f} p.p.): previsão linear em h=12 = "
            f"{th['j'] / th['sel'] * (DF['selic'].loc['2021':'2023'].max() - DF['selic'].loc['2021-01-01']):+.2f} (por Selic em nível) a "
            f"{th['j'] / th['selm'] * (DF['selic'].loc['2021':'2023'].max() - DF['selic'].loc['2021-01-01']):+.2f} (por Selic média); aproximação, sem correção de não linearidade\n")

    j = DF['juros_divida']; e = DF['endividamento']
    f.write(f"\nDescritivos: corr(J, Selic) = {j.corr(DF['selic']):.2f}; corr(J, E) = {j.corr(e):.2f}; "
            f"J/E média 2005 = {100 * (j / e).loc['2005'].mean():.1f}%, 2021 = {100 * (j / e).loc['2021'].mean():.1f}%, "
            f"ago/2026 = {100 * (j / e).iloc[-1]:.1f}%\n")
    f.write(f"J: fev/2026 {j.loc['2026-02-01']:.2f}, ago/2026 {j.loc['2026-08-01']:.2f}; Selic fev/2026 {DF['selic'].loc['2026-02-01']:.2f}, ago/2026 {DF['selic'].loc['2026-08-01']:.2f}\n")
    f.write(f"Episódio 2021-2023: J jan/2021 {j.loc['2021-01-01']:.2f}, máx. 2021-2023 {j.loc['2021':'2023'].max():.2f} "
            f"({j.loc['2021':'2023'].idxmax():%Y-%m}); Selic jan/2021 {DF['selic'].loc['2021-01-01']:.2f}, máx. {DF['selic'].loc['2021':'2023'].max():.2f}\n")
print(f"Salvo: {out}")
