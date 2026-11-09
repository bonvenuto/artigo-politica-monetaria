"""
Script de Estimação de Projeções Locais Lineares (Jordà, 2005) — Versão Revisada Pós-Parecer
Comparação de Robustez com o modelo SVAR sob Normalização Exata (+1,00 p.p. de Choque na Selic em h = 0)
Variáveis: IPCA Itens Livres (SGS 11428), Comprometimento com Juros (SGS 29033), Log IBC-Br e Selic
Autor: Ângelo Augusto Bonvenuto
"""

import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10.5
plt.rcParams['axes.titlesize'] = 11.5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)

CSV_PATH = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")
df_clean = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)

# 1. Sistema de 6 variáveis: [l_icbr, l_ptax, l_ibc, ipca_livres (11428), selic, juros_divida (29033)]
df_var = pd.DataFrame(index=df_clean.index)
df_var['l_icbr'] = np.log(df_clean['ic_br'])
df_var['l_ptax'] = np.log(df_clean['ptax'])
df_var['l_ibc'] = np.log(df_clean['ibc_br'])
df_var['ipca_livres'] = df_clean['ipca_livres']
df_var['selic'] = df_clean['selic']
df_var['juros_divida'] = df_clean['juros_divida']

p = 6
HORIZONS = 24
res_var = VAR(df_var).fit(p)
irf_svar = res_var.irf(HORIZONS)
selic_idx = list(df_var.columns).index('selic')

# 2. Choque estrutural de Cholesky normalizado para +1,00 p.p. de impacto na Selic em h = 0
# Como u_t = P * e_t, um choque estrutural de 1 d.p. (e_{selic,t} = 1) eleva a Selic em P[selic, selic] p.p. em h = 0.
# Logo, definindo Shock_t^{1pp} = e_{selic,t} * P[selic, selic], um aumento de 1 unidade em Shock_t^{1pp}
# corresponde exatamente a um choque estrutural não antecipado de +1,00 p.p. na taxa Selic em h = 0.
residuals = res_var.resid
P = np.linalg.cholesky(res_var.sigma_u)
P_inv = np.linalg.inv(P)
scale = P[selic_idx, selic_idx]

structural_shocks_std = (P_inv @ residuals.T).T
structural_shocks_std.index = residuals.index
shock_1pp = structural_shocks_std.iloc[:, selic_idx] * scale

# IRFs ortogonalizadas do SVAR na mesma escala (+1,00 p.p. em h = 0)
svar_orth_norm = irf_svar.orth_irfs / scale
svar_stderr_norm = irf_svar.stderr(orth=True) / scale

# 3. Estimação das Projeções Locais (Jordà, 2005)
target_vars = ['ipca_livres', 'juros_divida', 'l_ibc', 'selic']
lp_results = {var: {'irf': [], 'lower': [], 'upper': [], 'se': [], 'pval': []} for var in target_vars}

controls = []
for k in range(1, p + 1):
    for col in df_var.columns:
        s_lag = df_var[col].shift(k)
        s_lag.name = f"{col}_lag{k}"
        controls.append(s_lag)
df_controls = pd.concat(controls, axis=1)

for h in range(HORIZONS + 1):
    for var in target_vars:
        y_lead = df_var[var].shift(-h)
        reg_df = pd.DataFrame({'y_lead': y_lead, 'shock': shock_1pp}).join(df_controls).dropna()
        X = sm.add_constant(reg_df[['shock'] + [c.name for c in controls]])
        y = reg_df['y_lead']

        hac_maxlags = max(1, h + 1)
        ols_res = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': hac_maxlags})

        beta_shock = ols_res.params['shock']
        se_shock = ols_res.bse['shock']
        pval_shock = ols_res.pvalues['shock']

        lp_results[var]['irf'].append(beta_shock)
        lp_results[var]['se'].append(se_shock)
        lp_results[var]['pval'].append(pval_shock)
        lp_results[var]['lower'].append(beta_shock - 1.96 * se_shock)
        lp_results[var]['upper'].append(beta_shock + 1.96 * se_shock)

# 4. Gerar Figura 4: Comparação SVAR vs. Projeções Locais (Escala +1,00 p.p. Selic)
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

