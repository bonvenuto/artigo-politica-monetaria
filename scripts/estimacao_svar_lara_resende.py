"""
Script de Estimação Econométrica do SVAR (Versão Revisada Pós-Parecer):
Avaliação Empírica da Hipótese de André Lara Resende (2005 - 2026)
- Série correta de IPCA Itens Livres (SGS 11428) e IPCA Monitorados (SGS 4449)
- Inclusão da Taxa de Câmbio Nominal PTAX (SGS 3696) e Expectativas Focus 12m (Olinda/BCB)
- Variável financeira das famílias: Comprometimento de Renda com Juros da Dívida (SGS 29033)
- Normalização exata do choque estrutural de Cholesky para +1,00 p.p. na Taxa Selic em h = 0
Autor: Ângelo Augusto Bonvenuto
"""

import os
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10.5
plt.rcParams['axes.titlesize'] = 11.5
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 12.5

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "data"), exist_ok=True)


def fetch_bcb_series(code, name):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
    res = requests.get(url, timeout=25)
    if res.status_code != 200:
        raise ValueError(f"Falha ao baixar série {name} (código {code}): status {res.status_code}")
    data = res.json()
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df = df.rename(columns={'valor': name}).set_index('data')[[name]]
    return df


def fetch_focus_ipca_12m():
    url = (
        "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/"
        "ExpectativasMercadoInflacao12Meses?$filter=Indicador%20eq%20'IPCA'%20and%20"
        "Suavizada%20eq%20'S'%20and%20baseCalculo%20eq%200&$select=Data,Mediana&$format=json"
    )
    res = requests.get(url, timeout=30)
    if res.status_code != 200:
        raise ValueError(f"Falha ao baixar Expectativas Focus 12m: status {res.status_code}")
    data = res.json()['value']
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Mediana'] = pd.to_numeric(df['Mediana'], errors='coerce')
    s = df.set_index('Data')['Mediana'].resample('MS').mean().rename('exp_ipca_12m')
    return s.to_frame()


print("=== 1. Coletando e Verificando Séries Históricas do BCB (SGS e Olinda/Focus) ===")
series_map = {
    'selic': 4189,            # Selic efetiva acumulada no mês anualizada (% a.a.)
    'ipca_livres': 11428,     # IPCA - Itens Livres (% a.m.) [Série oficial de preços livres]
    'ipca_comerc': 4447,      # IPCA - Comercializáveis (% a.m.)
    'ipca_adm': 4449,         # IPCA - Monitorados/Administrados (% a.m.)
    'ipca_cheio': 433,        # IPCA - Índice Cheio (% a.m.)
    'endividamento': 29037,   # Endividamento das famílias com o SFN (% renda 12m)
    'servico_divida': 29034,  # Comprometimento de renda com serviço da dívida c/ ajuste sazonal (%)
    'juros_divida': 29033,    # Comprometimento de renda apenas com juros da dívida c/ ajuste sazonal (%)
    'ibc_br': 24364,          # IBC-Br com ajuste sazonal
    'ptax': 3696,             # Taxa de câmbio R$/US$ PTAX venda fim de período
    'ic_br': 27574            # Índice de Commodities Brasil (IC-Br) em USD
}

csv_path = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")

required_cols = list(series_map.keys()) + ['exp_ipca_12m']
need_download = True
if os.path.exists(csv_path):
    df_existing = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    if all(col in df_existing.columns for col in required_cols):
        print("Carregando base completa e verificada de", csv_path)
        df_clean = df_existing
        need_download = False

