"""
Script de Estimação de Projeções Locais Dependentes de Estado (Jordà, 2005)
Avaliação Empírica de "Eu Acuso: uma proposta para eliminar os juros absurdos" (Lara Resende, 2026)
Testa o efeito inflacionário da manutenção de juros persistentemente altos (Platô de Juros)
e o efeito desinflacionário da redução da Selic a partir de patamares elevados.
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
plt.rcParams['axes.titlesize'] = 11.5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)

CSV_PATH = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")
df_clean = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)

df_var = pd.DataFrame(index=df_clean.index)
df_var['l_icbr'] = np.log(df_clean['ic_br'])
df_var['l_ibc'] = np.log(df_clean['ibc_br'])
df_var['ipca_livres'] = df_clean['ipca_livres']
df_var['selic'] = df_clean['selic']
df_var['servico_divida'] = df_clean['servico_divida']

# Estimar VAR(6) e extrair choque estrutural ortogonalizado de Cholesky
p = 6
HORIZONS = 24
res_var = VAR(df_var).fit(p)
residuals = res_var.resid
P = np.linalg.cholesky(res_var.sigma_u)
shocks = (np.linalg.inv(P) @ residuals.T).T
shocks.index = residuals.index
selic_idx = list(df_var.columns).index('selic')
s_selic = shocks.iloc[:, selic_idx]

# Definir variável de estado: Platô de Juros Persistentemente Altos
# Indicadora I_t = 1 quando a média móvel de 12 meses da Selic supera a mediana histórica (11,27% a.a.)
selic_ma12 = df_var['selic'].rolling(12).mean()
threshold = selic_ma12.median()
high_plateau = (selic_ma12 > threshold).astype(float).shift(1)

controls = []
for k in range(1, p + 1):
    for col in df_var.columns:
        s_lag = df_var[col].shift(k)
        s_lag.name = f"{col}_lag{k}"
        controls.append(s_lag)
df_controls = pd.concat(controls, axis=1)

results_state = {
    'high': {'beta': [], 'se': [], 'p': [], 'low': [], 'up': []},
    'low': {'beta': [], 'se': [], 'p': [], 'low': [], 'up': []},
    'cut_serv': {'beta': [], 'se': [], 'p': [], 'low': [], 'up': []}
}

for h in range(HORIZONS + 1):
    # Inflação acumulada em h meses: sum_{j=0}^h pi_{t+j}
    cum_inf = df_var['ipca_livres'].rolling(h + 1).sum().shift(-h)
    
    reg_df = pd.concat([
        cum_inf.rename('y'),
        (s_selic * high_plateau).rename('shock_high'),
        (s_selic * (1.0 - high_plateau)).rename('shock_low'),
        high_plateau.rename('state')
    ] + [df_controls], axis=1).dropna()
    
    X = sm.add_constant(reg_df.drop(columns=['y']))
    ols = sm.OLS(reg_df['y'], X).fit(cov_type='HAC', cov_kwds={'maxlags': max(1, h + 1)})
    
    for regime, col_name in [('high', 'shock_high'), ('low', 'shock_low')]:
        b = ols.params[col_name]
        se = ols.bse[col_name]
        pval = ols.pvalues[col_name]
        results_state[regime]['beta'].append(b)
        results_state[regime]['se'].append(se)
        results_state[regime]['p'].append(pval)
        results_state[regime]['low'].append(b - 1.96 * se)
        results_state[regime]['up'].append(b + 1.96 * se)

    # Efeito no serviço da dívida no regime de juros altos
    y_serv = df_var['servico_divida'].shift(-h)
    reg_serv = pd.concat([
        y_serv.rename('y'),
        (s_selic * high_plateau).rename('shock_high'),
        (s_selic * (1.0 - high_plateau)).rename('shock_low'),
        high_plateau.rename('state')
    ] + [df_controls], axis=1).dropna()
    X_s = sm.add_constant(reg_serv.drop(columns=['y']))
    ols_s = sm.OLS(reg_serv['y'], X_s).fit(cov_type='HAC', cov_kwds={'maxlags': max(1, h + 1)})
    b_s = ols_s.params['shock_high']
    se_s = ols_s.bse['shock_high']
    results_state['cut_serv']['beta'].append(b_s)
    results_state['cut_serv']['se'].append(se_s)
    results_state['cut_serv']['p'].append(ols_s.pvalues['shock_high'])
    results_state['cut_serv']['low'].append(b_s - 1.96 * se_s)
    results_state['cut_serv']['up'].append(b_s + 1.96 * se_s)

# Gerar Figura 5
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
h_axis = np.arange(HORIZONS + 1)

# Painel (a): Inflação Acumulada sob Platô de Juros Altos vs Regime Moderado (+1 dp choque Selic)
ax = axes[0]
b_high = np.array(results_state['high']['beta'])
l_high = np.array(results_state['high']['low'])
u_high = np.array(results_state['high']['up'])

b_low = np.array(results_state['low']['beta'])
l_low = np.array(results_state['low']['low'])
u_low = np.array(results_state['low']['up'])

ax.plot(h_axis, b_high, color='#b2182b', lw=2.4, marker='o', markersize=4,
        label=f'Platô de Juros Altos (Média 12m > {threshold:.1f}% a.a.)')
ax.fill_between(h_axis, l_high, u_high, color='#f4a582', alpha=0.30, label='IC 95% (Platô de Juros Altos)')

ax.plot(h_axis, b_low, color='#2166ac', lw=2.2, ls='--', marker='s', markersize=4,
        label=f'Regime de Juros Moderados (≤ {threshold:.1f}% a.a.)')
ax.fill_between(h_axis, l_low, u_low, color='#92c5de', alpha=0.22, label='IC 95% (Juros Moderados)')

ax.axhline(0, color='black', lw=0.9, ls='-')
ax.set_title('(a) Inflação Livre Acumulada após Choque de Alta na Selic\n[Dependência de Estado: Platô de Juros Altos vs. Moderados]', loc='left', fontweight='bold')
ax.set_xlabel('Horizonte (Meses após o choque)')
ax.set_ylabel('Variação Acumulada do IPCA Livres (p.p.)')
ax.set_xlim(0, HORIZONS)
ax.legend(loc='lower left', frameon=True, fontsize=8.8)

# Painel (b): Efeito Desinflacionário Simétrico de um Corte da Selic (-1 dp) no Platô de Juros Altos
ax2 = axes[1]
cut_inf = -b_high
cut_inf_low = -u_high
cut_inf_up = -l_high

ax2.plot(h_axis, cut_inf, color='#1b7837', lw=2.5, marker='D', markersize=4,
         label='Redução Acumulada da Inflação Livre (p.p.)')
ax2.fill_between(h_axis, cut_inf_low, cut_inf_up, color='#a6dba0', alpha=0.35,
                 label='IC 95% HAC (Efeito Desinflacionário do Corte)')

ax2.axhline(0, color='black', lw=0.9, ls='-')
ax2.set_title('(b) Efeito de uma Redução da Selic a partir do Platô Elevado\n[Proposta Lara Resende (2026): Corte de Juros Reduz Inflação]', loc='left', fontweight='bold')
ax2.set_xlabel('Horizonte (Meses após o início da redução da Selic)')
ax2.set_ylabel('Variação Acumulada do IPCA Livres (p.p.)')
ax2.set_xlim(0, HORIZONS)
ax2.legend(loc='upper right', frameon=True, fontsize=9)

plt.tight_layout()
fig5_root = os.path.join(PROJECT_ROOT, "figura5_regime_juros_altos_lp.png")
fig5_dir = os.path.join(OUTPUT_DIR, "figura5_regime_juros_altos_lp.png")
plt.savefig(fig5_root, dpi=300)
plt.savefig(fig5_dir, dpi=300)
plt.close()
print(f"Salvo: {fig5_root}")

summary_path = os.path.join(PROJECT_ROOT, "resultados", "regime_juros_altos_lp.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write(f"=== PROJEÇÕES LOCAIS DEPENDENTES DE ESTADO (LARA RESENDE, 2026) ===\n")
    f.write(f"Limiar do Platô de Juros Altos (Mediana da MM12m da Selic): {threshold:.2f}% a.a.\n\n")
    f.write("Horizonte | Platô Alto (Infl. Acum.) | p-valor | Regime Moderado (Infl. Acum.) | p-valor | Corte de Juros no Platô Alto\n")
    for h in [0, 3, 6, 9, 12, 18, 24]:
        bh = results_state['high']['beta'][h]
        ph = results_state['high']['p'][h]
        bl = results_state['low']['beta'][h]
        pl = results_state['low']['p'][h]
        f.write(f"h = {h:2d}    | {bh:+24.4f} | {ph:7.4f} | {bl:+29.4f} | {pl:7.4f} | {-bh:+28.4f}\n")

print("Resumo salvo em:", summary_path)
