"""
SVAR recursivo (resposta ao painel independente).

Especificação-base:
- IC-Br em dólares (SGS 29042) no lugar da SGS 27574, que é a versão em reais (REV-29);
- 11 dummies sazonais exógenas na especificação-base do VAR (REV-16);
- intervalos de 95% por bootstrap com correção de viés (Kilian, 1998) ao lado dos erros-padrão assintóticos (REV-19);
- testes de autocorrelação residual (Portmanteau) com e sem dummies;
- comparação com as especificações anteriores (sem dummies; IC-Br em R$).

Pré-requisito: data/base_macro_bcb.csv e data/base_complementar_bcb.csv (scripts/coleta_series_complementares.py).
Autor: Ângelo Augusto Bonvenuto
"""

import os

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.var_model import ma_rep

from comum import (DF, FIG_DIR, HORIZONS, P_LAGS, PROJECT_ROOT, RES_DIR, SEASONAL, build_system, fit_var)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10, 'axes.labelsize': 10.5,
                     'axes.titlesize': 11.2, 'legend.fontsize': 8.5})

rng = np.random.default_rng(20261109)
NAMES = ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida']
SI, II, JI, BI, PI = 4, 3, 5, 2, 1
H_TAB = [0, 3, 6, 9, 12, 18, 24]


def savefig(name):
    plt.savefig(os.path.join(FIG_DIR, name), dpi=300)
    plt.savefig(os.path.join(PROJECT_ROOT, name), dpi=300)
    plt.close()


# ---------------------------------------------------------------------------
# 1. Figura 1: séries históricas
# ---------------------------------------------------------------------------
d = DF
fig, axes = plt.subplots(3, 1, figsize=(10.5, 11), sharex=True)
axes[0].plot(d.index, d['selic'], label='Selic efetiva (% a.a.) [SGS 4189]', color='#003366', lw=2.0)
axes[0].plot(d.index, d['exp_ipca_12m'], label='Expectativa Focus IPCA 12m (% a.a.)', color='#2b83ba', lw=1.6, ls='-.')
t0 = axes[0].twinx()
t0.plot(d.index, d['ipca_livres'], label='IPCA livres (% a.m.) [SGS 11428]', color='#cc3300', lw=1.2, alpha=0.85)
t0.plot(d.index, d['ipca_adm'], label='IPCA monitorados (% a.m.) [SGS 4449]', color='#ff9900', lw=1.1, ls='--', alpha=0.75)
axes[0].set_ylabel('Selic / expectativa (% a.a.)')
t0.set_ylabel('Inflação mensal (% a.m.)')
axes[0].set_title('(a) Selic, expectativas Focus 12m e inflação de itens livres e monitorados', loc='left', fontweight='bold')
l1, b1 = axes[0].get_legend_handles_labels(); l2, b2 = t0.get_legend_handles_labels()
axes[0].legend(l1 + l2, b1 + b2, loc='upper right', frameon=True)

axes[1].plot(d.index, d['juros_divida'], label='Comprometimento c/ juros (% renda) [SGS 29033]', color='#1b7837', lw=2.1)
axes[1].plot(d.index, d['servico_divida'], label='Comprometimento c/ serviço total (% renda) [SGS 29034]', color='#7fbc41', lw=1.5, ls='--')
t1 = axes[1].twinx()
t1.plot(d.index, d['endividamento'], label='Endividamento (% renda 12m) [SGS 29037]', color='#762a83', lw=1.7, ls=':')
axes[1].set_ylabel('Comprometimento (% renda)')
t1.set_ylabel('Endividamento (% renda 12m)')
axes[1].set_title('(b) Comprometimento de renda com juros e serviço total; endividamento das famílias', loc='left', fontweight='bold')
l1, b1 = axes[1].get_legend_handles_labels(); l2, b2 = t1.get_legend_handles_labels()
axes[1].legend(l1 + l2, b1 + b2, loc='upper left', frameon=True)

