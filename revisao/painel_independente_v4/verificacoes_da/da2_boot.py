"""DA rodada 2: bootstrap recursivo sob a nula linear (mesmo DGP de inferencia_regimes.py, seção D)
para (i) o Wald da LP totalmente interagida em h=24 e h=18; (ii) consistência de sinal de dif24 na grade."""
import numpy as np, pandas as pd
from comum import (SEASONAL, P_LAGS, build_system, cum, identify_shock, lag_controls, ols_hac, plateau_state, state_regs)
rng = np.random.default_rng(777)
v = build_system(); shock, _, res_var = identify_shock(v)
state, thr, ma12 = plateau_state(v['selic'])
CTRL = pd.concat([lag_controls(v), SEASONAL], axis=1)
GRID = np.arange(9.0, 14.01, 0.5); QGRID = [float((ma12.dropna() <= g).mean()) for g in GRID]

def lp(y, sh, st, C, h):
    return ols_hac(y, pd.concat(state_regs(sh, st) + [C], axis=1), h)[0]

def stats_for(vv, sh, st, C, m12, thr_grid):
    Ci = C.mul(st, axis=0).add_suffix('_hi')
    out = {}
    for h in (18, 24):
        o = lp(cum(vv['ipca_livres'], h), sh, st, pd.concat([C, Ci], axis=1), h)
        out[f'wint{h}'] = float(o.wald_test('sh_high = sh_mod', scalar=True).statistic)
    difs = []
    for g in thr_grid:
        s2 = (m12 > g).astype(float).shift(1)
        o = lp(cum(vv['ipca_livres'], 24), sh, s2, C, 24)
        difs.append(o.params['sh_high'] - o.params['sh_mod'])
    difs = np.array(difs)
    out['allpos24'] = float((difs > 0).all()); out['meandif24'] = difs.mean()
    return out

obs = stats_for(v, shock, state, CTRL, ma12, GRID)
print('observado:', obs)
Y = v.values; T, K = Y.shape
D = np.column_stack([np.ones(T), SEASONAL.values]); ND = D.shape[1]
Bm = res_var.params.values
A = np.stack([Bm[ND + k*K: ND + (k+1)*K].T for k in range(P_LAGS)]); det = Bm[:ND]
U = res_var.resid.values - res_var.resid.values.mean(0)
bt = {k: [] for k in obs}
for b in range(399):
    if b % 50 == 0: print("rep", b, flush=True)
    ids = rng.integers(0, len(U), T); Yb = np.zeros_like(Y); Yb[:P_LAGS] = Y[:P_LAGS]
    for t in range(P_LAGS, T):
        Yb[t] = D[t] @ det + sum(A[k] @ Yb[t-k-1] for k in range(P_LAGS)) + U[ids[t]]
    vb = pd.DataFrame(Yb, index=v.index, columns=v.columns)
    try: shb, _, _ = identify_shock(vb)
    except np.linalg.LinAlgError: continue
    Cb = pd.concat([lag_controls(vb), SEASONAL], axis=1)
    stb, _, m12b = plateau_state(vb['selic'])
    r = stats_for(vb, shb, stb, Cb, m12b, np.quantile(m12b.dropna(), QGRID))
    for k in r: bt[k].append(r[k])
bt = {k: np.array(x) for k, x in bt.items()}
print('B válidas =', len(bt['wint24']))
for k in ('wint18', 'wint24'):
    print(f"{k}: obs {obs[k]:.2f} | p boot {np.mean(bt[k] >= obs[k]):.3f} | q95 nula {np.quantile(bt[k], .95):.2f}")
print(f"todas as 11 dif24 > 0: obs {obs['allpos24']:.0f} | freq. sob a nula {bt['allpos24'].mean():.3f} (mesmo sinal, qualquer: ~{2*bt['allpos24'].mean():.3f} se simétrico)")
print(f"média de dif24 na grade: obs {obs['meandif24']:+.2f} | p boot (unilateral) {np.mean(bt['meandif24'] >= obs['meandif24']):.3f} | bilateral {np.mean(np.abs(bt['meandif24']) >= abs(obs['meandif24'])):.3f}")
