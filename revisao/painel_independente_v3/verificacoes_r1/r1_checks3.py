"""Verificacoes adicionais (parte 3) do Revisor 1."""
import os, warnings
import numpy as np, pandas as pd, statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.stats.diagnostic import acorr_ljungbox
warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)
IDX = df.index
SEAS = pd.concat([pd.Series((IDX.month == m).astype(float), index=IDX, name=f"m_{m}") for m in range(2, 13)], axis=1)
v = pd.DataFrame(index=IDX)
v['l_icbr'] = np.log(df['ic_br']); v['l_ptax'] = np.log(df['ptax']); v['l_ibc'] = np.log(df['ibc_br'])
v['ipca_livres'] = df['ipca_livres']; v['selic'] = df['selic']; v['juros_divida'] = df['juros_divida']
out=[]
def P_(s=""): out.append(s); print(s)
lags = lambda vv, a, b: pd.concat([vv[c].shift(k).rename(f"{c}_l{k}") for k in range(a, b + 1) for c in vv.columns], axis=1)
r = VAR(v).fit(6); Pm = np.linalg.cholesky(r.sigma_u)
e = (np.linalg.inv(Pm) @ r.resid.T).T; e.index = r.resid.index; sh = e.iloc[:, 4] * Pm[4, 4]
P_("=== Previsibilidade do choque ===")
lb = acorr_ljungbox(sh, lags=[6, 12, 24], return_df=True)
P_("Ljung-Box do choque: " + ", ".join(f"lag {i}: p={p:.3f}" for i, p in zip(lb.index, lb['lb_pvalue'])))
d = pd.concat([sh.rename('s'), lags(v, 7, 12), SEAS, df[['exp_ipca_12m']].shift(1).rename(columns={'exp_ipca_12m':'focus_l1'})], axis=1).dropna()
X = sm.add_constant(d.drop(columns='s'))
o = sm.OLS(d['s'], X).fit(cov_type='HAC', cov_kwds={'maxlags': 6})
for name, cols in [('lags 7-12 do sistema', [c for c in X.columns if '_l' in c]), ('dummies sazonais', list(SEAS.columns)), ('Focus t-1', ['focus_l1'])]:
    R = np.zeros((len(cols), len(X.columns)))
    for i, c in enumerate(cols): R[i, list(X.columns).index(c)] = 1
    P_(f"choque ~ {name}: Wald p={float(o.wald_test(R, scalar=True).pvalue):.4f}")
P_(f"R2 da regressao do choque em lags 7-12 + sazonais + Focus: {sm.OLS(d['s'], X).fit().rsquared:.3f}")

P_("\n=== LP estado totalmente interagida (controles x estado) ===")
ma12 = v['selic'].rolling(12).mean(); st = (ma12 > ma12.median()).astype(float).shift(1)
C = pd.concat([lags(v, 1, 6), SEAS], axis=1)
Ci = C.mul(st, axis=0).add_suffix('_hi')
cum = lambda y, h: y.rolling(h + 1).sum().shift(-h)
for h in [6, 12, 18, 24]:
    X = pd.concat([(sh*st).rename('sh_high'), (sh*(1-st)).rename('sh_mod'), st.rename('gamma'), C, Ci], axis=1)
    dd = pd.concat([cum(v['ipca_livres'], h).rename('y'), X], axis=1).dropna()
    o = sm.OLS(dd['y'], sm.add_constant(dd.drop(columns='y'))).fit(cov_type='HAC', cov_kwds={'maxlags': h+1})
    P_(f"h={h:2d} (k={dd.shape[1]}, N={len(dd)}) | alto {o.params['sh_high']:+.2f} (p={o.pvalues['sh_high']:.3f}) | mod {o.params['sh_mod']:+.2f} (p={o.pvalues['sh_mod']:.3f}) | Wald p={float(o.wald_test('sh_high = sh_mod', scalar=True).pvalue):.3f}")
open(os.path.join(ROOT, "r1_checks3_output.txt"), "w").write("\n".join(out))
