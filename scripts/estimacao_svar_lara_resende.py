"""
Script de Estimação Econométrica do SVAR:
Hipótese de André Lara Resende (Canal de Custos e Fragilidade Financeira)
Período: 2005 - 2026 (Mensal)
Autor: Pipeline Acadêmico
"""

import sys
import os
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller

# Configuração estética dos gráficos para publicação acadêmica
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 13

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "data"), exist_ok=True)

def fetch_bcb_series(code, name):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
    res = requests.get(url, timeout=20)
    if res.status_code != 200:
        raise ValueError(f"Falha ao baixar série {name} (código {code}): status {res.status_code}")
    data = res.json()
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df = df.rename(columns={'valor': name}).set_index('data')
    return df

print("=== 1. Coletando Séries Históricas do Banco Central do Brasil (SGS) ===")
series_map = {
    'selic': 4189,            # Selic efetiva acumulada no mês (% a.a.)
    'ipca_livres': 4447,      # IPCA Preços Livres (% a.m.)
    'ipca_adm': 4448,         # IPCA Preços Administrados (% a.m.)
    'ipca_cheio': 433,        # IPCA Cheio (% a.m.)
    'endividamento': 29037,   # Endividamento familiar c/ SFN (% renda 12m)
    'servico_divida': 29034,  # Comprometimento de renda com serviço da dívida c/ ajuste (% renda mensal)
    'juros_divida': 29033,    # Comprometimento de renda apenas com juros c/ ajuste (%)
    'ibc_br': 24364,          # IBC-Br c/ ajuste sazonal
    'ptax': 3696,             # Câmbio PTAX de fim de período (R$/US$)
    'ic_br': 27574            # Índice de Commodities Brasil em USD
}

csv_path = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")
if not os.path.exists(csv_path) and os.path.exists(os.path.join(PROJECT_ROOT, "base_macro_bcb.csv")):
    csv_path = os.path.join(PROJECT_ROOT, "base_macro_bcb.csv")
if os.path.exists(csv_path):
    print("Carregando base pré-salva de", csv_path)
    df_clean = pd.read_csv(csv_path, index_col=0, parse_dates=True)
else:
    df_all = pd.DataFrame()
    for col_name, sgs_code in series_map.items():
        print(f"Baixando {col_name} (SGS {sgs_code})...")
        s = fetch_bcb_series(sgs_code, col_name)
        if df_all.empty:
            df_all = s
        else:
            df_all = df_all.join(s, how='outer')
    df_clean = df_all.loc['2005-03-01':].dropna()
    df_clean.to_csv(csv_path)

print("\n=== 2. Gerando Gráfico 1: Evolução Histórica das Séries ===")
fig, axes = plt.subplots(3, 1, figsize=(10, 11), sharex=True)

# Painel 1: Taxa Selic e Inflação (Livres vs Adm)
axes[0].plot(df_clean.index, df_clean['selic'], label='Taxa Selic Efetiva (% a.a.)', color='#003366', lw=2)
ax0_twin = axes[0].twinx()
ax0_twin.plot(df_clean.index, df_clean['ipca_livres'], label='IPCA Preços Livres (% a.m.)', color='#cc3300', lw=1.3, alpha=0.85)
ax0_twin.plot(df_clean.index, df_clean['ipca_adm'], label='IPCA Administrados (% a.m.)', color='#ff9900', lw=1.2, ls='--', alpha=0.8)
axes[0].set_ylabel('Taxa Selic (% a.a.)', color='#003366')
ax0_twin.set_ylabel('Inflação Mensal (%)', color='#cc3300')
axes[0].set_title('(a) Política Monetária e Dinâmica Inflacionária Desagregada', loc='left', fontweight='bold')
lines0, labels0 = axes[0].get_legend_handles_labels()
lines0_t, labels0_t = ax0_twin.get_legend_handles_labels()
axes[0].legend(lines0 + lines0_t, labels0 + labels0_t, loc='upper left', frameon=True)

# Painel 2: Comprometimento de Renda e Endividamento Familiar
axes[1].plot(df_clean.index, df_clean['servico_divida'], label='Comprometimento c/ Serviço da Dívida (% renda mensal)', color='#1b7837', lw=2)
axes[1].plot(df_clean.index, df_clean['juros_divida'], label='Comprometimento c/ Juros (% renda)', color='#7fbc41', lw=1.5, ls='--')
ax1_twin = axes[1].twinx()
ax1_twin.plot(df_clean.index, df_clean['endividamento'], label='Endividamento das Famílias (% renda 12m)', color='#762a83', lw=1.8, ls=':')
axes[1].set_ylabel('Comprometimento (%)', color='#1b7837')
ax1_twin.set_ylabel('Endividamento (% renda anual)', color='#762a83')
axes[1].set_title('(b) Estrutura Financeira das Famílias no SFN', loc='left', fontweight='bold')
lines1, labels1 = axes[1].get_legend_handles_labels()
lines1_t, labels1_t = ax1_twin.get_legend_handles_labels()
axes[1].legend(lines1 + lines1_t, labels1 + labels1_t, loc='upper left', frameon=True)