if need_download:
    print("Atualizando base de dados oficial do BCB (SGS 11428, 4449, 29033, PTAX e Focus 12m)...")
    df_all = pd.DataFrame()
    for col_name, sgs_code in series_map.items():
        print(f"  -> Baixando {col_name} (SGS {sgs_code})...")
        s = fetch_bcb_series(sgs_code, col_name)
        df_all = s if df_all.empty else df_all.join(s, how='outer')
    print("  -> Baixando exp_ipca_12m (Olinda / Focus IPCA 12m suavizada)...")
    s_focus = fetch_focus_ipca_12m()
    df_all = df_all.join(s_focus, how='outer')
    df_clean = df_all.loc['2005-03-01':'2026-08-01'].dropna()
    df_clean.to_csv(csv_path)
    print(f"Base salva com sucesso em {csv_path} (N = {len(df_clean)} observações mensais).")

print("\n=== 2. Gerando Figura 1: Evolução Histórica das Séries (2005-2026) ===")
fig, axes = plt.subplots(3, 1, figsize=(10.5, 11), sharex=True)

# Painel (a): Selic, Expectativas Focus 12m e IPCA Livres (11428) vs Monitorados (4449)
axes[0].plot(df_clean.index, df_clean['selic'], label='Taxa Selic Efetiva (% a.a.) [SGS 4189]', color='#003366', lw=2.0)
axes[0].plot(df_clean.index, df_clean['exp_ipca_12m'], label='Expectativa Focus IPCA 12m (% a.a.)', color='#2b83ba', lw=1.6, ls='-.')
ax0_twin = axes[0].twinx()
ax0_twin.plot(df_clean.index, df_clean['ipca_livres'], label='IPCA Itens Livres (% a.m.) [SGS 11428]', color='#cc3300', lw=1.2, alpha=0.85)
ax0_twin.plot(df_clean.index, df_clean['ipca_adm'], label='IPCA Monitorados (% a.m.) [SGS 4449]', color='#ff9900', lw=1.1, ls='--', alpha=0.75)
axes[0].set_ylabel('Selic / Expectativa 12m (% a.a.)', color='#003366')
ax0_twin.set_ylabel('Inflação Mensal (% a.m.)', color='#cc3300')
axes[0].set_title('(a) Taxa Selic, Expectativas Focus 12m e Inflação de Itens Livres vs. Monitorados', loc='left', fontweight='bold')
lines0, labels0 = axes[0].get_legend_handles_labels()
lines0_t, labels0_t = ax0_twin.get_legend_handles_labels()
axes[0].legend(lines0 + lines0_t, labels0 + labels0_t, loc='upper right', frameon=True, fontsize=8.5)

# Painel (b): Comprometimento com Juros (29033), Serviço Total (29034) e Endividamento (29037)
axes[1].plot(df_clean.index, df_clean['juros_divida'], label='Comprometimento c/ Juros da Dívida (% renda) [SGS 29033]', color='#1b7837', lw=2.1)
axes[1].plot(df_clean.index, df_clean['servico_divida'], label='Comprometimento c/ Serviço Total (% renda) [SGS 29034]', color='#7fbc41', lw=1.5, ls='--')
ax1_twin = axes[1].twinx()
ax1_twin.plot(df_clean.index, df_clean['endividamento'], label='Estoque de Endividamento (% renda 12m) [SGS 29037]', color='#762a83', lw=1.7, ls=':')
axes[1].set_ylabel('Comprometimento Mensal (%)', color='#1b7837')
ax1_twin.set_ylabel('Endividamento (% renda 12m)', color='#762a83')
axes[1].set_title('(b) Fragilidade Financeira das Famílias: Juros vs. Serviço Total e Endividamento no SFN', loc='left', fontweight='bold')
lines1, labels1 = axes[1].get_legend_handles_labels()
lines1_t, labels1_t = ax1_twin.get_legend_handles_labels()
axes[1].legend(lines1 + lines1_t, labels1 + labels1_t, loc='upper left', frameon=True, fontsize=8.5)

