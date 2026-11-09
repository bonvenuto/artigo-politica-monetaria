"""Verificacoes adicionais (parte 2) do Revisor 1."""
import os, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.api import VAR
warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)
IDX = df.index
SEAS = pd.concat([pd.Series((IDX.month == m).astype(float), index=IDX, name=f"m_{m}") for m in range(2, 13)], axis=1)
v = pd.DataFrame(index=IDX)
v['l_icbr'] = np.log(df['ic_br']); v['l_ptax'] = np.log(df['ptax']); v['l_ibc'] = np.log(df['ibc_br'])
v['ipca_livres'] = df['ipca_livres']; v['selic'] = df['selic']; v['juros_divida'] = df['juros_divida']
si = 4
out = []
def P_(s=""): out.append(s); print(s)
def lags(vv, p):
    return pd.concat([vv[c].shift(k).rename(f"{c}_l{k}") for k in range(1, p + 1) for c in vv.columns], axis=1)
def shock_of(p, exog=None):
    r = VAR(v, exog=exog).fit(p); Pm = np.linalg.cholesky(r.sigma_u)
    e = (np.linalg.inv(Pm) @ r.resid.T).T; e.index = r.resid.index
    return e.iloc[:, si] * Pm[si, si], r
ma12 = v['selic'].rolling(12).mean(); state = (ma12 > ma12.median()).astype(float).shift(1)
cum = lambda y, h: y.rolling(h + 1).sum().shift(-h)
def regs(sh, st): return [(sh * st).rename('sh_high'), (sh * (1 - st)).rename('sh_mod'), st.rename('gamma')]
def fit(y, X, h):
    d = pd.concat([y.rename('y'), X], axis=1).dropna()
    return sm.OLS(d['y'], sm.add_constant(d.drop(columns='y'))).fit(cov_type='HAC', cov_kwds={'maxlags': h + 1}), d

# 1. Sensibilidade ao numero de defasagens (VAR e LP com o mesmo p)
P_("=== 1. Sensibilidade a p (VAR do choque e LP com mesmo p; LP estado com sazonais) ===")
for p in [2, 4, 6, 9, 12]:
    sh, _ = shock_of(p)
    C = pd.concat([lags(v, p), SEAS], axis=1)
    o24, _ = fit(cum(v['ipca_livres'], 24), pd.concat(regs(sh, state) + [C], axis=1), 24)
    o12, _ = fit(cum(v['ipca_livres'], 12), pd.concat(regs(sh, state) + [C], axis=1), 12)
    oj, _ = fit(v['juros_divida'].shift(-12), pd.concat([sh.rename('s'), lags(v, p)], axis=1), 12)
    P_(f"p={p:2d} | beta_mod24 {o24.params['sh_mod']:+.2f} (p={o24.pvalues['sh_mod']:.3f}) | beta_alto24 {o24.params['sh_high']:+.2f} (p={o24.pvalues['sh_high']:.3f}) | "
       f"gamma12 {o12.params['gamma']:+.2f} (p={o12.pvalues['gamma']:.3f}) | Wald12 p={float(o12.wald_test('sh_high = sh_mod', scalar=True).pvalue):.3f} | J_fam LP h12 {oj.params['s']:+.3f} (p={oj.pvalues['s']:.3f})")

# 2. VAR com sazonais: whiteness e IRFs
P_("\n=== 2. VAR(6) com dummies sazonais exogenas ===")
r0 = VAR(v).fit(6); rs = VAR(v, exog=SEAS.values).fit(6)
for nm, r in [('sem saz', r0), ('com saz', rs)]:
    w = r.test_whiteness(nlags=12); w24 = r.test_whiteness(nlags=24)
    P_(f"{nm}: Portmanteau(12) p={w.pvalue:.4f}; Portmanteau(24) p={w24.pvalue:.4f}")
# Ljung-Box da equacao de inflacao no lag 12
from statsmodels.stats.diagnostic import acorr_ljungbox
for nm, r in [('sem saz', r0), ('com saz', rs)]:
    lb = acorr_ljungbox(r.resid.iloc[:, 3], lags=[12], return_df=True)
    ac12 = r.resid.iloc[:, 3].autocorr(12)
    P_(f"{nm}: residuo eq. inflacao, autocorr lag12={ac12:+.3f}, LB(12) p={lb['lb_pvalue'].iloc[0]:.4f}")
Ps = np.linalg.cholesky(rs.sigma_u)
ir = rs.irf(24); oi = ir.orth_irfs / Ps[si, si]; se = ir.stderr(orth=True) / Ps[si, si]
for j, nm in [(3, 'inflacao'), (5, 'J_fam')]:
    P_(f"{nm} SVAR c/ saz: " + " | ".join(f"h={h}: {oi[h, j, si]:+.3f} [{se[h, j, si]:.3f}]" for h in [3, 5, 6, 12, 18, 24]))
