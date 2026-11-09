"""
Funções e definições comuns aos scripts de estimação.

Especificação-base (resposta ao painel independente, REV-16 e REV-29):
- vetor endógeno [ln IC-Br em US$ (SGS 29042), ln PTAX, ln IBC-Br, IPCA livres, Selic, J^fam (SGS 29033)];
- VAR(6) com 11 dummies sazonais exógenas;
- choque = inovação de Cholesky da equação da Selic, escalada para +1 p.p. de impacto;
- LPs com as 6 defasagens do sistema e as 11 dummies sazonais;
- família de Holm: h em {3, 6, 9, 12, 18, 24} (h = 0 é diagnóstico, nulo ou quase nulo por construção).

Autor: Ângelo Augusto Bonvenuto
"""

import os
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.tsa.api import VAR

warnings.filterwarnings("ignore")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(PROJECT_ROOT, "figuras")
RES_DIR = os.path.join(PROJECT_ROOT, "resultados")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(RES_DIR, exist_ok=True)

P_LAGS = 6
HORIZONS = 24
H_REPORT = [0, 3, 6, 9, 12, 18, 24]
H_FAMILY = [3, 6, 9, 12, 18, 24]
END = '2026-08-01'


def carregar_base():
    base = pd.read_csv(os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)
    comp = pd.read_csv(os.path.join(PROJECT_ROOT, "data", "base_complementar_bcb.csv"), index_col=0, parse_dates=True)
    df = base.join(comp, how='left').loc[:END]
    df = df.rename(columns={'ic_br': 'ic_br_brl'})
    return df


DF = carregar_base()
IDX = DF.index
SEASONAL = pd.concat(
    [pd.Series((IDX.month == m).astype(float), index=IDX, name=f'm_{m}') for m in range(2, 13)], axis=1
)
COVID = pd.Series(((IDX >= '2020-03-01') & (IDX <= '2021-06-01')).astype(float), index=IDX, name='d_covid')

BASE_COLS = ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'selic', 'juros_divida']
FOCUS_COLS = ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_livres', 'exp_ipca_12m', 'selic', 'juros_divida']
CHEIO_COLS = ['l_icbr', 'l_ptax', 'l_ibc', 'ipca_cheio', 'exp_ipca_12m', 'selic', 'juros_divida']


def build_system(cols=BASE_COLS, icbr='usd', policy='selic', df=None):
    """Monta o vetor endógeno. icbr: 'usd' (SGS 29042, base) ou 'brl' (SGS 27574).
    policy: 'selic' (SGS 4189, média do mês) ou 'meta_selic' (SGS 432, fim do mês); a coluna mantém o nome 'selic'."""
    df = DF if df is None else df
    v = pd.DataFrame(index=df.index)
    for c in cols:
        if c == 'l_icbr':
            v[c] = np.log(df['ic_br_usd'] if icbr == 'usd' else df['ic_br_brl'])
        elif c == 'l_ptax':
            v[c] = np.log(df['ptax'])
        elif c == 'l_ibc':
            v[c] = np.log(df['ibc_br'])
        elif c == 'selic':
            v[c] = df[policy]
        else:
            v[c] = df[c]
    return v


def fit_var(v, p=P_LAGS, seasonal=True):
    return VAR(v, exog=SEASONAL.loc[v.index].values if seasonal else None).fit(p)


def identify_shock(v, p=P_LAGS, seasonal=True):
    """Inovação de Cholesky da equação da Selic, escalada para +1 p.p. de impacto. Retorna (choque, P55, resultado do VAR)."""
    res = fit_var(v, p, seasonal)
    P = np.linalg.cholesky(res.sigma_u)
    si = list(v.columns).index('selic')
    e = (np.linalg.inv(P) @ res.resid.T).T
    e.index = res.resid.index
    return e.iloc[:, si] * P[si, si], P[si, si], res


def lag_controls(v, p=P_LAGS):
    return pd.concat([v[c].shift(k).rename(f"{c}_l{k}") for k in range(1, p + 1) for c in v.columns], axis=1)


def cum(y, h):
    """Soma de y de t a t+h."""
    return y.rolling(h + 1).sum().shift(-h)


def ols_hac(y, X, h, maxlags=None):
    d = pd.concat([y.rename('y'), X], axis=1).dropna()
    m = sm.OLS(d['y'], sm.add_constant(d.drop(columns=['y'])))
    ml = max(1, h + 1) if maxlags is None else maxlags
    return m.fit(cov_type='HAC', cov_kwds={'maxlags': ml}), d


def ewc(o, d, key=None, contrast=None):
    """Inferência EWC (Lazarus, Lewis, Stock e Watson, 2018), nu = floor(0,4 T^(2/3)), valores críticos t_nu.
    key: coeficiente; contrast: dict {coef: peso} para uma combinação linear. Retorna (estimativa, ep, t, p, nu)."""
    names = ['const'] + list(d.drop(columns='y').columns)
    X = sm.add_constant(d.drop(columns='y'), has_constant='add').values
    u = o.resid.values
    T = len(u)
    w = np.zeros(len(names))
    if contrast is None:
        contrast = {key: 1.0}
    for k, val in contrast.items():
        w[names.index(k)] = val
    XtX_inv = np.linalg.inv(X.T @ X)
    a = X @ XtX_inv @ w          # influência da combinação linear
    z = a * u
    nu = int(np.floor(0.4 * T ** (2 / 3)))
    tt = (np.arange(1, T + 1) - 0.5) / T
    lam = np.array([np.sqrt(2 / T) * np.sum(z * np.cos(np.pi * k * tt)) for k in range(1, nu + 1)])
    se = np.sqrt(np.mean(lam ** 2) * T)
    est = float(w @ o.params.values)
    t = est / se
    return est, se, t, 2 * stats.t.sf(abs(t), nu), nu


def holm(pvals):
    return multipletests(pvals, method='holm')[1]


def state_regs(shock, state):
    return [(shock * state).rename('sh_high'), (shock * (1.0 - state)).rename('sh_mod'), state.rename('gamma')]


def plateau_state(selic, threshold=None):
    ma12 = selic.rolling(12).mean()
    thr = ma12.median() if threshold is None else threshold
    return (ma12 > thr).astype(float).shift(1), thr, ma12


def spells(state):
    st = state.dropna()
    out, cur, prev = [], None, None
    for t, x in st.items():
        if x == 1 and cur is None:
            cur = t
        if x == 0 and cur is not None:
            out.append((cur, prev))
            cur = None
        prev = t
    if cur is not None:
        out.append((cur, prev))
    return out


def fmt(x, nd=3):
    return f"{x:+.{nd}f}"