# Painel (c): IBC-Br, Câmbio PTAX e Commodities IC-Br
axes[2].plot(df_clean.index, df_clean['ibc_br'], label='IBC-Br Dessazonalizado [SGS 24364]', color='#222222', lw=1.8)
ax2_twin = axes[2].twinx()
ax2_twin.plot(df_clean.index, df_clean['ic_br'], label='Índice de Commodities IC-Br (USD) [SGS 27574]', color='#b2182b', lw=1.5, ls='--')
ax2_twin.plot(df_clean.index, df_clean['ptax'] * 50, label='Câmbio PTAX R$/US$ (×50 p/ escala) [SGS 3696]', color='#542788', lw=1.3, ls=':')
axes[2].set_ylabel('IBC-Br (Índice)', color='#222222')
ax2_twin.set_ylabel('IC-Br (USD) / PTAX (×50)', color='#b2182b')
axes[2].set_title('(c) Atividade Doméstica (IBC-Br), Câmbio Nominal (PTAX) e Commodities (IC-Br)', loc='left', fontweight='bold')
lines2, labels2 = axes[2].get_legend_handles_labels()
lines2_t, labels2_t = ax2_twin.get_legend_handles_labels()
axes[2].legend(lines2 + lines2_t, labels2 + labels2_t, loc='upper left', frameon=True, fontsize=8.5)

axes[2].xaxis.set_major_locator(mdates.YearLocator(2))
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.tight_layout()
fig1_path = os.path.join(OUTPUT_DIR, "figura1_series_historicas.png")
plt.savefig(fig1_path, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura1_series_historicas.png"), dpi=300)
plt.close()
print(f"Salvo: {fig1_path}")

# === 3. Preparação do Vetor Endógeno de 6 Variáveis e Testes ADF ===
# Ordenamento de Cholesky: [l_icbr, l_ptax, l_ibc, ipca_livres, selic, juros_divida]
df_var = pd.DataFrame(index=df_clean.index)
df_var['l_icbr'] = np.log(df_clean['ic_br'])
df_var['l_ptax'] = np.log(df_clean['ptax'])
df_var['l_ibc'] = np.log(df_clean['ibc_br'])
df_var['ipca_livres'] = df_clean['ipca_livres']
df_var['selic'] = df_clean['selic']
df_var['juros_divida'] = df_clean['juros_divida']

print("\n=== 3. Testes de Raiz Unitária (ADF) ===")
adf_lines = []
for col in df_var.columns:
    res_adf = adfuller(df_var[col], autolag='AIC')
    line = f"ADF {col:14s}: Estatística = {res_adf[0]:+.3f}, p-valor = {res_adf[1]:.4f}, Lags = {res_adf[2]}"
    print(line)
    adf_lines.append(line)

# === 4. Estimação do Modelo SVAR(6) com Identificação de Cholesky Normalizada (+1,00 p.p. Selic) ===
p = 6
model = VAR(df_var)
lag_sel = model.select_order(maxlags=12)
print("\n=== 4. Seleção de Defasagens ===")
print(lag_sel.summary())

res_var = model.fit(p)
HORIZONS = 24
irf = res_var.irf(HORIZONS)

P = np.linalg.cholesky(res_var.sigma_u)
selic_idx = list(df_var.columns).index('selic')
inf_idx = list(df_var.columns).index('ipca_livres')
jur_idx = list(df_var.columns).index('juros_divida')
ibc_idx = list(df_var.columns).index('l_ibc')
ptax_idx = list(df_var.columns).index('l_ptax')

# Escala do choque de Cholesky: 1 desvio-padrão equivale a P[selic_idx, selic_idx] p.p. na Selic em h=0.
# Dividimos orth_irfs e seus erros-padrão assintóticos por scale para normalizar em +1,00 p.p. de Selic em h=0.
scale = P[selic_idx, selic_idx]
orth_irfs_norm = irf.orth_irfs / scale
orth_stderr_norm = irf.stderr(orth=True) / scale

print(f"\nEscala do choque estrutural de 1 d.p. na Selic: {scale:.4f} p.p. (Normalizado para +1,00 p.p. em h=0)")

# === 5. Gerando Figura 2: Funções de Resposta ao Impulso (IRF) do SVAR ===
fig, axes = plt.subplots(2, 2, figsize=(12, 8.8))
h_axis = np.arange(HORIZONS + 1)

irf_plots = [
    (inf_idx, 'IPCA Itens Livres (% a.m.)', '(a) Resposta do IPCA Itens Livres (SGS 11428)\n[Choque de +1,00 p.p. na Selic c/ Controle de Câmbio]', '#cc0000', axes[0, 0]),
    (jur_idx, 'Comprometimento c/ Juros (% renda)', '(b) Comprometimento Familiar c/ Juros (SGS 29033)\n[Canal de Fragilidade Financeira das Famílias]', '#1b7837', axes[0, 1]),
    (ibc_idx, 'Log IBC-Br (Atividade Real)', '(c) Resposta do Nível de Atividade (Log IBC-Br)\n[Contração Gradual da Demanda Doméstica]', '#003366', axes[1, 0]),
    (selic_idx, 'Taxa Selic (% a.a.)', '(d) Trajetória da Taxa Selic após o Choque Inicial\n[Persistência e Inércia do Ciclo Monetário]', '#542788', axes[1, 1]),
]

for v_idx, ylabel, title, color, ax in irf_plots:
    y_hat = orth_irfs_norm[:, v_idx, selic_idx]
    se_hat = orth_stderr_norm[:, v_idx, selic_idx]
    lower = y_hat - 1.96 * se_hat
    upper = y_hat + 1.96 * se_hat

    ax.axhline(0, color='black', lw=1.0, ls='--')
    ax.plot(h_axis, y_hat, color=color, lw=2.3, label='IRF SVAR (+1,00 p.p. Selic)')
    ax.fill_between(h_axis, lower, upper, color=color, alpha=0.18, label='IC 95% Assintótico')
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('Horizonte Temporal (Meses)')
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(0, HORIZONS + 1, 3))
    ax.legend(loc='best', frameon=True)

