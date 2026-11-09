import os, warnings
import numpy as np, pandas as pd, statsmodels.api as sm
from statsmodels.tsa.api import VAR
warnings.filterwarnings("ignore")
ROOT = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)
v = pd.DataFrame(index=df.index)
v['l_icbr'] = np.log(df['ic_br']); v['l_ptax'] = np.log(df['ptax']); v['l_ibc'] = np.log(df['ibc_br'])
v['ipca_livres'] = df['ipca_livres']; v['selic'] = df['selic']; v['juros_divida'] = df['juros_divida']
lags = lambda vv, a, b: pd.concat([vv[c].shift(k).rename(f"{c}_l{k}") for k in range(a, b + 1) for c in vv.columns], axis=1)
r = VAR(v).fit(6); Pm = np.linalg.cholesky(r.sigma_u)
e = (np.linalg.inv(Pm) @ r.resid.T).T; e.index = r.resid.index; sh = e.iloc[:, 4] * Pm[4, 4]
d = pd.concat([sh.rename('s'), lags(v, 7, 12)], axis=1).dropna()
o = sm.OLS(d['s'], sm.add_constant(d.drop(columns='s'))).fit()
print(f"F classico choque ~ lags 7-12 (36 restr.): F={o.fvalue:.2f}, p={o.f_pvalue:.4f}, R2={o.rsquared:.3f}, N={len(d)}")
# selic lags 7-12 only
d2 = pd.concat([sh.rename('s'), lags(v[['selic','ipca_livres']], 7, 12)], axis=1).dropna()
o2 = sm.OLS(d2['s'], sm.add_constant(d2.drop(columns='s'))).fit()
print(f"F classico choque ~ lags 7-12 de Selic e inflacao (12 restr.): F={o2.fvalue:.2f}, p={o2.f_pvalue:.4f}")
