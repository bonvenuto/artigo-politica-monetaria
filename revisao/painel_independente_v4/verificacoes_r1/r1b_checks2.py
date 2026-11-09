"""Revisor 1 — rodada 2: checagens rápidas (F das sazonais, EWC independente, MDE/IC, Holm, N efetivo)."""
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'pkg', 'scripts'))
from comum import (SEASONAL, build_system, cum, ewc, holm, identify_shock, lag_controls, ols_hac,  # noqa
                   plateau_state, state_regs, fit_var)

out = []
W = lambda s='': (out.append(s), print(s))
v = build_system()
shock, scale, res = identify_shock(v)
state, thr, _ = plateau_state(v['selic'])
C = pd.concat([lag_controls(v), SEASONAL], axis=1)
pi = v['ipca_livres']

# 1. F das 11 dummies na equação de inflação do VAR(6)
d = pd.concat([pi.rename('y'), lag_controls(v), SEASONAL], axis=1).dropna()
o = sm.OLS(d['y'], sm.add_constant(d.drop(columns='y'))).fit()
ft = o.f_test(' , '.join(f'{c} = 0' for c in SEASONAL.columns))
W(f'1. F sazonais na eq. de inflação: F={float(ft.fvalue):.2f}, p={float(ft.pvalue):.2e}')

# 2. EWC independente (escores X_t u_t, Omega = (1/nu) sum Lambda_j Lambda_j')
for h in (12, 24):
    o, dd = ols_hac(cum(pi, h), pd.concat(state_regs(shock, state) + [C], axis=1), h)
    X = sm.add_constant(dd.drop(columns='y'), has_constant='add').values
    u = o.resid.values
    T = len(u)
    S = X * u[:, None]
    nu = int(np.floor(0.4 * T ** (2 / 3)))
    tt = (np.arange(1, T + 1) - 0.5) / T
    Lam = np.array([np.sqrt(2 / T) * (np.cos(np.pi * j * tt) @ S) for j in range(1, nu + 1)])
    Om = Lam.T @ Lam / nu
    Q = np.linalg.inv(X.T @ X / T)
    V = Q @ Om @ Q / T
    names = ['const'] + list(dd.drop(columns='y').columns)
    for k in ('sh_mod', 'gamma'):
        j = names.index(k)
        t = o.params[k] / np.sqrt(V[j, j])
        W(f'2. h={h} {k}: EWC independente t={t:+.3f} p={2*stats.t.sf(abs(t), nu):.3f} | função do autor p={ewc(o, dd, k)[3]:.3f}')
    w = np.zeros(len(names)); w[names.index('sh_high')] = 1; w[names.index('sh_mod')] = -1
    se = np.sqrt(w @ V @ w)
    dif = o.params['sh_high'] - o.params['sh_mod']
    cv = o.cov_params()
    senw = np.sqrt(cv.loc['sh_high', 'sh_high'] + cv.loc['sh_mod', 'sh_mod'] - 2 * cv.loc['sh_high', 'sh_mod'])
    W(f'   dif={dif:+.3f} EP NW={senw:.3f} MDE80 NW={2.802*senw:.2f} ({2.802*senw*shock.std():.3f}/DP) | EP EWC={se:.3f} '
      f'MDE80 EWC={(stats.t.ppf(.975, nu)+stats.t.ppf(.8, nu))*se:.2f}')

# 3. Holm de beta_mod (família h=3..24)
ps = []
for h in (3, 6, 9, 12, 18, 24):
    o, _ = ols_hac(cum(pi, h), pd.concat(state_regs(shock, state) + [C], axis=1), h)
    ps.append(o.pvalues['sh_mod'])
W(f'3. p NW beta_mod: {np.round(ps, 3)} -> Holm {np.round(holm(ps), 3)}')

# 4. Observações efetivas do platô em h=24 por episódio
o, dd = ols_hac(cum(pi, 24), pd.concat(state_regs(shock, state) + [C], axis=1), 24)
st = dd['gamma']
W('4. h=24: meses no platô por ano da amostra efetiva: ' + str(st.groupby(st.index.year).sum().loc[lambda s: s > 0].to_dict()))
# platô no limiar 14% (onde o sup-Wald h=24 é atingido)
st14, _, _ = plateau_state(v['selic'], 14.0)
o, dd = ols_hac(cum(pi, 24), pd.concat(state_regs(shock, st14) + [C], axis=1), 24)
W(f'   limiar 14%: meses no platô na amostra h=24 = {int(dd["gamma"].sum())}, anos: '
  + str(dd['gamma'].groupby(dd.index.year).sum().loc[lambda s: s > 0].to_dict()))
W(f'   limiar 14%: b_alto {o.params["sh_high"]:+.2f} b_mod {o.params["sh_mod"]:+.2f} Wald stat {float(o.wald_test("sh_high = sh_mod", scalar=True).statistic):.2f}')

# 5. Assimetria de J em h=0 (não reportada no texto)
Xa = pd.concat([shock.clip(lower=0).rename('s_pos'), shock.clip(upper=0).rename('s_neg'), C], axis=1)
o, _ = ols_hac(v['juros_divida'], Xa, 0)
W(f'5. J h=0: b+ {o.params["s_pos"]:+.3f} ({o.pvalues["s_pos"]:.3f}) b- {o.params["s_neg"]:+.3f} ({o.pvalues["s_neg"]:.3f}); '
  'ambos os sinais de surpresa elevam J no impacto => termo |choque|, não assimetria de transmissão')

with open(os.path.join(HERE, 'r1b_checks2_output.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