plt.tight_layout()
fig2_path = os.path.join(OUTPUT_DIR, "figura2_irf_svar.png")
plt.savefig(fig2_path, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura2_irf_svar.png"), dpi=300)
plt.close()
print(f"Salvo: {fig2_path}")

# === 6. Gerando Figura 3: Decomposição da Variância do Erro de Previsão (FEVD) ===
fevd = res_var.fevd(HORIZONS)
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.4))
fevd_horizons = np.arange(1, HORIZONS + 1)
colors = ['#2b83ba', '#8073ac', '#abdda4', '#fdae61', '#d7191c', '#1b7837']
labels = [
    'Commodities (IC-Br)',
    'Câmbio (PTAX)',
    'Atividade (IBC-Br)',
    'Choques Próprios (IPCA Livres)',
    'Política Monetária (Selic)',
    'Encargos de Juros (Famílias)'
]

# Painel (a): FEVD do Comprometimento com Juros das Famílias (SGS 29033)
decomp_jur = fevd.decomp[jur_idx, :, :].T * 100
axes[0].stackplot(fevd_horizons, decomp_jur, labels=labels, colors=colors, alpha=0.88)
axes[0].set_title('(a) FEVD: Comprometimento Familiar c/ Juros (SGS 29033)', fontweight='bold')
axes[0].set_xlabel('Horizonte (Meses)')
axes[0].set_ylabel('Participação na Variância (%)')
axes[0].set_xlim(1, HORIZONS)
axes[0].set_ylim(0, 100)

