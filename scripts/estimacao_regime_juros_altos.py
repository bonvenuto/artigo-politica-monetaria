"""
Script de Estimação de Projeções Locais Dependentes de Estado e Assimétricas (Jordà, 2005; Tenreyro & Thwaites, 2016)
Versão Revisada Pós-Parecer (Atende integralmente a R1, R2, R4, R5, R6 e S2):
1. Série oficial de IPCA Itens Livres (SGS 11428) e controle de Câmbio Nominal (PTAX, SGS 3696)
2. Normalização exata do choque estrutural para +1,00 p.p. na Selic no impacto (h = 0)
3. Estimação e reporte do parâmetro de nível do regime (gamma^h) e teste de Wald H0: beta_alto = beta_mod
4. Estimação assimétrica separada para choques positivos (beta^+_alto) e cortes (beta^-_alto) sem espelhamento artificial
5. Bateria de robustez: Expectativas Focus 12m (Olinda/BCB), IPCA Cheio (SGS 433), Juro Real Ex-Ante, Limiares 10% e 12% e Dummies COVID/Sazonais
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
plt.rcParams['axes.titlesize'] = 11.2

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "figuras")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "resultados"), exist_ok=True)

CSV_PATH = os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv")
df_clean = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)

# 1. Sistema Base de 6 Variáveis: [l_icbr, l_ptax, l_ibc, ipca_livres (11428), selic, juros_divida (29033)]
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
residuals = res_var.resid
P = np.linalg.cholesky(res_var.sigma_u)
selic_idx = list(df_var.columns).index('selic')
scale = P[selic_idx, selic_idx]

# Choque estrutural normalizado para +1,00 p.p. de impacto na Selic em h = 0
shocks_std = (np.linalg.inv(P) @ residuals.T).T
shocks_std.index = residuals.index
s_1pp = shocks_std.iloc[:, selic_idx] * scale

# Decomposição assimétrica do choque:
# s_pos = max(Shock_t, 0) >= 0 (apertos não antecipados)
# s_neg = min(Shock_t, 0) <= 0 (cortes não antecipados)
s_pos = s_1pp.clip(lower=0.0)
s_neg = s_1pp.clip(upper=0.0)

# Variável de estado: Platô de Juros Persistentemente Altos (MM12m da Selic > mediana histórica)
selic_ma12 = df_var['selic'].rolling(12).mean()
threshold_med = selic_ma12.median()
high_state = (selic_ma12 > threshold_med).astype(float).shift(1)

n_pos_high = int(((s_1pp > 0) & (high_state == 1)).sum())
n_neg_high = int(((s_1pp < 0) & (high_state == 1)).sum())

controls = [df_var[c].shift(k).rename(f"{c}_lag{k}") for k in range(1, p + 1) for c in df_var.columns]
df_controls = pd.concat(controls, axis=1)

# Armazenar resultados horizonte a horizonte
results = {
    'b_high': [], 'se_high': [], 'p_high': [],
    'b_mod': [], 'se_mod': [], 'p_mod': [],
    'p_diff_reg': [],
    'gamma': [], 'se_gamma': [], 'p_gamma': [],
    'b_pos_high': [], 'se_pos_high': [], 'p_pos_high': [],
    'b_neg_high': [], 'se_neg_high': [], 'p_neg_high': [],
    'p_sym_high': []
}

for h in range(HORIZONS + 1):
    cum_inf = df_var['ipca_livres'].rolling(h + 1).sum().shift(-h)

    # (A) Modelo Dependente de Estado Simétrico Dentro do Regime
    reg_sym = pd.concat([
        cum_inf.rename('y'),
        (s_1pp * high_state).rename('sh_high'),
        (s_1pp * (1.0 - high_state)).rename('sh_mod'),
        high_state.rename('gamma')
    ] + [df_controls], axis=1).dropna()

    X_sym = sm.add_constant(reg_sym.drop(columns=['y']))
    ols_sym = sm.OLS(reg_sym['y'], X_sym).fit(cov_type='HAC', cov_kwds={'maxlags': max(1, h + 1)})
    wald_reg = ols_sym.wald_test('sh_high = sh_mod', scalar=True)

    results['b_high'].append(ols_sym.params['sh_high'])
    results['se_high'].append(ols_sym.bse['sh_high'])
    results['p_high'].append(ols_sym.pvalues['sh_high'])
    results['b_mod'].append(ols_sym.params['sh_mod'])
    results['se_mod'].append(ols_sym.bse['sh_mod'])
    results['p_mod'].append(ols_sym.pvalues['sh_mod'])
    results['p_diff_reg'].append(float(wald_reg.pvalue))
    results['gamma'].append(ols_sym.params['gamma'])
    results['se_gamma'].append(ols_sym.bse['gamma'])
    results['p_gamma'].append(ols_sym.pvalues['gamma'])

    # (B) Modelo Dependente de Estado Assimétrico no Platô Alto (Tenreyro & Thwaites, 2016)
    reg_asym = pd.concat([
        cum_inf.rename('y'),
        (s_pos * high_state).rename('sh_high_pos'),
        (s_neg * high_state).rename('sh_high_neg'),
        (s_1pp * (1.0 - high_state)).rename('sh_mod'),
        high_state.rename('gamma')
    ] + [df_controls], axis=1).dropna()

    X_asym = sm.add_constant(reg_asym.drop(columns=['y']))
    ols_asym = sm.OLS(reg_asym['y'], X_asym).fit(cov_type='HAC', cov_kwds={'maxlags': max(1, h + 1)})
    wald_sym = ols_asym.wald_test('sh_high_pos = sh_high_neg', scalar=True)

    results['b_pos_high'].append(ols_asym.params['sh_high_pos'])
    results['se_pos_high'].append(ols_asym.bse['sh_high_pos'])
    results['p_pos_high'].append(ols_asym.pvalues['sh_high_pos'])
    results['b_neg_high'].append(ols_asym.params['sh_high_neg'])
    results['se_neg_high'].append(ols_asym.bse['sh_high_neg'])
    results['p_neg_high'].append(ols_asym.pvalues['sh_high_neg'])
    results['p_sym_high'].append(float(wald_sym.pvalue))

# 2. Gerar Figura 5: Dois Painéis Independentes (Sem Espelhamento Mecânico!)
fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.6))
h_axis = np.arange(HORIZONS + 1)

b_high = np.array(results['b_high'])
se_high = np.array(results['se_high'])
b_mod = np.array(results['b_mod'])
se_mod = np.array(results['se_mod'])

# Painel (a): Platô de Juros Altos vs Regime Moderado (Choque de +1,00 p.p. na Selic)
axes[0].axhline(0, color='black', lw=1.0, ls='--')
axes[0].plot(h_axis, b_high, color='#b2182b', lw=2.3, marker='o', markersize=3.8,
             label=f'Platô de Juros Altos (MM12m > {threshold_med:.2f}% a.a.)')
axes[0].fill_between(h_axis, b_high - 1.645 * se_high, b_high + 1.645 * se_high, color='#b2182b', alpha=0.18, label='IC 90% HAC (Platô Alto)')
axes[0].plot(h_axis, b_mod, color='#2166ac', lw=2.3, ls='--', marker='s', markersize=3.8,
             label=f'Regime de Juros Moderados (≤ {threshold_med:.2f}% a.a.)')
axes[0].fill_between(h_axis, b_mod - 1.645 * se_mod, b_mod + 1.645 * se_mod, color='#2166ac', alpha=0.15, label='IC 90% HAC (Moderado)')
axes[0].set_title('(a) Resposta Acumulada do IPCA Livres (SGS 11428)\n[Choque de +1,00 p.p. na Selic por Regime de Juros]', fontweight='bold')
axes[0].set_xlabel('Horizonte Temporal (Meses)')
axes[0].set_ylabel('Inflação Acumulada de Itens Livres (p.p.)')
axes[0].set_xticks(range(0, HORIZONS + 1, 3))
axes[0].legend(loc='lower left', frameon=True, fontsize=8.5)

# Painel (b): Efeito de Nível do Platô Alto (gamma^h) e Estimativa Direta de Cortes (-beta^-_alto)
gamma_arr = np.array(results['gamma'])
se_gamma = np.array(results['se_gamma'])
# Efeito estimado diretamente de um corte de -1,00 p.p. no Platô Alto: E[Delta Pi | Shock^- = -1] = -1 * beta^-_alto
cut_effect_direct = -1.0 * np.array(results['b_neg_high'])
se_cut_direct = np.array(results['se_neg_high'])

axes[1].axhline(0, color='black', lw=1.0, ls='--')
axes[1].plot(h_axis, gamma_arr, color='#d95f02', lw=2.3, marker='^', markersize=4.0,
             label=r'Efeito de Nível do Platô Alto ($\hat{\gamma}^h$, $I_{t-1}=1$)')
axes[1].fill_between(h_axis, gamma_arr - 1.645 * se_gamma, gamma_arr + 1.645 * se_gamma, color='#d95f02', alpha=0.18, label=r'IC 90% HAC ($\hat{\gamma}^h$)')
axes[1].plot(h_axis, cut_effect_direct, color='#1b7837', lw=2.3, ls='-.', marker='d', markersize=4.0,
             label=f'Estimativa Direta de Corte de -1 p.p. (-β⁻_alto, N⁻={n_neg_high})')
axes[1].fill_between(h_axis, cut_effect_direct - 1.645 * se_cut_direct, cut_effect_direct + 1.645 * se_cut_direct,
                     color='#1b7837', alpha=0.15, label='IC 90% HAC (Corte Direto)')
axes[1].set_title('(b) Nível do Platô Alto (γ^h) e Estimativa Assimétrica de Corte\n[Sem Imposição de Simetria — Controle de Câmbio PTAX]', fontweight='bold')
axes[1].set_xlabel('Horizonte Temporal (Meses)')
axes[1].set_ylabel('Impacto Acumulado no IPCA Livres (p.p.)')
axes[1].set_xticks(range(0, HORIZONS + 1, 3))
axes[1].legend(loc='upper left', frameon=True, fontsize=8.5)

plt.tight_layout()
fig5_path = os.path.join(OUTPUT_DIR, "figura5_regime_juros_altos_lp.png")
plt.savefig(fig5_path, dpi=300)
plt.savefig(os.path.join(PROJECT_ROOT, "figura5_regime_juros_altos_lp.png"), dpi=300)
plt.close()
print(f"Salvo: {fig5_path}")


# 3. Rodar Bateria de Robustez (Focus 12m, IPCA Cheio, Juro Real Ex-Ante, Limiares 10% e 12%, COVID/Sazonal)
def run_robustness_spec(df_in, cols, inf_col, state_series, add_dummies=False):
    df_v = pd.DataFrame(index=df_in.index)
    for c in cols:
        if c == 'l_icbr':
            df_v[c] = np.log(df_in['ic_br'])
        elif c == 'l_ptax':
            df_v[c] = np.log(df_in['ptax'])
        elif c == 'l_ibc':
            df_v[c] = np.log(df_in['ibc_br'])
        else:
            df_v[c] = df_in[c]
    res_v = VAR(df_v).fit(6)
    P_v = np.linalg.cholesky(res_v.sigma_u)
    s_idx = list(df_v.columns).index('selic')
    sc = P_v[s_idx, s_idx]
    sh_std = (np.linalg.inv(P_v) @ res_v.resid.T).T
    sh_std.index = res_v.resid.index
    sh_1pp = sh_std.iloc[:, s_idx] * sc

    ctrls = [df_v[c].shift(k).rename(f"{c}_l{k}") for k in range(1, 7) for c in df_v.columns]
    if add_dummies:
        covid = ((df_v.index >= '2020-03-01') & (df_v.index <= '2021-06-01')).astype(float)
        ctrls.append(pd.Series(covid, index=df_v.index, name='d_covid'))
        for m in range(2, 13):
            ctrls.append(pd.Series((df_v.index.month == m).astype(float), index=df_v.index, name=f'm_{m}'))
    df_c = pd.concat(ctrls, axis=1)

    out = {}
    for h in [3, 6, 9, 12, 24]:
        cum_y = df_v[inf_col].rolling(h + 1).sum().shift(-h)
        reg = pd.concat([
            cum_y.rename('y'),
            (sh_1pp * state_series).rename('sh_high'),
            (sh_1pp * (1.0 - state_series)).rename('sh_mod'),
            state_series.rename('gamma'),
            df_c
        ], axis=1).dropna()
        ols = sm.OLS(reg['y'], sm.add_constant(reg.drop(columns=['y']))).fit(cov_type='HAC', cov_kwds={'maxlags': max(1, h + 1)})
        out[h] = (
            ols.params['sh_high'], ols.pvalues['sh_high'],
            ols.params['sh_mod'], ols.pvalues['sh_mod'],
            ols.params['gamma'], ols.pvalues['gamma']
        )
    return out


# Especificações de robustez
state_10 = (selic_ma12 > 10.0).astype(float).shift(1)
state_12 = (selic_ma12 > 12.0).astype(float).shift(1)
r_exante = (df_clean['selic'] - df_clean['exp_ipca_12m']).rolling(12).mean()
state_rexante = (r_exante > r_exante.median()).astype(float).shift(1)

rob_specs = {
    '1. Baseline 6-var (SGS 11428 + PTAX, Limiar Mediana 11,27%)': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida'], 'ipca_livres', high_state, False
    ),
    '2. Controle Expectativas Focus 12m (7-var, SGS 11428 + PTAX + Focus)': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'exp_ipca_12m', 'selic', 'juros_divida'], 'ipca_livres', high_state, False
    ),
    '3. IPCA Cheio (SGS 433 + PTAX + Expectativas Focus 12m)': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_cheio', 'exp_ipca_12m', 'selic', 'juros_divida'], 'ipca_cheio', high_state, False
    ),
    '4. Regime por Juro Real Ex-Ante (Selic - Focus 12m > Mediana 6,18%)': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'exp_ipca_12m', 'selic', 'juros_divida'], 'ipca_livres', state_rexante, False
    ),
    '5. Limiar Alternativo: Selic MM12m > 10,0% a.a.': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida'], 'ipca_livres', state_10, False
    ),
    '6. Limiar Alternativo: Selic MM12m > 12,0% a.a.': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida'], 'ipca_livres', state_12, False
    ),
    '7. Dummies Sazonais Mensais + Dummy Pandemia COVID-19 (2020-2021)': run_robustness_spec(
        df_clean, ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida'], 'ipca_livres', high_state, True
    ),
}

out_txt = os.path.join(PROJECT_ROOT, "resultados", "regime_juros_altos_lp.txt")
with open(out_txt, "w", encoding="utf-8") as f:
    f.write("=== PROJEÇÕES LOCAIS DEPENDENTES DE ESTADO E ASSIMÉTRICAS (REVISÃO PÓS-PARECER) ===\n")
    f.write(f"Série de Inflação: IPCA Itens Livres (SGS 11428) | Controle Cambial: Log PTAX (SGS 3696)\n")
    f.write(f"Limiar do Platô de Juros Altos (Mediana da MM12m da Selic): {threshold_med:.2f}% a.a.\n")
    f.write(f"Episódios de Choque no Platô Alto: N_alta (Shock > 0) = {n_pos_high} meses | N_corte (Shock < 0) = {n_neg_high} meses\n")
    f.write("Unidade do Choque: Normalizado para +1,00 p.p. de impacto na Selic em h = 0\n\n")

    f.write("--- TABELA PRINCIPAL (SIMÉTRICA E ASSIMÉTRICA POR REGIME) ---\n")
    f.write("Horiz | b_alto (p-val)   | b_mod (p-val)    | p(alto=mod) | gamma^h (p-val)  || Alta b+_alto (p) | Corte b-_alto (p) | p(b+=b-)\n")
    for h in [0, 3, 6, 9, 12, 18, 24]:
        f.write(
            f"h={h:2d}  | {results['b_high'][h]:+6.3f} ({results['p_high'][h]:.3f}) | "
            f"{results['b_mod'][h]:+6.3f} ({results['p_mod'][h]:.3f}) | "
            f"   {results['p_diff_reg'][h]:.3f}    | "
            f"{results['gamma'][h]:+6.3f} ({results['p_gamma'][h]:.3f}) || "
            f"{results['b_pos_high'][h]:+6.3f} ({results['p_pos_high'][h]:.3f})   | "
            f"{results['b_neg_high'][h]:+6.3f} ({results['p_neg_high'][h]:.3f})    |  {results['p_sym_high'][h]:.3f}\n"
        )

    f.write("\n--- BATERIA DE ROBUSTEZ (R2, R4, S2) ---\n")
    for spec_name, res_dict in rob_specs.items():
        f.write(f"\n[{spec_name}]\n")
        f.write("Horiz | b_alto (p-val)   | b_mod (p-val)    | gamma^h (p-val)\n")
        for h in [3, 6, 9, 12, 24]:
            bh, ph, bm, pm, gm, pg = res_dict[h]
            f.write(f"h={h:2d}  | {bh:+6.3f} ({ph:.3f}) | {bm:+6.3f} ({pm:.3f}) | {gm:+6.3f} ({pg:.3f})\n")

print(f"Resumo completo salvo em: {out_txt}")