# Painel 3: Atividade (IBC-Br) e Commodities (IC-Br)
axes[2].plot(df_clean.index, df_clean['ibc_br'], label='IBC-Br Dessazonalizado (2002=100)', color='#333333', lw=1.8)
ax2_twin = axes[2].twinx()
ax2_twin.plot(df_clean.index, df_clean['ic_br'], label='Índice de Commodities Brasil (USD)', color='#b2182b', lw=1.5, ls='--')
axes[2].set_ylabel('IBC-Br', color='#333333')
ax2_twin.set_ylabel('IC-Br (USD)', color='#b2182b')
axes[2].set_title('(c) Atividade Econômica Doméstica e Choque Externo de Commodities', loc='left', fontweight='bold')
lines2, labels2 = axes[2].get_legend_handles_labels()
lines2_t, labels2_t = ax2_twin.get_legend_handles_labels()
axes[2].legend(lines2 + lines2_t, labels2 + labels2_t, loc='upper left', frameon=True)

axes[2].xaxis.set_major_locator(mdates.YearLocator(2))
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.tight_layout()
fig_path1 = os.path.join(OUTPUT_DIR, "figura1_series_historicas.png")
plt.savefig(fig_path1, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura1_series_historicas.png"), dpi=300)
plt.close()
print(f"Salvo: {fig_path1}")

print("\n=== 3. Testes de Raiz Unitária (ADF) ===")
# Transformações: log de variáveis de nível, taxas em percentual
df_var = pd.DataFrame(index=df_clean.index)
df_var['l_icbr'] = np.log(df_clean['ic_br'])
df_var['l_ibc'] = np.log(df_clean['ibc_br'])
df_var['ipca_livres'] = df_clean['ipca_livres']
df_var['selic'] = df_clean['selic']
df_var['servico_divida'] = df_clean['servico_divida']

for col in df_var.columns:
    res_adf = adfuller(df_var[col], autolag='AIC')
    print(f"ADF {col:15s}: Estatística = {res_adf[0]:.3f}, p-valor = {res_adf[1]:.4f}, Lags = {res_adf[2]}")

print("\n=== 4. Estimação do Modelo SVAR ===")
# Seleção de Defasagens
model = VAR(df_var)
lag_selection = model.select_order(maxlags=8)
print("Critérios de seleção de ordem:")
print(lag_selection.summary())
opt_lag = lag_selection.aic
if opt_lag < 1:
    opt_lag = 2
print(f"Ordem ótima selecionada (AIC): p = {opt_lag}")

var_res = model.fit(opt_lag)
print(var_res.summary())

# Identificação Estrutural de Cholesky
# Ordenamento: [l_icbr, l_ibc, ipca_livres, selic, servico_divida]
# Racional teórico:
# 1. IC-Br: commodities globais exógenas à economia brasileira no mês
# 2. IBC-Br: atividade econômica real
# 3. IPCA Livres: inflação contemporânea de preços flexíveis
# 4. Selic: regra de política monetária (reage a choque externo, atividade e inflação contemporâneos)
# 5. Serviço da Dívida: absorve contemporaneamente o repasse das taxas de juros no mês

HORIZONS = 24
irf = var_res.irf(HORIZONS)

print("\n=== 5. Gerando Gráfico 2: Funções de Resposta ao Impulso (IRF) ===")
# Resposta das variáveis a um choque positivo não antecipado na Selic (1 d.p.)
# Índice de 'selic' no vetor é 3
selic_idx = list(df_var.columns).index('selic')

fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))

target_vars = [
    ('ipca_livres', 'IPCA Preços Livres (% a.m.)', '(a) Resposta da Inflação de Preços Livres\n[Teste do Price Puzzle]', axes[0, 0]),
    ('servico_divida', 'Comprometimento de Renda (% renda)', '(b) Resposta do Comprometimento de Renda\n[Fragilidade Financeira Minskyana]', axes[0, 1]),
    ('l_ibc', 'Log IBC-Br (Nível de Atividade)', '(c) Resposta da Atividade Econômica Real', axes[1, 0]),
    ('selic', 'Taxa Selic (% a.a.)', '(d) Persistência do Choque na Selic', axes[1, 1])
]