# Painel (b): FEVD do IPCA Itens Livres (SGS 11428)
decomp_inf = fevd.decomp[inf_idx, :, :].T * 100
axes[1].stackplot(fevd_horizons, decomp_inf, labels=labels, colors=colors, alpha=0.88)
axes[1].set_title('(b) FEVD: Inflação de Itens Livres (SGS 11428)', fontweight='bold')
axes[1].set_xlabel('Horizonte (Meses)')
axes[1].set_ylabel('Participação na Variância (%)')
axes[1].set_xlim(1, HORIZONS)
axes[1].set_ylim(0, 100)
axes[1].legend(loc='upper right', frameon=True, fontsize=8.5)

plt.tight_layout()
fig3_path = os.path.join(OUTPUT_DIR, "figura3_fevd_svar.png")
plt.savefig(fig3_path, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura3_fevd_svar.png"), dpi=300)
plt.close()
print(f"Salvo: {fig3_path}")

# === 7. Salvar Resumo Completo em resultados/resultados_svar_summary.txt ===
summary_path = os.path.join(PROJECT_ROOT, "resultados", "resultados_svar_summary.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("=== RESUMO ECONOMÉTRICO DO SVAR(6) REVISADO (2005-2026, T = 258) ===\n")
    f.write("Vetor Endógeno (Cholesky): [l_icbr, l_ptax, l_ibc, ipca_livres (SGS 11428), selic, juros_divida (SGS 29033)]\n")
    f.write(f"Escala de 1 d.p. do choque na Selic: {scale:.4f} p.p. (IRFs normalizadas para +1,00 p.p. de Selic em h=0)\n\n")
    f.write("--- 1. Testes ADF ---\n")
    for l in adf_lines:
        f.write(l + "\n")
    f.write("\n--- 2. Respostas ao Impulso Normalizadas (+1,00 p.p. na Selic em h=0) ---\n")
    f.write("Horizonte | IPCA Livres (11428) [EP] | Juros Dívida (29033) [EP] | Log IBC-Br [EP] | Câmbio Log PTAX | Selic (% a.a.)\n")
    for h in [0, 3, 6, 9, 12, 18, 24]:
        f.write(
            f"h = {h:2d}    | "
            f"{orth_irfs_norm[h, inf_idx, selic_idx]:+8.4f} [{orth_stderr_norm[h, inf_idx, selic_idx]:.4f}] | "
            f"{orth_irfs_norm[h, jur_idx, selic_idx]:+9.4f} [{orth_stderr_norm[h, jur_idx, selic_idx]:.4f}] | "
            f"{orth_irfs_norm[h, ibc_idx, selic_idx]:+7.4f} [{orth_stderr_norm[h, ibc_idx, selic_idx]:.4f}] | "
            f"{orth_irfs_norm[h, ptax_idx, selic_idx]:+15.4f} | "
            f"{orth_irfs_norm[h, selic_idx, selic_idx]:+10.4f}\n"
        )
    f.write("\n--- 3. FEVD do IPCA Itens Livres (SGS 11428) (%) ---\n")
    f.write("Horizonte | IC-Br | PTAX | IBC-Br | IPCA Livres | Selic | Juros Dívida\n")
    for h in [1, 6, 12, 18, 24]:
        row = fevd.decomp[inf_idx, h - 1, :] * 100
        f.write(f"h = {h:2d}    | {row[0]:5.2f} | {row[1]:4.2f} | {row[2]:6.2f} | {row[3]:11.2f} | {row[4]:5.2f} | {row[5]:12.2f}\n")
    f.write("\n--- 4. FEVD do Comprometimento com Juros (SGS 29033) (%) ---\n")
    f.write("Horizonte | IC-Br | PTAX | IBC-Br | IPCA Livres | Selic | Juros Dívida\n")
    for h in [1, 6, 12, 18, 24]:
        row = fevd.decomp[jur_idx, h - 1, :] * 100
        f.write(f"h = {h:2d}    | {row[0]:5.2f} | {row[1]:4.2f} | {row[2]:6.2f} | {row[3]:11.2f} | {row[4]:5.2f} | {row[5]:12.2f}\n")

print(f"Resumo salvo em: {summary_path}")