axes[2].plot(d.index, d['ibc_br'], label='IBC-Br dessazonalizado [SGS 24364]', color='#222222', lw=1.8)
t2 = axes[2].twinx()
t2.plot(d.index, d['ic_br_usd'], label='IC-Br em US$ [SGS 29042]', color='#b2182b', lw=1.5, ls='--')
t2.plot(d.index, d['ptax'] * 40, label='PTAX R$/US$ (×40) [SGS 3696]', color='#542788', lw=1.3, ls=':')
axes[2].set_ylabel('IBC-Br (índice)')
t2.set_ylabel('IC-Br (US$) / PTAX (×40)')
axes[2].set_title('(c) Atividade (IBC-Br), câmbio (PTAX) e commodities (IC-Br em US$)', loc='left', fontweight='bold')
l1, b1 = axes[2].get_legend_handles_labels(); l2, b2 = t2.get_legend_handles_labels()
axes[2].legend(l1 + l2, b1 + b2, loc='upper left', frameon=True)
axes[2].xaxis.set_major_locator(mdates.YearLocator(2))
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.tight_layout()
savefig("figura1_series_historicas.png")

# ---------------------------------------------------------------------------
# 2. Sistema-base, ADF, seleção de defasagens e diagnósticos
# ---------------------------------------------------------------------------
v = build_system()
adf_lines = []
for c in v.columns:
    r = adfuller(v[c], autolag='AIC')
    adf_lines.append(f"ADF {c:14s}: estatística = {r[0]:+.3f}, p = {r[1]:.4f}, defasagens = {r[2]}")

sel = VAR(v, exog=SEASONAL.values).select_order(maxlags=12)
sel_lines = [f"Ordens selecionadas (com sazonais): {sel.selected_orders}"]
for p in [2, 5, 6]:
    sel_lines.append(f"p={p}: AIC={sel.ics['aic'][p]:.3f} BIC={sel.ics['bic'][p]:.3f} HQIC={sel.ics['hqic'][p]:.3f}")

res = fit_var(v)                      # base: com sazonais
res_ns = fit_var(v, seasonal=False)   # sem sazonais
diag = []
for nm, r in [('com sazonais (base)', res), ('sem sazonais', res_ns)]:
    w12, w24 = r.test_whiteness(nlags=12), r.test_whiteness(nlags=24)
    roots = np.max(np.abs(np.linalg.eigvals(np.vstack([np.hstack(list(r.coefs)),
                                                       np.eye(6 * (P_LAGS - 1), 6 * P_LAGS)]))))
    diag.append(f"VAR(6) {nm}: Portmanteau(12) p={w12.pvalue:.4f}; Portmanteau(24) p={w24.pvalue:.4f}; "
                f"maior módulo da companheira = {roots:.4f}; autocorr. lag 12 do resíduo da inflação = "
                f"{r.resid.iloc[:, II].autocorr(12):+.3f}")

# Teste F conjunto das 11 dummies sazonais (RR2-15; "p < 10^-11" do texto, §3.2)
ipl = v['ipca_livres']
dum = SEASONAL.loc[v.index]
Rm = np.hstack([np.zeros((11, 1)), np.eye(11)])
# (a) regressão da inflação de itens livres só sobre constante + 11 dummies (amostra completa, T = len(v))
oa = sm.OLS(ipl, sm.add_constant(dum)).fit()
fa = oa.f_test(Rm)
# (b) equação da inflação do VAR(6): constante + 11 dummies + 6 defasagens das 6 variáveis (amostra de estimação)
Zb = sm.add_constant(pd.concat([dum.iloc[P_LAGS:]] + [v.shift(k).add_suffix(f'_l{k}').iloc[P_LAGS:] for k in range(1, P_LAGS + 1)], axis=1))
ob = sm.OLS(ipl.iloc[P_LAGS:], Zb).fit()
Rb = np.zeros((11, Zb.shape[1])); Rb[:, 1:12] = np.eye(11)
fb = ob.f_test(Rb)
sazonal_lines = [
    f"(a) Regressão do IPCA livres (SGS 11428) apenas em constante + 11 dummies mensais (T = {int(oa.nobs)}): F(11, {int(oa.df_resid)}) = {float(fa.fvalue):.2f}, p = {float(fa.pvalue):.3e}",
    f"(b) Equação da inflação do VAR(6) (constante + 11 dummies + 6 defasagens das 6 variáveis; T = {int(ob.nobs)}): F(11, {int(ob.df_resid)}) = {float(fb.fvalue):.2f}, p = {float(fb.pvalue):.3e}",
]