plot_specs = [
    ('ipca_livres', 'IPCA Itens Livres (% a.m.)', '(a) Resposta do IPCA Itens Livres (SGS 11428)\n[SVAR vs. Projeções Locais — Choque +1,00 p.p. Selic]', axes[0, 0]),
    ('juros_divida', 'Comprometimento c/ Juros (% renda)', '(b) Comprometimento de Renda c/ Juros (SGS 29033)\n[SVAR vs. Projeções Locais — Choque +1,00 p.p. Selic]', axes[0, 1]),
    ('l_ibc', 'Log IBC-Br (Nível de Atividade)', '(c) Resposta da Atividade Econômica Real (Log IBC-Br)', axes[1, 0]),
    ('selic', 'Taxa Selic (% a.a.)', '(d) Trajetória da Taxa Selic (+1,00 p.p. em h = 0)', axes[1, 1])
]

h_axis = np.arange(HORIZONS + 1)

for var_name, y_label, title, ax in plot_specs:
    var_idx = list(df_var.columns).index(var_name)
    svar_resp = svar_orth_norm[:, var_idx, selic_idx]

    lp_resp = np.array(lp_results[var_name]['irf'])
    lp_low = np.array(lp_results[var_name]['lower'])
    lp_high = np.array(lp_results[var_name]['upper'])

    ax.axhline(0, color='black', lw=1.0, ls='--')
    ax.plot(h_axis, svar_resp, color='#cc0000', lw=2.2, ls='-', marker='o', markersize=3.5, label='SVAR (Cholesky, +1 p.p.)')
    ax.plot(h_axis, lp_resp, color='#004c99', lw=2.2, ls='--', marker='s', markersize=3.5, label='Projeções Locais (Jordà, +1 p.p.)')
    ax.fill_between(h_axis, lp_low, lp_high, color='#004c99', alpha=0.18, label='IC 95% LP (Newey-West HAC)')

    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('Horizonte Temporal (Meses)')
    ax.set_ylabel(y_label)
    ax.set_xticks(range(0, HORIZONS + 1, 3))
    ax.legend(loc='best', frameon=True, fontsize=8.5)

plt.tight_layout()
fig4_path = os.path.join(OUTPUT_DIR, "figura4_lp_vs_svar.png")
plt.savefig(fig4_path, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura4_lp_vs_svar.png"), dpi=300)
plt.close()
print(f"Salvo: {fig4_path}")

# 5. Salvar Tabela Comparativa em resultados/comparacao_svar_vs_lp.txt
inf_idx = list(df_var.columns).index('ipca_livres')
jur_idx = list(df_var.columns).index('juros_divida')

out_txt = os.path.join(PROJECT_ROOT, "resultados", "comparacao_svar_vs_lp.txt")
with open(out_txt, "w", encoding="utf-8") as f:
    f.write("=== COMPARAÇÃO NORMALIZADA (+1,00 p.p. SELIC EM h=0): SVAR vs. PROJEÇÕES LOCAIS (JORDÀ, 2005) ===\n")
    f.write("Sistema de 6 variáveis: [l_icbr, l_ptax, l_ibc, ipca_livres (SGS 11428), selic, juros_divida (SGS 29033)]\n\n")
    f.write("Horizonte | IPCA Livres SVAR | IPCA Livres LP (EP) [p-val] | Juros Dívida SVAR | Juros Dívida LP (EP) [p-val] | IC 95% LP (Juros Dívida)\n")
    for h in [0, 3, 6, 9, 12, 18, 24]:
        s_inf = svar_orth_norm[h, inf_idx, selic_idx]
        l_inf = lp_results['ipca_livres']['irf'][h]
        se_inf = lp_results['ipca_livres']['se'][h]
        p_inf = lp_results['ipca_livres']['pval'][h]

        s_jur = svar_orth_norm[h, jur_idx, selic_idx]
        l_jur = lp_results['juros_divida']['irf'][h]
        se_jur = lp_results['juros_divida']['se'][h]
        p_jur = lp_results['juros_divida']['pval'][h]
        lo_jur = lp_results['juros_divida']['lower'][h]
        hi_jur = lp_results['juros_divida']['upper'][h]

        f.write(
            f"h = {h:2d}    | {s_inf:+16.4f} | {l_inf:+8.4f} ({se_inf:.4f}) [{p_inf:.3f}] | "
            f"{s_jur:+17.4f} | {l_jur:+9.4f} ({se_jur:.4f}) [{p_jur:.3f}] | [{lo_jur:+.4f}; {hi_jur:+.4f}]\n"
        )

print(f"Salvo: {out_txt}")
