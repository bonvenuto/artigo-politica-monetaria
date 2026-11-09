"""
Revisor 1 — rodada 2. Checagens independentes (rodar a partir de replica/, lê replica/pkg).

1. Bootstrap recursivo sob a nula linear (mesmo DGP do autor, resíduos iid e wild Rademacher) para a
   estatística de Wald da LP TOTALMENTE INTERAGIDA (h=12 e h=24) — o autor não submete essa especificação ao
   bootstrap. Também Wald base e |t| de gamma^12, para comparar com o autor.
2. Meta Selic (SGS 432): LP linear de inflação e de J^fam (REV-15 pede LPs lineares e H2, não só estado).
3. LP com defasagens aumentadas (Montiel Olea & Plagborg-Møller, 2021): p+1 defasagens, EP EHW (HC1).
4. Diagnósticos dos dados simulados no bootstrap do autor (explosividade / Selic fora de faixa).
"""
import os
import sys
import time

import numpy as np
import pandas as pd
import statsmodels.api as sm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'pkg', 'scripts'))
from comum import (DF, P_LAGS, SEASONAL, build_system, cum, ewc, identify_shock, lag_controls, ols_hac,  # noqa
                   plateau_state, state_regs)

B = int(os.environ.get('B', 299))
rng = np.random.default_rng(777)
out = []


def W(s=''):
    out.append(s)
    print(s, flush=True)


v = build_system()
shock, scale, res_var = identify_shock(v)
state, thr, ma12 = plateau_state(v['selic'])
pi = v['ipca_livres']


def stats_for(vv, sh, st):
    C = pd.concat([lag_controls(vv), SEASONAL], axis=1)
    Ci = C.mul(st, axis=0).add_suffix('_hi')
    r = {}
    for h in (12, 24):
        o, _ = ols_hac(cum(vv['ipca_livres'], h), pd.concat(state_regs(sh, st) + [C], axis=1), h)
        r[f'wb{h}'] = float(o.wald_test('sh_high = sh_mod', scalar=True).statistic)
        if h == 12:
            r['tg12'] = abs(o.params['gamma'] / o.bse['gamma'])
        oi, _ = ols_hac(cum(vv['ipca_livres'], h), pd.concat(state_regs(sh, st) + [C, Ci], axis=1), h)
        r[f'wi{h}'] = float(oi.wald_test('sh_high = sh_mod', scalar=True).statistic)
        r[f'bmi{h}'] = oi.params['sh_mod']
    return r


obs = stats_for(v, shock, state)
W('=== 1. BOOTSTRAP SOB A NULA LINEAR: ESPECIFICAÇÃO BASE E TOTALMENTE INTERAGIDA ===')
W('Observado: ' + ', '.join(f'{k}={x:.3f}' for k, x in obs.items()))

Y = v.values
T, K = Y.shape
D = np.column_stack([np.ones(T), SEASONAL.values])
ND = D.shape[1]
Bm = res_var.params.values
A = np.stack([Bm[ND + k * K: ND + (k + 1) * K].T for k in range(P_LAGS)])
det = Bm[:ND]
U = res_var.resid.values - res_var.resid.values.mean(0)
Uall = np.vstack([np.zeros((P_LAGS, K)), U])  # alinhado a t (primeiras p linhas sem resíduo)


def simulate(scheme):
    Yb = np.zeros_like(Y)
    Yb[:P_LAGS] = Y[:P_LAGS]
    if scheme == 'iid':
        e = U[rng.integers(0, len(U), T)]
    else:  # wild Rademacher, preserva a heterocedasticidade no tempo
        e = Uall * rng.choice([-1.0, 1.0], size=(T, 1))
    for t in range(P_LAGS, T):
        Yb[t] = D[t] @ det + sum(A[k] @ Yb[t - k - 1] for k in range(P_LAGS)) + e[t]
    return pd.DataFrame(Yb, index=v.index, columns=v.columns)


