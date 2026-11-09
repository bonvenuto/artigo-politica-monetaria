"""
Projeções Locais lineares (Jordà, 2005) — versão 4.

- Choque: inovação de Cholesky da Selic no VAR(6) com dummies sazonais e IC-Br em US$ (comum.identify_shock);
- controles: 6 defasagens do sistema + 11 dummies sazonais (os mesmos regressores do VAR, de modo que a resposta
  em h=0 coincide com a do SVAR por construção — Frisch-Waugh-Lovell; não é evidência de aderência);
- inferência: Newey-West (h+1) e EWC (Lazarus et al., 2018); Holm na família h ∈ {3, 6, 9, 12, 18, 24};
- conversão para choque de 1 desvio-padrão.

Autor: Ângelo Augusto Bonvenuto
"""

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from comum import (FIG_DIR, H_FAMILY, H_REPORT, HORIZONS, PROJECT_ROOT, RES_DIR, SEASONAL, build_system, ewc,
                   holm, identify_shock, lag_controls, ols_hac)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10, 'axes.titlesize': 11.2})

v = build_system()
shock, scale, res_var = identify_shock(v)
sd = float(shock.std())
SI = list(v.columns).index('selic')
P = np.linalg.cholesky(res_var.sigma_u)
irf = res_var.irf(HORIZONS)
svar = irf.orth_irfs / scale
CTRL = pd.concat([lag_controls(v), SEASONAL], axis=1)

TARGETS = ['ipca_livres', 'juros_divida', 'l_ibc', 'selic']
lp = {t: {} for t in TARGETS}
for t in TARGETS:
    for h in range(HORIZONS + 1):
        o, d = ols_hac(v[t].shift(-h), pd.concat([shock.rename('shock'), CTRL], axis=1), h)
        _, se_e, _, p_e, nu = ewc(o, d, 'shock')
        lp[t][h] = dict(b=o.params['shock'], se=o.bse['shock'], p=o.pvalues['shock'], se_ewc=se_e, p_ewc=p_e)
    hp = holm([lp[t][h]['p'] for h in H_FAMILY])
    for h, x in zip(H_FAMILY, hp):
        lp[t][h]['p_holm'] = x

# Figura 4
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
h_axis = np.arange(HORIZONS + 1)
for (t, ylab, title), ax in zip([
    ('ipca_livres', 'IPCA livres (% a.m.)', '(a) IPCA itens livres (SGS 11428)'),
    ('juros_divida', 'Comprometimento c/ juros (% renda)', '(b) Comprometimento de renda com juros (SGS 29033)'),
    ('l_ibc', 'ln IBC-Br', '(c) Atividade (ln IBC-Br)'),
    ('selic', 'Selic (% a.a.)', '(d) Selic')], axes.flat):
    j = list(v.columns).index(t)
    b = np.array([lp[t][h]['b'] for h in h_axis]); s = np.array([lp[t][h]['se'] for h in h_axis])
    ax.axhline(0, color='black', lw=1.0, ls='--')
    ax.plot(h_axis, svar[:, j, SI], color='#cc0000', lw=2.2, marker='o', markersize=3.2, label='SVAR')
    ax.plot(h_axis, b, color='#004c99', lw=2.2, ls='--', marker='s', markersize=3.2, label='LP')
    ax.fill_between(h_axis, b - 1.96 * s, b + 1.96 * s, color='#004c99', alpha=0.16, label='IC 95% LP (Newey-West)')
    ax.set_title(title, fontweight='bold'); ax.set_xlabel('Horizonte (meses)'); ax.set_ylabel(ylab)
    ax.set_xticks(range(0, HORIZONS + 1, 3)); ax.legend(loc='best', frameon=True, fontsize=8.5)
plt.tight_layout()
for path in [os.path.join(FIG_DIR, "figura4_lp_vs_svar.png"), os.path.join(PROJECT_ROOT, "figura4_lp_vs_svar.png")]:
    plt.savefig(path, dpi=300)
plt.close()

out = os.path.join(RES_DIR, "comparacao_svar_vs_lp.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("=== TABELA 3: SVAR vs. LP LINEAR (versão 4: VAR e LP com 11 dummies sazonais; IC-Br em US$) ===\n")
    f.write(f"Choque +1 p.p. na Selic em h=0 | d.p. do choque = {sd:.4f} p.p. | P55 = {scale:.4f}\n")
    f.write("LP: coef (EP NW) [p NW] {p EWC} <p Holm, família h=3..24>\n")
    for t in ['ipca_livres', 'juros_divida', 'l_ibc', 'selic']:
        j = list(v.columns).index(t)
        f.write(f"\n[{t}]\n")
        for h in H_REPORT:
            r = lp[t][h]
            ph = f"{r['p_holm']:.3f}" if 'p_holm' in r else '  -  '
            f.write(f"h={h:2d} | SVAR {svar[h, j, SI]:+.4f} | LP {r['b']:+.4f} ({r['se']:.4f}) [{r['p']:.3f}] {{{r['p_ewc']:.3f}}} <{ph}> "
                    f"| por 1 d.p.: {r['b'] * sd:+.4f}\n")
    jm = max(range(HORIZONS + 1), key=lambda h: lp['juros_divida'][h]['b'])
    f.write(f"\nPico da LP de J^fam: h={jm}, {lp['juros_divida'][jm]['b']:+.4f} por 1 p.p. ({lp['juros_divida'][jm]['b'] * sd:+.4f} por 1 d.p.)\n")
print(f"Salvo: {out}")
