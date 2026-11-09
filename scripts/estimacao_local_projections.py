"""
Script de Estimação de Projeções Locais (Jordà, 2005)
Comparação de Robustez com o modelo SVAR
Variáveis: IPCA Preços Livres e Comprometimento de Renda c/ Serviço da Dívida
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
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)

CSV_PATH = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")
if not os.path.exists(CSV_PATH) and os.path.exists(os.path.join(PROJECT_ROOT, "base_macro_bcb.csv")):
    CSV_PATH = os.path.join(PROJECT_ROOT, "base_macro_bcb.csv")

# 1. Carregar dados
df_clean = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)

df_var = pd.DataFrame(index=df_clean.index)
df_var['l_icbr'] = np.log(df_clean['ic_br'])
df_var['l_ibc'] = np.log(df_clean['ibc_br'])
df_var['ipca_livres'] = df_clean['ipca_livres']
df_var['selic'] = df_clean['selic']
df_var['servico_divida'] = df_clean['servico_divida']

# 2. Estimar VAR(6) de referência e recuperar choque ortogonalizado de Cholesky
p = 6
model_var = VAR(df_var)
res_var = model_var.fit(p)
HORIZONS = 24
irf_svar = res_var.irf(HORIZONS)
selic_idx = list(df_var.columns).index('selic')

# Choques estruturais via Cholesky
# u_t = A0^-1 e_t => e_t = P^-1 u_t, onde P é a matriz triangular inferior de Cholesky de Sigma
residuals = res_var.resid
sigma_u = res_var.sigma_u
P = np.linalg.cholesky(sigma_u)
P_inv = np.linalg.inv(P)

# Série temporal dos choques estruturais
structural_shocks = (P_inv @ residuals.T).T
structural_shocks.index = residuals.index
shock_series = structural_shocks.iloc[:, selic_idx]  # Choque de política monetária

# 3. Estimação das Projeções Locais (Jordà, 2005)
# Para cada h em [0, HORIZONS]:
# y_{t+h} = alpha_h + beta_h * Shock_t + sum_{k=1}^p Gamma_{h,k} * Y_{t-k} + eps_{t+h}
# Erros-padrão Newey-West com defasagem h + 1

target_vars = ['ipca_livres', 'servico_divida', 'l_ibc', 'selic']
lp_results = {var: {'irf': [], 'lower': [], 'upper': [], 'se': []} for var in target_vars}

# Criar defasagens de controle (lagged controls)
controls = []
for k in range(1, p + 1):
    for col in df_var.columns:
        s_lag = df_var[col].shift(k)
        s_lag.name = f"{col}_lag{k}"
        controls.append(s_lag)
df_controls = pd.concat(controls, axis=1)

for h in range(HORIZONS + 1):
    # Alinhar dados para o horizonte h
    # A variável dependente é y_{t+h}
    for var in target_vars:
        y_lead = df_var[var].shift(-h)
        
        # DataFrame de regressão
        reg_df = pd.DataFrame({
            'y_lead': y_lead,
            'shock': shock_series
        }).join(df_controls).dropna()
        
        X = sm.add_constant(reg_df[['shock'] + [c.name for c in controls]])
        y = reg_df['y_lead']
        
        # Regressão OLS com Newey-West (HAC) bandwidth = h + 1
        hac_maxlags = max(1, h + 1)
        ols_res = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': hac_maxlags})
        
        beta_shock = ols_res.params['shock']
        se_shock = ols_res.bse['shock']
        
        lp_results[var]['irf'].append(beta_shock)
        lp_results[var]['se'].append(se_shock)
        lp_results[var]['lower'].append(beta_shock - 1.96 * se_shock)
        lp_results[var]['upper'].append(beta_shock + 1.96 * se_shock)

# 4. Gerar Gráfico Comparativo: SVAR vs. Projeções Locais (Jordà)
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

plot_specs = [
    ('ipca_livres', 'IPCA Preços Livres (% a.m.)', '(a) Resposta da Inflação de Preços Livres\n[Price Puzzle: SVAR vs. Projeções Locais]', axes[0, 0]),
    ('servico_divida', 'Comprometimento de Renda (% renda)', '(b) Comprometimento de Renda c/ Serviço da Dívida\n[Fragilidade Financeira Minskyana: SVAR vs. LP]', axes[0, 1]),
    ('l_ibc', 'Log IBC-Br (Nível de Atividade)', '(c) Resposta da Atividade Econômica Real', axes[1, 0]),
    ('selic', 'Taxa Selic (% a.a.)', '(d) Trajetória da Selic após o Choque', axes[1, 1])
]

h_axis = np.arange(HORIZONS + 1)

for var_name, y_label, title, ax in plot_specs:
    var_idx = list(df_var.columns).index(var_name)
    
    # SVAR IRF
    svar_resp = irf_svar.irfs[:, var_idx, selic_idx]
    svar_se = irf_svar.stderr()[:, var_idx, selic_idx]
    svar_low = svar_resp - 1.96 * svar_se
    svar_up = svar_resp + 1.96 * svar_se
    
    # LP IRF
    lp_resp = np.array(lp_results[var_name]['irf'])
    lp_low = np.array(lp_results[var_name]['lower'])
    lp_up = np.array(lp_results[var_name]['upper'])
    
    # Plot SVAR
    ax.plot(h_axis, svar_resp, color='#003366', lw=2.2, label='SVAR (Cholesky, p=6)')
    ax.plot(h_axis, svar_low, color='#003366', lw=1.0, ls=':')
    ax.plot(h_axis, svar_up, color='#003366', lw=1.0, ls=':')
    
    # Plot Local Projections
    ax.plot(h_axis, lp_resp, color='#b2182b', lw=2.2, ls='--', marker='o', markersize=4, label='Projeções Locais (Jordà, 2005)')
    ax.fill_between(h_axis, lp_low, lp_up, color='#f4a582', alpha=0.3, label='IC 95% Projeções Locais (HAC)')
    
    ax.axhline(0, color='black', lw=0.8, ls='-')
    ax.set_title(title, loc='left', fontweight='bold', fontsize=11)
    ax.set_ylabel(y_label)
    ax.set_xlabel('Meses após o choque monetário')
    ax.set_xlim(0, HORIZONS)
    ax.legend(loc='best', frameon=True, fontsize=9)

plt.tight_layout()
fig_comp_path = os.path.join(PROJECT_ROOT, "figura4_lp_vs_svar.png")
fig_comp_figuras = os.path.join(OUTPUT_DIR, "figura4_lp_vs_svar.png")
plt.savefig(fig_comp_path, dpi=300)
plt.savefig(fig_comp_figuras, dpi=300)
plt.close()
print(f"Salvo: {fig_comp_path}")

# 5. Salvar tabela comparativa numérica
summary_txt = os.path.join(PROJECT_ROOT, "resultados", "comparacao_svar_vs_lp.txt")
with open(summary_txt, 'w', encoding='utf-8') as f:
    f.write("=== TABELA COMPARATIVA: SVAR vs. PROJEÇÕES LOCAIS (JORDÀ, 2005) ===\n\n")
    for var in target_vars:
        f.write(f"--- Variável: {var} ---\n")
        f.write("Horizonte (h) | SVAR IRF | LP IRF | LP Erro-Padrão (HAC) | LP IC 95%\n")
        var_idx = list(df_var.columns).index(var)
        for h in [0, 3, 6, 9, 12, 18, 24]:
            svar_val = irf_svar.irfs[h, var_idx, selic_idx]
            lp_val = lp_results[var]['irf'][h]
            lp_se_val = lp_results[var]['se'][h]
            lp_l = lp_results[var]['lower'][h]
            lp_u = lp_results[var]['upper'][h]
            f.write(f"h = {h:2d}        | {svar_val:8.4f} | {lp_val:7.4f} | {lp_se_val:20.4f} | [{lp_l:7.4f}, {lp_u:7.4f}]\n")
        f.write("\n")

print("Estimação de Projeções Locais concluída com sucesso!")