P = np.linalg.cholesky(res.sigma_u)
scale = P[SI, SI]
irf = res.irf(HORIZONS)
oi = irf.orth_irfs / scale
se_asy = irf.stderr(orth=True) / scale
fevd = res.fevd(HORIZONS).decomp


# ---------------------------------------------------------------------------
# 3. Bootstrap com correção de viés (Kilian, 1998)
# ---------------------------------------------------------------------------
Y = v.values
T, K = Y.shape
D = np.column_stack([np.ones(T), SEASONAL.values])   # constante + 11 sazonais
ND = D.shape[1]


def ols_var(Yb):
    Z = np.column_stack([D[P_LAGS:]] + [Yb[P_LAGS - k:T - k] for k in range(1, P_LAGS + 1)])
    B, *_ = np.linalg.lstsq(Z, Yb[P_LAGS:], rcond=None)
    U = Yb[P_LAGS:] - Z @ B
    S = U.T @ U / (len(U) - Z.shape[1])
    A = np.stack([B[ND + k * K: ND + (k + 1) * K].T for k in range(P_LAGS)])  # (p, K, K)
    return B[:ND], A, S, U


def companion_max(A):
    C = np.vstack([np.hstack(list(A)), np.eye(K * (P_LAGS - 1), K * P_LAGS)])
    return np.max(np.abs(np.linalg.eigvals(C)))


def simulate(det, A, U):
    Uc = U - U.mean(0)
    ids = rng.integers(0, len(Uc), len(Uc))
    Yb = np.zeros_like(Y)
    Yb[:P_LAGS] = Y[:P_LAGS]
    for t in range(P_LAGS, T):
        Yb[t] = D[t] @ det + sum(A[k] @ Yb[t - k - 1] for k in range(P_LAGS)) + Uc[ids[t - P_LAGS]]
    return Yb


def correct(A, bias):
    """Correção de viés com ajuste para preservar a estacionariedade (Kilian, 1998)."""
    m0 = companion_max(A)
    delta = 1.0
    Ac = A - bias
    while companion_max(Ac) >= max(m0, 0.9999) and delta > 0:
        delta -= 0.01
        Ac = A - delta * bias
    return Ac


det0, A0, S0, U0 = ols_var(Y)
B1, B2 = 300, 600
A_draws = np.array([ols_var(simulate(det0, A0, U0))[1] for _ in range(B1)])
bias = A_draws.mean(0) - A0
Ac = correct(A0, bias)

irf_bt = []
for _ in range(B2):
    det_b, A_b, S_b, U_b = ols_var(simulate(det0, Ac, U0))
    A_bc = correct(A_b, bias)
    try:
        Pb = np.linalg.cholesky(S_b)
    except np.linalg.LinAlgError:
        continue
    Phi = ma_rep(A_bc, HORIZONS)
    irf_bt.append(np.einsum('hij,j->hi', Phi, Pb[:, SI]) / Pb[SI, SI])
irf_bt = np.array(irf_bt)  # (B, H+1, K)
lo, hi = np.percentile(irf_bt, 2.5, axis=0), np.percentile(irf_bt, 97.5, axis=0)
Phi_c = ma_rep(Ac, HORIZONS)
oi_bc = np.einsum('hij,j->hi', Phi_c, np.linalg.cholesky(S0)[:, SI]) / np.linalg.cholesky(S0)[SI, SI]


