"""Verificacoes adicionais do Revisor 1 (metodologia). Nao faz parte do pacote do autor."""
import os, sys, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)
P_LAGS = 6
IDX = df.index
SEAS = pd.concat([pd.Series((IDX.month == m).astype(float), index=IDX, name=f"m_{m}") for m in range(2, 13)], axis=1)

def build(cols):
    v = pd.DataFrame(index=IDX)
    for c in cols:
        if c == 'l_icbr': v[c] = np.log(df['ic_br'])
        elif c == 'l_ptax': v[c] = np.log(df['ptax'])
        elif c == 'l_ibc': v[c] = np.log(df['ibc_br'])
        else: v[c] = df[c]
    return v

BASE = ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida']
v = build(BASE)
res = VAR(v).fit(P_LAGS)
P = np.linalg.cholesky(res.sigma_u); si = 4; scale = P[si, si]
e = (np.linalg.inv(P) @ res.resid.T).T; e.index = res.resid.index
shock = e.iloc[:, si] * scale
ma12 = v['selic'].rolling(12).mean(); thr = ma12.median()
state = (ma12 > thr).astype(float).shift(1)

def lags(vv, p=P_LAGS):
    return pd.concat([vv[c].shift(k).rename(f"{c}_l{k}") for k in range(1, p + 1) for c in vv.columns], axis=1)
CTRL = pd.concat([lags(v), SEAS], axis=1)

def ols(y, X, h, maxlags=None):
    d = pd.concat([y.rename('y'), X], axis=1).dropna()
    m = sm.OLS(d['y'], sm.add_constant(d.drop(columns=['y'])))
    ml = max(1, h + 1) if maxlags is None else maxlags
    return m.fit(cov_type='HAC', cov_kwds={'maxlags': ml}), d

def cum(y, h): return y.rolling(h + 1).sum().shift(-h)

def regs(sh, st):
    return [(sh * st).rename('sh_high'), (sh * (1 - st)).rename('sh_mod'), st.rename('gamma')]

out = []
def P_(s=""): out.append(s); print(s)

# --- A. Verificacoes de numeros citados no texto ---
P_("=== A. Numeros citados no texto ===")
sel = VAR(v).select_order(maxlags=12)
P_(f"select_order: {sel.selected_orders}")
ics = sel.ics
for p in [2, 5, 6]:
    P_(f"p={p}: AIC={ics['aic'][p]:.3f} BIC={ics['bic'][p]:.3f} HQIC={ics['hqic'][p]:.3f}")