fe = rs.fevd(24).decomp
P_(f"FEVD c/ saz: Selic em J_fam h=12/18/24: {fe[5, 11, si]*100:.1f} / {fe[5, 17, si]*100:.1f} / {fe[5, 23, si]*100:.1f} | IBC em inflacao h=24: {fe[3, 23, 2]*100:.2f}")

# 3. EWC (Lazarus, Lewis, Stock & Watson 2018) com valores criticos t_nu
P_("\n=== 3. Inferencia EWC (LLSW 2018), nu = 0.4 T^(2/3) ===")
def ewc_t(o, d, key):
    X = sm.add_constant(d.drop(columns='y')).values; cols = ['const'] + list(d.drop(columns='y').columns)
    j = cols.index(key)
    others = np.delete(X, j, axis=1)
    xt = X[:, j] - others @ np.linalg.lstsq(others, X[:, j], rcond=None)[0]
    u = o.resid.values; z = xt * u; T = len(z)
    nu = int(np.floor(0.4 * T ** (2 / 3)))
    tt = (np.arange(1, T + 1) - 0.5) / T
    lam = np.array([np.sqrt(2 / T) * np.sum(z * np.cos(np.pi * k * tt)) for k in range(1, nu + 1)])
    omega = np.mean(lam ** 2)
    se = np.sqrt(omega * T) / np.sum(xt ** 2)
    tstat = o.params[key] / se
    return tstat, 2 * stats.t.sf(abs(tstat), nu), nu
sh6, _ = shock_of(6)
C6 = pd.concat([lags(v, 6), SEAS], axis=1)
for h, key in [(9, 'gamma'), (12, 'gamma'), (18, 'gamma'), (24, 'sh_mod')]:
    o, d = fit(cum(v['ipca_livres'], h), pd.concat(regs(sh6, state) + [C6], axis=1), h)
    t, p, nu = ewc_t(o, d, key)
    P_(f"h={h:2d} {key:7s}: est {o.params[key]:+.3f} | NW(h+1) p={o.pvalues[key]:.3f} | EWC t={t:+.2f} p={p:.3f} (nu={nu})")
for h in [6, 12, 18]:
    o, d = fit(v['juros_divida'].shift(-h), pd.concat([sh6.rename('s'), lags(v, 6)], axis=1), h)
    t, p, nu = ewc_t(o, d, 's')
    P_(f"J_fam linear h={h:2d}: est {o.params['s']:+.3f} | NW p={o.pvalues['s']:.3f} | EWC t={t:+.2f} p={p:.4f}")

# 4. Block bootstrap com bloco 12 (sensibilidade)
P_("\n=== 4. Block bootstrap pares, bloco 12, B=499 (sensibilidade ao bloco) ===")
rng = np.random.default_rng(7)
for h, key in [(12, 'gamma'), (24, 'sh_mod')]:
    o, d = fit(cum(v['ipca_livres'], h), pd.concat(regs(sh6, state) + [C6], axis=1), h)
    Xm = sm.add_constant(d.drop(columns='y')); y = d['y'].values; T0 = len(d); L = 12; j = list(Xm.columns).index(key)
    bs = []
    for b in range(499):
        st = rng.integers(0, T0 - L, size=int(np.ceil(T0 / L)))
        ids = np.concatenate([np.arange(s, s + L) for s in st])[:T0]
        bs.append(np.linalg.lstsq(Xm.values[ids], y[ids], rcond=None)[0][j])
    sb = np.std(bs)
    P_(f"h={h} {key}: est {o.params[key]:+.3f} | se NW {o.bse[key]:.3f} | se boot(L=12) {sb:.3f} | t_boot {o.params[key]/sb:+.2f}")

# 5. Variacao da Selic nos meses com choque e distribuicao do choque em meses sem mudanca
P_("\n=== 5. Choque vs. variacao mensal da Selic ===")
ds = v['selic'].diff()
s = sh6.dropna(); ds = ds.loc[s.index]
P_(f"corr(choque, dSelic) = {np.corrcoef(s, ds)[0,1]:+.3f}; R2 regressao dSelic~choque = {np.corrcoef(s, ds)[0,1]**2:.3f}")
z = ds.abs() < 0.02
P_(f"meses com |dSelic|<0.02: {int(z.sum())} de {len(ds)}; dp do choque nesses meses {s[z].std():.3f} vs. demais {s[~z].std():.3f}")

open(os.path.join(ROOT, "r1_checks2_output.txt"), "w").write("\n".join(out))