# ---------------------------------------------------------------------------
# 4. Figura 2 (IRFs) e Figura 3 (FEVD)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 8.8))
h_axis = np.arange(HORIZONS + 1)
for (j, ylab, title, color), ax in zip([
    (II, 'IPCA livres (% a.m.)', '(a) IPCA itens livres (SGS 11428)', '#cc0000'),
    (JI, 'Comprometimento c/ juros (% renda)', '(b) Comprometimento de renda com juros (SGS 29033)', '#1b7837'),
    (BI, 'ln IBC-Br', '(c) Atividade (ln IBC-Br)', '#003366'),
    (SI, 'Selic (% a.a.)', '(d) Trajetória da Selic', '#542788')], axes.flat):
    ax.axhline(0, color='black', lw=1.0, ls='--')
    ax.plot(h_axis, oi[:, j, SI], color=color, lw=2.3, label='IRF (+1 p.p. na Selic em h=0)')
    ax.fill_between(h_axis, oi[:, j, SI] - 1.96 * se_asy[:, j, SI], oi[:, j, SI] + 1.96 * se_asy[:, j, SI],
                    color=color, alpha=0.15, label='IC 95% assintótico')
    ax.plot(h_axis, lo[:, j], color=color, lw=1.0, ls=':', label='IC 95% bootstrap (Kilian)')
    ax.plot(h_axis, hi[:, j], color=color, lw=1.0, ls=':')
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('Horizonte (meses)')
    ax.set_ylabel(ylab)
    ax.set_xticks(range(0, HORIZONS + 1, 3))
    ax.legend(loc='best', frameon=True)
plt.tight_layout()
savefig("figura2_irf_svar.png")

fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.4))
colors = ['#2b83ba', '#8073ac', '#abdda4', '#fdae61', '#d7191c', '#1b7837']
labels = ['Commodities (IC-Br US$)', 'Câmbio (PTAX)', 'Atividade (IBC-Br)', 'Inflação (choques próprios)',
          'Selic', 'Comprometimento c/ juros']
hz = np.arange(1, HORIZONS + 1)
for ax, j, title in [(axes[0], JI, '(a) FEVD: comprometimento c/ juros (SGS 29033)'),
                     (axes[1], II, '(b) FEVD: inflação de itens livres (SGS 11428)')]:
    ax.stackplot(hz, fevd[j].T * 100, labels=labels, colors=colors, alpha=0.88)
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel('Horizonte (meses; h = 1 é o impacto)')
    ax.set_ylabel('Participação na variância (%)')
    ax.set_xlim(1, HORIZONS); ax.set_ylim(0, 100)
axes[1].legend(loc='upper right', frameon=True)
plt.tight_layout()
savefig("figura3_fevd_svar.png")


# ---------------------------------------------------------------------------
# 5. Especificações anteriores, para documentar o efeito das mudanças
# ---------------------------------------------------------------------------
def irf_of(vv, seasonal):
    r = fit_var(vv, seasonal=seasonal)
    Pm = np.linalg.cholesky(r.sigma_u)
    o = r.irf(HORIZONS)
    return o.orth_irfs / Pm[SI, SI], o.stderr(orth=True) / Pm[SI, SI], r.fevd(HORIZONS).decomp, Pm[SI, SI]


alt = {
    'Base: IC-Br US$ (29042) + sazonais': (oi, se_asy, fevd, scale),
    'IC-Br US$ (29042), sem sazonais': irf_of(v, False),
    'IC-Br R$ (27574) + sazonais': irf_of(build_system(icbr='brl'), True),
    'Especificação anterior: IC-Br R$ (27574), sem sazonais': irf_of(build_system(icbr='brl'), False),
}