irf = res.irf(24); oi = irf.orth_irfs / scale
P_("SVAR inflacao h=0..8: " + " ".join(f"{x:+.3f}" for x in oi[:9, 3, si]))
v7 = build(['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'exp_ipca_12m', 'selic', 'juros_divida'])
r7 = VAR(v7).fit(P_LAGS); P7 = np.linalg.cholesky(r7.sigma_u)
oi7 = r7.irf(24).orth_irfs / P7[5, 5]
P_("SVAR 7 var inflacao h=0..8: " + " ".join(f"{x:+.4f}" for x in oi7[:9, 3, 5]))
# F test sazonal
d = pd.concat([v['ipca_livres'].rename('y'), SEAS], axis=1).dropna()
f0 = sm.OLS(d['y'], sm.add_constant(d.drop(columns='y'))).fit()
P_(f"F sazonal (sem controles): F={f0.fvalue:.2f}, p={f0.f_pvalue:.2e}")
# VAR residual whiteness / normality
try:
    wt = res.test_whiteness(nlags=12)
    P_(f"Portmanteau (12 lags) VAR(6): stat={wt.test_statistic:.1f}, p={wt.pvalue:.4f}")
    wt2 = VAR(v).fit(2).test_whiteness(nlags=12)
    P_(f"Portmanteau (12 lags) VAR(2): stat={wt2.test_statistic:.1f}, p={wt2.pvalue:.4f}")
except Exception as ex:
    P_(f"whiteness err {ex}")
P_(f"VAR(6) estavel: {res.is_stable()} | max |raiz| companion = {np.max(np.abs(np.linalg.eigvals(res.companion_matrix if hasattr(res,'companion_matrix') else np.eye(2)))) if hasattr(res,'companion_matrix') else 'n/a'}")
roots = res.roots; P_(f"menor |raiz| do polinomio inverso (proximo de 1 = raiz unitaria): {np.min(np.abs(roots)):.4f}")

# --- B. Episodios de regime ---
P_("\n=== B. Episodios do platô ===")
st = state.dropna()
spells = []; cur = None
for t, x in st.items():
    if x == 1 and cur is None: cur = t
    if x == 0 and cur is not None: spells.append((cur, prev)); cur = None
    prev = t
if cur is not None: spells.append((cur, prev))
for a, b in spells:
    P_(f"  platô: {a:%Y-%m} a {b:%Y-%m} ({(b.year-a.year)*12 + b.month-a.month+1} meses)")
P_(f"  n meses no platô = {int(st.sum())}; n spells = {len(spells)}")
for h in [12, 24]:
    y = cum(v['ipca_livres'], h)
    _, dd = ols(y, pd.concat(regs(shock, state) + [CTRL], axis=1), h)
    P_(f"  h={h}: N={len(dd)}, N platô={int(dd['gamma'].sum())}, ultimo t={dd.index[-1]:%Y-%m}")

# --- C. Primeiro estagio por regime: resposta da Selic ---
P_("\n=== C. Resposta da Selic (nivel) por regime, LP estado-dependente com sazonais ===")
for h in [0, 3, 6, 9, 12, 18, 24]:
    o, _ = ols(v['selic'].shift(-h), pd.concat(regs(shock, state) + [CTRL], axis=1), h)
    P_(f"h={h:2d} Selic | alto {o.params['sh_high']:+.3f} ({o.bse['sh_high']:.3f}) | mod {o.params['sh_mod']:+.3f} ({o.bse['sh_mod']:.3f})")
P_("Soma acumulada da Selic (p.p.-mes) 0..h, por regime:")
for h in [12, 24]:
    o, _ = ols(cum(v['selic'], h), pd.concat(regs(shock, state) + [CTRL], axis=1), h)
    P_(f"h={h:2d} | alto {o.params['sh_high']:+.2f} | mod {o.params['sh_mod']:+.2f}")

# --- D. Placebo de impacto: variaveis ordenadas antes da Selic devem ter resposta 0 em h=0 em cada regime ---
P_("\n=== D. Placebo h=0 (variaveis ordenadas antes da Selic) ===")
for var, y in [('ipca_livres', v['ipca_livres']), ('l_ptax(x100)', 100 * v['l_ptax']), ('l_ibc(x100)', 100 * v['l_ibc']), ('l_icbr(x100)', 100 * v['l_icbr'])]:
    for lab, C in [('sem saz', lags(v)), ('com saz', CTRL)]:
        o, _ = ols(y, pd.concat(regs(shock, state) + [C], axis=1), 0)
        w = o.wald_test('sh_high = 0, sh_mod = 0', scalar=True)
        P_(f"{var:13s} {lab}: alto {o.params['sh_high']:+.3f} (p={o.pvalues['sh_high']:.3f}) mod {o.params['sh_mod']:+.3f} (p={o.pvalues['sh_mod']:.3f}) | Wald conj p={float(w.pvalue):.3f}")

# --- E. Poder / efeito minimo detectavel da diferenca entre regimes ---
P_("\n=== E. MDE (80% poder, bicaudal 5%) para beta_alto - beta_mod ===")
for h in [3, 6, 9, 12, 18, 24]:
    o, _ = ols(cum(v['ipca_livres'], h), pd.concat(regs(shock, state) + [CTRL], axis=1), h)
    c = o.cov_params(); se_d = np.sqrt(c.loc['sh_high', 'sh_high'] + c.loc['sh_mod', 'sh_mod'] - 2 * c.loc['sh_high', 'sh_mod'])
    diff = o.params['sh_high'] - o.params['sh_mod']
    sd = shock.std()
    P_(f"h={h:2d} diff={diff:+.3f} se={se_d:.3f} MDE80={2.8*se_d:.2f} p.p. por 1 p.p. (= {2.8*se_d*sd:.3f} p.p. por 1 DP) | IC95 diff [{diff-1.96*se_d:+.2f}, {diff+1.96*se_d:+.2f}]")

# --- F. Robustez de gamma: defasagens omitidas / persistencia ---
P_("\n=== F. gamma^h sob controles adicionais (base com sazonais) ===")
pi = v['ipca_livres']
pi_ma12_l = pi.rolling(12).sum().shift(1).rename('pi12_l1')
selic_ma12_l = ma12.shift(1).rename('selicma12_l1')
specs = {
    'base (6 lags)': CTRL,
    '12 lags': pd.concat([lags(v, 12), SEAS], axis=1),
    '+ inflacao 12m defasada': pd.concat([CTRL, pi_ma12_l], axis=1),
    '+ Selic MM12 linear defasada': pd.concat([CTRL, selic_ma12_l], axis=1),
    '+ ambos': pd.concat([CTRL, pi_ma12_l, selic_ma12_l], axis=1),
    '+ Focus 12m (6 lags)': pd.concat([CTRL, lags(df[['exp_ipca_12m']])], axis=1),
}
for name, C in specs.items():
    row = []
    for h in [6, 9, 12, 18]:
        o, _ = ols(cum(pi, h), pd.concat(regs(shock, state) + [C], axis=1), h)
        row.append(f"h={h}: {o.params['gamma']:+.2f} (p={o.pvalues['gamma']:.3f})")
    P_(f"{name:30s} | " + " | ".join(row))
# beta_mod^24 tambem
P_("beta_mod^24 sob esses controles:")
for name, C in specs.items():
    o, _ = ols(cum(pi, 24), pd.concat(regs(shock, state) + [C], axis=1), 24)
    P_(f"  {name:30s} beta_mod24 {o.params['sh_mod']:+.2f} (p={o.pvalues['sh_mod']:.3f}) | beta_alto24 {o.params['sh_high']:+.2f} (p={o.pvalues['sh_high']:.3f})")

# --- G. Inferencia alternativa: NW com banda maior; LP com lag-augmentation + EHW ---
P_("\n=== G. Inferencia alternativa para gamma^12, beta_mod^24, J^fam linear h=12/18 ===")
T = len(v.dropna())
bw = int(np.ceil(1.3 * np.sqrt(T)))
for lab, ml in [('NW h+1', None), (f'NW max(h+1,{bw})', 'big')]:
    o12, _ = ols(cum(pi, 12), pd.concat(regs(shock, state) + [CTRL], axis=1), 12, None if ml is None else max(13, bw))
    o24, _ = ols(cum(pi, 24), pd.concat(regs(shock, state) + [CTRL], axis=1), 24, None if ml is None else max(25, bw))
    P_(f"{lab:18s}: gamma12 p={o12.pvalues['gamma']:.3f} | beta_mod24 p={o24.pvalues['sh_mod']:.3f}")
# Equal-weighted cosine (EWC) / fixed-b: use NW with bandwidth = 0.5*T? approximate via larger maxlags + t_{nu} not implemented; report NW with maxlags=2h
for h, key in [(12, 'gamma'), (24, 'sh_mod')]:
    o, dd = ols(cum(pi, h), pd.concat(regs(shock, state) + [CTRL], axis=1), h, 2 * h)
    P_(f"NW maxlags=2h  h={h} {key}: p={o.pvalues[key]:.3f}")

# --- H. Moving block bootstrap (pares, choque fixo) com banda sup-t para gamma^h e beta_mod^h, h=0..24 ---
P_("\n=== H. Block bootstrap (pares, bloco=24, B=999) e sup-t ===")
rng = np.random.default_rng(12345)
H = list(range(25))
Xs, ys = {}, {}
for h in H:
    X = pd.concat(regs(shock, state) + [CTRL], axis=1)
    dd = pd.concat([cum(pi, h).rename('y'), X], axis=1)
    Xs[h] = dd
base_idx = Xs[0].dropna().index  # comum
est = {}
for h in H:
    dd = Xs[h].dropna()
    o = sm.OLS(dd['y'], sm.add_constant(dd.drop(columns='y'))).fit()
    est[h] = o.params
def boot_stats(B=999, L=24, keys=('gamma', 'sh_mod', 'sh_high')):
    T0 = len(Xs[0])
    draws = {k: np.full((B, len(H)), np.nan) for k in keys}
    pos = np.arange(T0)
    for b in range(B):
        starts = rng.integers(0, T0 - L, size=int(np.ceil(T0 / L)))
        ids = np.concatenate([np.arange(s, s + L) for s in starts])[:T0]
        for h in H:
            dd = Xs[h].iloc[ids].dropna()
            Xm = sm.add_constant(dd.drop(columns='y'), has_constant='add')
            beta, *_ = np.linalg.lstsq(Xm.values, dd['y'].values, rcond=None)
            bp = pd.Series(beta, index=Xm.columns)
            for k in keys: draws[k][b, H.index(h)] = bp[k]
    return draws
draws = boot_stats()
for k in ['gamma', 'sh_mod', 'sh_high']:
    pt = np.array([est[h][k] for h in H]); sd = np.nanstd(draws[k], axis=0)
    tmax = np.nanmax(np.abs((draws[k] - np.nanmean(draws[k], axis=0)) / sd), axis=1)
    csup = np.nanquantile(tmax, 0.95)
    sig_pt = [h for h in H if abs(pt[h] / sd[h]) > 1.96]
    sig_sup = [h for h in H if abs(pt[h] / sd[h]) > csup]
    P_(f"{k:8s}: c_sup-t={csup:.2f} | h signif. pontual (boot-se): {sig_pt} | h signif. sup-t: {sig_sup}")
    for h in [9, 12, 18, 24]:
        P_(f"     h={h}: est {pt[h]:+.3f} se_boot {sd[h]:.3f} t={pt[h]/sd[h]:+.2f}")

# --- I. LP com Selic como regressor e controles contemporaneos (Plagborg-Moller & Wolf) ---
P_("\n=== I. LP recursiva (Selic_t como regressor + controles contemporaneos das variaveis ordenadas antes) ===")
contemp = v[['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres']].add_suffix('_c0')
for var in ['juros_divida', 'ipca_livres']:
    for h in [0, 6, 12, 18, 24]:
        o1, _ = ols(v[var].shift(-h), pd.concat([shock.rename('shock'), lags(v)], axis=1), h)
        o2, _ = ols(v[var].shift(-h), pd.concat([v['selic'].rename('selic0'), contemp, lags(v)], axis=1), h)
        P_(f"{var:12s} h={h:2d} | choque gerado {o1.params['shock']:+.4f} (se {o1.bse['shock']:.4f}) | Selic+contemp {o2.params['selic0']:+.4f} (se {o2.bse['selic0']:.4f})")

# --- J. Bootstrap residual do SVAR (recursivo) para IRFs normalizadas ---
P_("\n=== J. SVAR: EP assintotico/P55 vs. bootstrap residual recursivo (B=499) ===")
Y = v.dropna().values; T_, K = Y.shape
coefs = res.coefs; c0 = res.intercept; U = res.resid.values
asy = irf.stderr(orth=True) / scale
bt = []
for b in range(499):
    ids = rng.integers(0, U.shape[0], U.shape[0]); Ub = U[ids] - U.mean(0)
    Yb = np.zeros_like(Y); Yb[:P_LAGS] = Y[:P_LAGS]
    for t in range(P_LAGS, T_):
        Yb[t] = c0 + sum(coefs[k] @ Yb[t - k - 1] for k in range(P_LAGS)) + Ub[t - P_LAGS]
    rb = VAR(pd.DataFrame(Yb, columns=v.columns)).fit(P_LAGS)
    try:
        Pb = np.linalg.cholesky(rb.sigma_u)
    except np.linalg.LinAlgError:
        continue
    bt.append(rb.irf(24).orth_irfs[:, :, si] / Pb[si, si])
bt = np.array(bt)
for j, nm in [(3, 'inflacao'), (5, 'J_fam')]:
    for h in [6, 12, 18, 24]:
        lo, hi = np.percentile(bt[:, h, j], [2.5, 97.5])
        P_(f"{nm:9s} h={h:2d}: pt {oi[h, j, si]:+.3f} | asy se {asy[h, j, si]:.3f} | boot se {bt[:, h, j].std():.3f} | boot mean {bt[:, h, j].mean():+.3f} | boot 95% [{lo:+.3f}, {hi:+.3f}]")

open(os.path.join(ROOT, "r1_checks_output.txt"), "w").write("\n".join(out))