diag = []
for scheme in ('iid', 'wild'):
    t0 = time.time()
    bt = {k: [] for k in obs}
    for b in range(B):
        vb = simulate(scheme)
        sel = vb['selic']
        diag.append(dict(scheme=scheme, smin=sel.min(), smax=sel.max(), pmax=np.abs(vb['ipca_livres']).max()))
        shb, _, rb = identify_shock(vb)
        stb, _, _ = plateau_state(sel)
        for k, x in stats_for(vb, shb, stb).items():
            bt[k].append(x)
    bt = {k: np.array(x) for k, x in bt.items()}
    W(f'\n[{scheme}] B={B} ({time.time() - t0:.0f}s)')
    for k in ['tg12', 'wb12', 'wb24', 'wi12', 'wi24']:
        p = float(np.mean(np.abs(bt[k]) >= abs(obs[k])))
        W(f'  {k:5s}: obs {obs[k]:7.3f} | p boot {p:.3f} | q95 nula {np.quantile(np.abs(bt[k]), 0.95):6.2f} | '
          f'rejeição nominal 5% (chi2_1 > 3,84 ou |t|>1,96): {np.mean(bt[k] > (1.96 if k == "tg12" else 3.841)):.2f}')
dg = pd.DataFrame(diag)
W('\nDiagnóstico dos dados simulados (Selic mín./máx.):')
W(dg.groupby('scheme')[['smin', 'smax', 'pmax']].describe(percentiles=[.05, .5, .95]).T.to_string())
W(f"Fração de réplicas com Selic simulada < 0: " + str(dg.groupby('scheme').apply(lambda d: float((d.smin < 0).mean())).to_dict()))

# ---------------------------------------------------------------------------
W('\n=== 2. META SELIC (SGS 432): LP LINEAR DE INFLAÇÃO E J^fam ===')
v_m = build_system(policy='meta_selic')
sh_m, sc_m, _ = identify_shock(v_m)
Cm = pd.concat([lag_controls(v_m), SEASONAL], axis=1)
Cb = pd.concat([lag_controls(v), SEASONAL], axis=1)
W(f'P55 meta = {sc_m:.4f}; d.p. choque meta = {sh_m.std():.4f}; corr com base = {pd.concat([shock, sh_m], axis=1).dropna().corr().iloc[0,1]:.3f}')
for nm, sh, C, vv in [('base', shock, Cb, v), ('meta', sh_m, Cm, v_m)]:
    for h in (3, 6, 9, 12, 18, 24):
        oj, dj = ols_hac(vv['juros_divida'].shift(-h), pd.concat([sh.rename('s'), C], axis=1), h)
        oi, di = ols_hac(vv['ipca_livres'].shift(-h), pd.concat([sh.rename('s'), C], axis=1), h)
        oc, dc = ols_hac(cum(vv['ipca_livres'], h), pd.concat([sh.rename('s'), C], axis=1), h)
        W(f'  {nm} h={h:2d} | J^fam {oj.params["s"]:+.3f} (NW {oj.pvalues["s"]:.3f}; EWC {ewc(oj, dj, "s")[3]:.3f}) | '
          f'por 1 dp {oj.params["s"]*sh.std():+.3f} | infl. mensal {oi.params["s"]:+.3f} ({oi.pvalues["s"]:.3f}) | '
          f'infl. acum. {oc.params["s"]:+.3f} ({oc.pvalues["s"]:.3f})')

# ---------------------------------------------------------------------------
W('\n=== 3. LP COM DEFASAGENS AUMENTADAS (p+1 = 7 defasagens nos controles; EP EHW/HC1) ===')
CA = pd.concat([lag_controls(v, P_LAGS + 1), SEASONAL], axis=1)
for h in (12, 24):
    d = pd.concat([cum(pi, h).rename('y')] + state_regs(shock, state) + [CA], axis=1).dropna()
    o = sm.OLS(d['y'], sm.add_constant(d.drop(columns='y'))).fit(cov_type='HC1')
    W(f'  h={h} | b_alto {o.params["sh_high"]:+.3f} ({o.pvalues["sh_high"]:.3f}) | b_mod {o.params["sh_mod"]:+.3f} '
      f'({o.pvalues["sh_mod"]:.3f}) | gamma {o.params["gamma"]:+.3f} ({o.pvalues["gamma"]:.3f}) | '
      f'Wald {float(o.wald_test("sh_high = sh_mod", scalar=True).pvalue):.3f}')
dj = pd.concat([v['juros_divida'].shift(-12).rename('y'), shock.rename('s'), CA], axis=1).dropna()
oj = sm.OLS(dj['y'], sm.add_constant(dj.drop(columns='y'))).fit(cov_type='HC1')
W(f'  J^fam h=12 | {oj.params["s"]:+.3f} ({oj.pvalues["s"]:.3f})')

with open(os.path.join(HERE, 'r1b_checks_output.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