# ---------------------------------------------------------------------------
# 6. Relatório
# ---------------------------------------------------------------------------
out = os.path.join(RES_DIR, "resultados_svar_summary.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("=== SVAR(6): IC-Br em US$ (SGS 29042) e 11 dummies sazonais exógenas ===\n")
    f.write(f"Amostra: {v.index[0]:%Y-%m} a {v.index[-1]:%Y-%m} (T = {len(v)}); estimação a partir de {res.resid.index[0]:%Y-%m}\n")
    f.write("Ordenamento: [ln ICBr(US$), ln PTAX, ln IBC, IPCA livres, Selic, J^fam (29033)]\n")
    f.write(f"P55 (impacto de 1 d.p. na Selic) = {scale:.4f} p.p.\n\n--- ADF ---\n")
    f.write("\n".join(adf_lines) + "\n\n--- Seleção de defasagens ---\n" + "\n".join(sel_lines) + "\n\n--- Diagnósticos ---\n")
    f.write("\n".join(diag) + "\n")
    f.write("\n--- Teste F conjunto das 11 dummies sazonais (hipótese nula: ausência de sazonalidade determinística no IPCA livres) ---\n")
    f.write("\n".join(sazonal_lines) + "\n")
    f.write(f"\nBootstrap Kilian: B1={B1} (viés), B2={len(irf_bt)} réplicas válidas; maior raiz original {companion_max(A0):.4f}, "
            f"corrigida {companion_max(Ac):.4f}\n")
    f.write("\n--- TABELA 2: IRFs (+1 p.p. Selic em h=0) | pontual [EP assintótico] {IC 95% bootstrap} <pontual corrigido de viés> ---\n")
    for j, nm in [(II, 'IPCA livres'), (JI, 'J^fam 29033'), (BI, 'ln IBC'), (PI, 'ln PTAX'), (SI, 'Selic'), (0, 'ln ICBr')]:
        f.write(f"[{nm}]\n")
        for h in H_TAB:
            f.write(f"  h={h:2d}: {oi[h, j, SI]:+.4f} [{se_asy[h, j, SI]:.4f}] {{{lo[h, j]:+.4f}; {hi[h, j]:+.4f}}} <{oi_bc[h, j]:+.4f}>\n")
    f.write("\nIRF da inflação h=0..8: " + " ".join(f"{x:+.3f}" for x in oi[:9, II, SI]) + "\n")
    f.write("\n--- FEVD (h = número de passos; h=1 é o impacto), % ---\n")
    for j, nm in [(II, 'IPCA livres'), (JI, 'J^fam')]:
        f.write(f"[{nm}] colunas: ICBr, PTAX, IBC, IPCA, Selic, J\n")
        for h in [1, 6, 12, 18, 24]:
            f.write(f"  h={h:2d}: " + " | ".join(f"{x:5.2f}" for x in fevd[j, h - 1] * 100) + "\n")
    f.write("\n--- COMPARAÇÃO ENTRE ESPECIFICAÇÕES (inflação, J^fam, FEVD) ---\n")
    for nm, (o, s, fe, sc) in alt.items():
        f.write(f"[{nm}] P55={sc:.4f}\n")
        f.write("  inflação: " + " | ".join(f"h={h}: {o[h, II, SI]:+.4f} [{s[h, II, SI]:.3f}]" for h in [3, 5, 6, 12, 18, 24]) + "\n")
        f.write("  J^fam:    " + " | ".join(f"h={h}: {o[h, JI, SI]:+.4f} [{s[h, JI, SI]:.3f}]" for h in [6, 9, 12, 18, 24]) + "\n")
        f.write(f"  FEVD inflação h=24: ICBr {fe[II, 23, 0]*100:.2f} PTAX {fe[II, 23, 1]*100:.2f} IBC {fe[II, 23, 2]*100:.2f} "
                f"Selic {fe[II, 23, SI]*100:.2f} | FEVD J h=12/18/24 Selic {fe[JI, 11, SI]*100:.2f}/{fe[JI, 17, SI]*100:.2f}/{fe[JI, 23, SI]*100:.2f}\n")
print(f"Salvo: {out}")