# Calcular intervalos assintóticos / bootstrap
# statsmodels irf.plot() gera com intervalos
for var_name, y_label, title, ax in target_vars:
    var_idx = list(df_var.columns).index(var_name)
    response = irf.irfs[:, var_idx, selic_idx]
    stderr = irf.stderr()[:, var_idx, selic_idx]
    lower = response - 1.96 * stderr
    upper = response + 1.96 * stderr
    h = np.arange(HORIZONS + 1)
    
    ax.plot(h, response, color='#003366', lw=2.2, label='Resposta Estrutural (IRF)')
    ax.fill_between(h, lower, upper, color='#4a90e2', alpha=0.25, label='Intervalo de Confiança 95%')
    ax.axhline(0, color='black', lw=0.9, ls='--')
    ax.set_title(title, loc='left', fontweight='bold', fontsize=11)
    ax.set_ylabel(y_label)
    ax.set_xlabel('Meses após o choque')
    ax.set_xlim(0, HORIZONS)
    ax.legend(loc='best', frameon=True)

plt.tight_layout()
fig_path2 = os.path.join(OUTPUT_DIR, "figura2_irf_svar.png")
plt.savefig(fig_path2, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura2_irf_svar.png"), dpi=300)
plt.close()
print(f"Salvo: {fig_path2}")

print("\n=== 6. Decomposição da Variância do Erro de Previsão (FEVD) ===")
fevd = var_res.fevd(HORIZONS)
print(fevd.summary())

# Gráfico da Decomposição de Variância para Comprometimento de Renda e IPCA
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# FEVD do Comprometimento de Renda
fevd_servico = fevd.decomp[list(df_var.columns).index('servico_divida')]
axes[0].stackplot(range(1, HORIZONS + 1), fevd_servico.T * 100,
                  labels=['IC-Br', 'IBC-Br', 'IPCA Livres', 'Selic', 'Serviço Dívida'],
                  colors=['#8c510a', '#01665e', '#d8b365', '#003366', '#5ab4ac'], alpha=0.85)
axes[0].set_title('(a) FEVD: Comprometimento de Renda com Serviço da Dívida', loc='left', fontweight='bold')
axes[0].set_xlabel('Horizonte (Meses)')
axes[0].set_ylabel('% da Variância Explicada')
axes[0].set_xlim(1, HORIZONS)
axes[0].set_ylim(0, 100)
axes[0].legend(loc='lower right', frameon=True)

# FEVD do IPCA Livres
fevd_ipca = fevd.decomp[list(df_var.columns).index('ipca_livres')]
axes[1].stackplot(range(1, HORIZONS + 1), fevd_ipca.T * 100,
                  labels=['IC-Br', 'IBC-Br', 'IPCA Livres', 'Selic', 'Serviço Dívida'],
                  colors=['#8c510a', '#01665e', '#d8b365', '#003366', '#5ab4ac'], alpha=0.85)
axes[1].set_title('(b) FEVD: Inflação de Preços Livres', loc='left', fontweight='bold')
axes[1].set_xlabel('Horizonte (Meses)')
axes[1].set_ylabel('% da Variância Explicada')
axes[1].set_xlim(1, HORIZONS)
axes[1].set_ylim(0, 100)
axes[1].legend(loc='lower right', frameon=True)

plt.tight_layout()
fig_path3 = os.path.join(OUTPUT_DIR, "figura3_fevd_svar.png")
plt.savefig(fig_path3, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura3_fevd_svar.png"), dpi=300)
plt.close()
print(f"Salvo: {fig_path3}")

# Exportar resultados tabulares em formato resumo
summary_file = os.path.join(PROJECT_ROOT, "resultados", "resultados_svar_summary.txt")
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write(f"=== RESULTADOS DA ESTIMAÇÃO DO SVAR (LARA RESENDE) ===\n")
    f.write(f"Amostra: {df_clean.index[0].strftime('%Y-%m')} a {df_clean.index[-1].strftime('%Y-%m')} (N = {len(df_clean)})\n")
    f.write(f"Defasagens selecionadas (AIC): {opt_lag}\n\n")
    f.write("RESPOSTA AO CHOQUE DE SELIC:\n")
    for var_name, y_label, title, _ in target_vars:
        var_idx = list(df_var.columns).index(var_name)
        resp_h0 = irf.irfs[0, var_idx, selic_idx]
        resp_h6 = irf.irfs[6, var_idx, selic_idx]
        resp_h12 = irf.irfs[12, var_idx, selic_idx]
        resp_h24 = irf.irfs[24, var_idx, selic_idx]
        f.write(f"- {var_name}: h=0: {resp_h0:.4f} | h=6: {resp_h6:.4f} | h=12: {resp_h12:.4f} | h=24: {resp_h24:.4f}\n")

print("\nExecução econométrica concluída com pleno sucesso!")
