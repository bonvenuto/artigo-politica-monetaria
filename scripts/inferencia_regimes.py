"""
Inferência sobre H1 (itens REV-02, 12, 13, 14, 15, 18 e 38 e RR2-17 a RR2-22 do painel independente).

A. Diferença beta_alto - beta_mod: IC 95% (Newey-West e EWC) e efeito mínimo detectável (MDE, poder de 80%).
B. LP totalmente interagida (controles x estado).
C. Sensibilidade ao número de defasagens p ∈ {2, 4, 6, 9, 12} (VAR do choque e LP com o mesmo p).
D. Bootstrap recursivo sob a hipótese nula de linearidade (resíduos iid e wild Rademacher): a cada réplica, gera
   dados do VAR linear estimado, reestima o VAR, o choque e o indicador de estado, e reestima as LPs (p-valores de
   gamma^12, das diferenças entre regimes, da LP totalmente interagida e do sup-Wald sobre a grade de limiares, com
   e sem trimming de 15%). Em paralelo (8 processos), com semente fixa por réplica.
E. Primeiro estágio: resposta da Selic por regime e inflação acumulada normalizada pela Selic acumulada.
F. Episódios de platô e número de observações por regime.
G. Grade de limiares (9% a 14%) para gamma^12 e para as diferenças em h=12 e h=24 (Figura 6).
H. Previsibilidade do choque: F clássico e Wald HAC.

Autor: Ângelo Augusto Bonvenuto
"""

import multiprocessing as mp
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.vector_ar.var_model import ma_rep

from comum import (DF, FIG_DIR, H_FAMILY, H_REPORT, P_LAGS, PROJECT_ROOT, RES_DIR, SEASONAL, build_system, cum,
                   ewc, fit_var, identify_shock, lag_controls, ols_hac, plateau_state, spells, state_regs)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10, 'axes.titlesize': 11})
rng = np.random.default_rng(2026)
SEED_BOOT = 2026
BOOT = 999
lines = []


def W(s=""):
    lines.append(s)
    print(s)


v = build_system()
shock, scale, res_var = identify_shock(v)
sd = float(shock.std())
state, thr, ma12 = plateau_state(v['selic'])
CTRL = pd.concat([lag_controls(v), SEASONAL], axis=1)
pi = v['ipca_livres']
Z80 = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)


def lp_state(y, sh, st, C, h):
    return ols_hac(y, pd.concat(state_regs(sh, st) + [C], axis=1), h)


# ---------------------------------------------------------------------------
# A. Diferença entre regimes, IC e MDE
# ---------------------------------------------------------------------------
W("=== A. DIFERENÇA beta_alto - beta_mod (inflação acumulada de itens livres; choque de +1 p.p.) ===")
W(f"MDE = (z_0,975 + z_0,80) x EP = {Z80:.2f} x EP (NW); MDE EWC = (t_0,975 + t_0,80; nu) x EP EWC. d.p. do choque = {sd:.4f}")
diffA = {}
for h in H_FAMILY:
    o, d = lp_state(cum(pi, h), shock, state, CTRL, h)
    c = o.cov_params()
    dif = o.params['sh_high'] - o.params['sh_mod']
    se = float(np.sqrt(c.loc['sh_high', 'sh_high'] + c.loc['sh_mod', 'sh_mod'] - 2 * c.loc['sh_high', 'sh_mod']))
    est, se_e, t_e, p_e, nu = ewc(o, d, contrast={'sh_high': 1.0, 'sh_mod': -1.0})
    tcrit = stats.t.ppf(0.975, nu)
    mde_e = (tcrit + stats.t.ppf(0.80, nu)) * se_e
    diffA[h] = dict(dif=dif, se=se, lo=dif - 1.96 * se, hi=dif + 1.96 * se, p=2 * stats.norm.sf(abs(dif / se)),
                    mde=Z80 * se, lo_e=dif - tcrit * se_e, hi_e=dif + tcrit * se_e, p_e=p_e, mde_e=mde_e)
    r = diffA[h]
    z1 = stats.norm.ppf(0.95); t1 = stats.t.ppf(0.95, nu)
    r.update(up_nw=dif + z1 * se, lo_nw=dif - z1 * se, up_e=dif + t1 * se_e, lo_e1=dif - t1 * se_e, se_e=se_e, nu=nu)
    W(f"h={h:2d} | dif {dif:+.3f} | EP NW {se:.3f} | IC95 NW [{r['lo']:+.2f}; {r['hi']:+.2f}] p={r['p']:.3f} | MDE80 {r['mde']:.2f} p.p. "
      f"({r['mde']*sd:.3f} por 1 d.p.) | IC95 EWC [{r['lo_e']:+.2f}; {r['hi_e']:+.2f}] p={p_e:.3f} | MDE80 EWC {mde_e:.2f}")
    W(f"      EP EWC {se_e:.3f} (nu={nu}) | MDE80 EWC {mde_e:.2f} p.p. = {mde_e*sd:.3f} por 1 d.p. | MDE80 NW {r['mde']*sd:.3f} por 1 d.p.")
    W(f"      Limites unilaterais de 95% da diferença (p.p. por 1 d.p. do choque): NW [{r['lo_nw']*sd:+.3f}; {r['up_nw']*sd:+.3f}] "
      f"| EWC [{r['lo_e1']*sd:+.3f}; {r['up_e']*sd:+.3f}]  (inferior: dif - 1,645 EP; superior: dif + 1,645 EP)")

# ---------------------------------------------------------------------------
# B. LP totalmente interagida
# ---------------------------------------------------------------------------
W("\n=== B. LP TOTALMENTE INTERAGIDA (todos os controles e sazonais interagidos com o estado) ===")
Ci = CTRL.mul(state, axis=0).add_suffix('_hi')
interB = {}
for h in H_FAMILY:
    o, d = lp_state(cum(pi, h), shock, state, pd.concat([CTRL, Ci], axis=1), h)
    pw = float(o.wald_test('sh_high = sh_mod', scalar=True).pvalue)
    pe = ewc(o, d, contrast={'sh_high': 1.0, 'sh_mod': -1.0})[3]
    interB[h] = dict(bh=o.params['sh_high'], ph=o.pvalues['sh_high'], bm=o.params['sh_mod'], pm=o.pvalues['sh_mod'],
                     pw=pw, pe=pe, N=len(d), k=d.shape[1])
    W(f"h={h:2d} (N={len(d)}, regressores={d.shape[1]}) | alto {o.params['sh_high']:+.3f} (p={o.pvalues['sh_high']:.3f}) | "
      f"mod {o.params['sh_mod']:+.3f} (p={o.pvalues['sh_mod']:.3f}) | Wald NW p={pw:.3f} | EWC p={pe:.3f}")

# ---------------------------------------------------------------------------
# C. Sensibilidade a p
# ---------------------------------------------------------------------------
W("\n=== C. SENSIBILIDADE AO NÚMERO DE DEFASAGENS (VAR do choque e LP com o mesmo p; com sazonais) ===")
sensC = {}
for p in [2, 4, 6, 9, 12]:
    shp, _, _ = identify_shock(v, p=p)
    Cp = pd.concat([lag_controls(v, p), SEASONAL], axis=1)
    o24, d24 = lp_state(cum(pi, 24), shp, state, Cp, 24)
    o12, d12 = lp_state(cum(pi, 12), shp, state, Cp, 12)
    oj, dj = ols_hac(v['juros_divida'].shift(-12), pd.concat([shp.rename('s'), Cp], axis=1), 12)
    r = dict(bm24=o24.params['sh_mod'], pm24=o24.pvalues['sh_mod'], pe_m24=ewc(o24, d24, 'sh_mod')[3],
             bh24=o24.params['sh_high'], ph24=o24.pvalues['sh_high'],
             w24=float(o24.wald_test('sh_high = sh_mod', scalar=True).pvalue),
             g12=o12.params['gamma'], pg12=o12.pvalues['gamma'], pe_g12=ewc(o12, d12, 'gamma')[3],
             w12=float(o12.wald_test('sh_high = sh_mod', scalar=True).pvalue),
             j12=oj.params['s'], pj12=oj.pvalues['s'], pe_j12=ewc(oj, dj, 's')[3])
    sensC[p] = r
    W(f"p={p:2d} | beta_mod24 {r['bm24']:+.2f} (NW {r['pm24']:.3f}; EWC {r['pe_m24']:.3f}) | beta_alto24 {r['bh24']:+.2f} ({r['ph24']:.3f}) | "
      f"Wald24 {r['w24']:.3f} | gamma12 {r['g12']:+.2f} (NW {r['pg12']:.3f}; EWC {r['pe_g12']:.3f}) | Wald12 {r['w12']:.3f} | "
      f"J^fam h12 {r['j12']:+.3f} (NW {r['pj12']:.3f}; EWC {r['pe_j12']:.3f})")

# ---------------------------------------------------------------------------
# G. Grade de limiares (observado)
# ---------------------------------------------------------------------------
GRID = np.arange(9.0, 14.01, 0.5)
QGRID = [float((ma12.dropna() <= g).mean()) for g in GRID]


def grid_stats(vv, sh, sel, C, thresholds, horizons=(12, 24), want_full=False):
    """Wald (NW) da diferença e t de gamma^12 para cada limiar."""
    m12 = sel.rolling(12).mean()
    res = []
    for g in thresholds:
        st = (m12 > g).astype(float).shift(1)
        row = {'thr': g}
        for h in horizons:
            o, _ = lp_state(cum(vv['ipca_livres'], h), sh, st, C, h)
            row[f'w{h}'] = float(o.wald_test('sh_high = sh_mod', scalar=True).statistic)
            row[f'pw{h}'] = float(o.wald_test('sh_high = sh_mod', scalar=True).pvalue)
            if want_full:
                cv = o.cov_params()
                row[f'dif{h}'] = o.params['sh_high'] - o.params['sh_mod']
                row[f'sedif{h}'] = float(np.sqrt(cv.loc['sh_high', 'sh_high'] + cv.loc['sh_mod', 'sh_mod'] - 2 * cv.loc['sh_high', 'sh_mod']))
            if h == 12:
                row['tg12'] = o.params['gamma'] / o.bse['gamma']
                row['g12'] = o.params['gamma']; row['seg12'] = o.bse['gamma']
            row['n_high'] = int(st.sum())
        res.append(row)
    return pd.DataFrame(res)


gridG = grid_stats(v, shock, v['selic'], CTRL, GRID, want_full=True)
supW12, supW24, supT = gridG['w12'].max(), gridG['w24'].max(), gridG['tg12'].abs().max()

# ---------------------------------------------------------------------------
# D. Bootstrap recursivo sob a nula de linearidade (iid e wild Rademacher)
# ---------------------------------------------------------------------------
Y = v.values
T, K = Y.shape
SI = list(v.columns).index('selic')
D = np.column_stack([np.ones(T), SEASONAL.values])
ND = D.shape[1]
Bmat = res_var.params.values           # (ND + K*p, K): const, 11 exógenas, defasagens
assert Bmat.shape[0] == ND + K * P_LAGS
A = np.stack([Bmat[ND + k * K: ND + (k + 1) * K].T for k in range(P_LAGS)])
det = Bmat[:ND]
U = res_var.resid.values - res_var.resid.values.mean(0)

# Trimming de 15%: limiares da grade cujo quantil da MM12 observada está em [0,15; 0,85]
QG = np.array(QGRID)
TRIM = (QG >= 0.15 - 1e-9) & (QG <= 0.85 + 1e-9)

# IRF verdadeira (do DGP linear) de J^fam em h=12 para +1 p.p. na Selic: calibra o teste C4 (LP de J^fam em h=12)
_Pm = np.linalg.cholesky(res_var.sigma_u)
_Phi = ma_rep(A, 12)
IRF_J12 = float((_Phi[12] @ _Pm[:, SI])[list(v.columns).index('juros_divida')] / _Pm[SI, SI])


def lp_j12(vv, sh, C):
    o, _ = ols_hac(vv['juros_divida'].shift(-12), pd.concat([sh.rename('s'), C], axis=1), 12)
    return o.params['s'], o.bse['s']


def interacted_wald(vv, sh, st, C, h):
    Ci_ = C.mul(st, axis=0).add_suffix('_hi')
    o, _ = lp_state(cum(vv['ipca_livres'], h), sh, st, pd.concat([C, Ci_], axis=1), h)
    return float(o.wald_test('sh_high = sh_mod', scalar=True).statistic)


def all_stats(vv, sh, st, C, m12_, thr_grid):
    """Estatísticas de teste (valores observados ou de uma réplica)."""
    a12, _ = lp_state(cum(vv['ipca_livres'], 12), sh, st, C, 12)
    a24, _ = lp_state(cum(vv['ipca_livres'], 24), sh, st, C, 24)
    g = grid_stats(vv, sh, vv['selic'], C, thr_grid, want_full=True)
    bj, sj = lp_j12(vv, sh, C)
    return dict(tg12=a12.params['gamma'] / a12.bse['gamma'],
                w12=float(a12.wald_test('sh_high = sh_mod', scalar=True).statistic),
                w24=float(a24.wald_test('sh_high = sh_mod', scalar=True).statistic),
                wint12=interacted_wald(vv, sh, st, C, 12), wint24=interacted_wald(vv, sh, st, C, 24),
                supW12=g['w12'].max(), supW24=g['w24'].max(), supT=g['tg12'].abs().max(),
                supW12_trim=g.loc[TRIM, 'w12'].max(), supW24_trim=g.loc[TRIM, 'w24'].max(),
                supT_trim=g.loc[TRIM, 'tg12'].abs().max(),
                dif12=a12.params['sh_high'] - a12.params['sh_mod'], dif24=a24.params['sh_high'] - a24.params['sh_mod'],
                allpos24=float((g['dif24'] > 0).all()), allpos12=float((g['dif12'] > 0).all()),
                nneg12=float((g['dif12'] < 0).sum()), npos24=float((g['dif24'] > 0).sum()),
                j12_b=bj, j12_se=sj, t_j12_c=(bj - IRF_J12) / sj, t_j12_0=bj / sj)


obs = all_stats(v, shock, state, CTRL, ma12, GRID)
obs['j12_irf_true'] = IRF_J12
KEYS_P = ['tg12', 'w12', 'w24', 'wint12', 'wint24', 'supT', 'supW12', 'supW24', 'supT_trim', 'supW12_trim', 'supW24_trim']


def replica(args):
    scheme, b = args
    rg = np.random.default_rng([SEED_BOOT, 0 if scheme == 'iid' else 1, b])
    Yb = np.zeros_like(Y)
    Yb[:P_LAGS] = Y[:P_LAGS]
    if scheme == 'iid':
        ids = rg.integers(0, len(U), T)
        shk = lambda t: U[ids[t]]
    else:
        eta = rg.choice([-1.0, 1.0], size=T)
        shk = lambda t: U[t - P_LAGS] * eta[t]
    for t in range(P_LAGS, T):
        Yb[t] = D[t] @ det + sum(A[k] @ Yb[t - k - 1] for k in range(P_LAGS)) + shk(t)
    neg = bool((Yb[:, SI] < 0).any())
    vb = pd.DataFrame(Yb, index=v.index, columns=v.columns)
    try:
        shb, _, _ = identify_shock(vb)
        Cb = pd.concat([lag_controls(vb), SEASONAL], axis=1)
        stb, _, m12b = plateau_state(vb['selic'])
        r = all_stats(vb, shb, stb, Cb, m12b, np.quantile(m12b.dropna(), QGRID))
    except (np.linalg.LinAlgError, ValueError, KeyError):
        return None
    r['selic_neg'] = float(neg)
    return r


os.environ.setdefault('OMP_NUM_THREADS', '1')
boot = {}
ctx = mp.get_context('fork')
for scheme in ['iid', 'wild']:
    with ctx.Pool(8) as pool:
        out_ = [r for r in pool.map(replica, [(scheme, b) for b in range(BOOT)], chunksize=4) if r is not None]
    boot[scheme] = {k: np.array([r[k] for r in out_]) for k in out_[0]}
bt = boot['iid']
pboot = {sc: {k: float(np.mean(np.abs(boot[sc][k]) >= abs(obs[k]))) for k in KEYS_P} for sc in boot}

# ---------------------------------------------------------------------------
# E. Primeiro estágio por regime e normalização
# ---------------------------------------------------------------------------
W("\n=== E. PRIMEIRO ESTÁGIO: SELIC POR REGIME (LP de estado com sazonais) ===")
stageE = {}
for h in H_REPORT:
    o, _ = lp_state(v['selic'].shift(-h), shock, state, CTRL, h)
    stageE[h] = dict(bh=o.params['sh_high'], seh=o.bse['sh_high'], bm=o.params['sh_mod'], sem=o.bse['sh_mod'],
                     pw=float(o.wald_test('sh_high = sh_mod', scalar=True).pvalue))
    W(f"h={h:2d} Selic | alto {o.params['sh_high']:+.3f} ({o.bse['sh_high']:.3f}) | mod {o.params['sh_mod']:+.3f} ({o.bse['sh_mod']:.3f}) | Wald p={stageE[h]['pw']:.3f}")
W("Razão inflação acumulada / Selic acumulada (p.p. de inflação por p.p.-mês de Selic), IC 95% bootstrap de blocos (bloco 24, B=999):")
ratioE = {}
for h in [12, 24]:
    di = pd.concat([cum(pi, h).rename('y')] + state_regs(shock, state) + [CTRL], axis=1)
    ds = pd.concat([cum(v['selic'], h).rename('y')] + state_regs(shock, state) + [CTRL], axis=1)
    rows = di.dropna().index.intersection(ds.dropna().index)
    di, ds = di.loc[rows], ds.loc[rows]
    Xi = sm.add_constant(di.drop(columns='y')).values
    cols = ['const'] + list(di.drop(columns='y').columns)
    jh, jm = cols.index('sh_high'), cols.index('sh_mod')

    def ratios(ix):
        bi = np.linalg.lstsq(Xi[ix], di['y'].values[ix], rcond=None)[0]
        bs = np.linalg.lstsq(Xi[ix], ds['y'].values[ix], rcond=None)[0]
        return bi[jh] / bs[jh], bi[jm] / bs[jm], bi[jh], bs[jh], bi[jm], bs[jm]

    full = ratios(np.arange(len(rows)))
    n, L = len(rows), 24
    draws = []
    for _ in range(999):
        st0 = rng.integers(0, n - L, size=int(np.ceil(n / L)))
        draws.append(ratios(np.concatenate([np.arange(s, s + L) for s in st0])[:n]))
    draws = np.array(draws)
    q = lambda j: np.percentile(draws[:, j], [2.5, 97.5])
    dq = np.percentile(draws[:, 0] - draws[:, 1], [2.5, 97.5])
    ratioE[h] = dict(r_h=full[0], r_m=full[1], ci_h=q(0), ci_m=q(1), pi_h=full[2], s_h=full[3], pi_m=full[4], s_m=full[5], ci_d=dq)
    W(f"h={h}: alto {full[2]:+.3f}/{full[3]:+.2f} = {full[0]:+.3f} [{q(0)[0]:+.3f}; {q(0)[1]:+.3f}] | "
      f"mod {full[4]:+.3f}/{full[5]:+.2f} = {full[1]:+.3f} [{q(1)[0]:+.3f}; {q(1)[1]:+.3f}] | dif. das razões IC95 [{dq[0]:+.3f}; {dq[1]:+.3f}]")
W("Placebo de impacto (h=0) das variáveis ordenadas antes da Selic, por regime:")
for nm, y in [('ipca_livres', pi), ('100 ln PTAX', 100 * v['l_ptax']), ('100 ln IBC', 100 * v['l_ibc']), ('100 ln ICBr', 100 * v['l_icbr'])]:
    o, _ = lp_state(y, shock, state, CTRL, 0)
    W(f"  {nm:12s}: alto {o.params['sh_high']:+.3f} (p={o.pvalues['sh_high']:.3f}) | mod {o.params['sh_mod']:+.3f} (p={o.pvalues['sh_mod']:.3f}) | "
      f"Wald conj. p={float(o.wald_test('sh_high = 0, sh_mod = 0', scalar=True).pvalue):.3f}")

# ---------------------------------------------------------------------------
# F. Episódios
# ---------------------------------------------------------------------------
W("\n=== F. EPISÓDIOS DE PLATÔ (I_{t-1} = 1) ===")
infl12 = (np.exp(np.log1p(DF['ipca_livres'] / 100).rolling(12).sum()) - 1) * 100
episodes = []
for a, b in spells(state):
    seg = v['selic'].loc[a:b]
    e = dict(ini=a, fim=b, meses=(b.year - a.year) * 12 + b.month - a.month + 1, selic_med=seg.mean(),
             selic_min=seg.min(), selic_max=seg.max(), inf_ini=infl12.loc[a], inf_fim=infl12.loc[b],
             inf_12_apos=infl12.shift(-12).loc[b] if b + pd.DateOffset(months=12) <= v.index[-1] else np.nan)
    episodes.append(e)
    W(f"{a:%Y-%m} a {b:%Y-%m} ({e['meses']} meses) | Selic média {e['selic_med']:.2f} (mín {e['selic_min']:.2f}, máx {e['selic_max']:.2f}) | "
      f"IPCA livres 12m: início {e['inf_ini']:.2f}, fim {e['inf_fim']:.2f}, 12 meses após o fim {e['inf_12_apos']:.2f}")
W("N por regime e horizonte (LP de estado da Tabela 4):")
for h in H_REPORT:
    o, d = lp_state(cum(pi, h), shock, state, CTRL, h)
    W(f"  h={h:2d}: N={len(d)}, platô={int(d['gamma'].sum())}, moderado={len(d) - int(d['gamma'].sum())}, última obs. {d.index[-1]:%Y-%m}")

# ---------------------------------------------------------------------------
# H. Previsibilidade do choque
# ---------------------------------------------------------------------------
W("\n=== H. PREVISIBILIDADE DO CHOQUE ===")
L712 = pd.concat([v[c].shift(k).rename(f"{c}_l{k}") for k in range(7, 13) for c in v.columns], axis=1)
d = pd.concat([shock.rename('s'), L712], axis=1).dropna()
oF = sm.OLS(d['s'], sm.add_constant(d.drop(columns='s'))).fit()
oH = sm.OLS(d['s'], sm.add_constant(d.drop(columns='s'))).fit(cov_type='HAC', cov_kwds={'maxlags': 6})
R = np.eye(len(oH.params))[1:]
W(f"choque ~ defasagens 7-12 do sistema ({R.shape[0]} restrições, N={len(d)}): F clássico = {oF.fvalue:.2f} (p={oF.f_pvalue:.3f}); "
  f"Wald HAC(6) p={float(oH.wald_test(R, scalar=True).pvalue):.4f}; R2 = {oF.rsquared:.3f}")
dF = pd.concat([shock.rename('s'), lag_controls(DF[['exp_ipca_12m']])], axis=1).dropna()
oFo = sm.OLS(dF['s'], sm.add_constant(dF.drop(columns='s'))).fit()
W(f"choque ~ 6 defasagens da expectativa Focus 12m: F = {oFo.fvalue:.2f} (p={oFo.f_pvalue:.3f})")
ds = v['selic'].diff().loc[shock.dropna().index]
W(f"corr(choque, ΔSelic mensal) = {np.corrcoef(shock.dropna(), ds)[0, 1]:+.3f}")

# ---------------------------------------------------------------------------
# Relatório do bootstrap e da grade
# ---------------------------------------------------------------------------
NM = {'tg12': '|t| de gamma^12 (limiar na mediana)', 'w12': 'Wald alto=mod, h=12 (base)', 'w24': 'Wald alto=mod, h=24 (base)',
      'wint12': 'Wald alto=mod, h=12, LP totalmente interagida', 'wint24': 'Wald alto=mod, h=24, LP totalmente interagida',
      'supT': 'sup |t| de gamma^12 na grade (11 limiares)', 'supW12': 'sup-Wald h=12 na grade (11 limiares)',
      'supW24': 'sup-Wald h=24 na grade (11 limiares)',
      'supT_trim': 'sup |t| de gamma^12, grade com trimming 15%', 'supW12_trim': 'sup-Wald h=12, grade com trimming 15%',
      'supW24_trim': 'sup-Wald h=24, grade com trimming 15%'}
W(f"\n=== D. BOOTSTRAP RECURSIVO SOB A NULA LINEAR (VAR, choque e estado reestimados; B={BOOT}, 8 processos, semente fixa por réplica) ===")
W(f"Trimming de 15%: limiares com quantil da MM12 em [0,15; 0,85] -> {', '.join(f'{g:.1f}' for g in GRID[TRIM])} (de {len(GRID)}). "
  f"Observado nos extremos: sup-Wald h=12 {obs['supW12']:.2f} (trim {obs['supW12_trim']:.2f}); h=24 {obs['supW24']:.2f} (trim {obs['supW24_trim']:.2f})")
for sc, nome in [('iid', 'REAMOSTRAGEM IID DOS RESÍDUOS'), ('wild', 'WILD BOOTSTRAP (Rademacher, resíduos multiplicados por ±1)')]:
    W(f"\n--- {nome} (réplicas válidas: {len(boot[sc]['tg12'])}) ---")
    for k in KEYS_P:
        W(f"{NM[k]:50s}: observado {obs[k]:+.3f} | p bootstrap = {pboot[sc][k]:.3f} | quantil 95% sob a nula = {np.quantile(np.abs(boot[sc][k]), 0.95):.2f}")
    W(f"Fração de réplicas com Selic simulada negativa em algum mês: {boot[sc]['selic_neg'].mean():.3f}")
    neg_m = boot[sc]['selic_neg'] == 0
    W("  Sensibilidade (descartando réplicas com Selic negativa; n=%d): " % neg_m.sum() + " | ".join(
        f"{k} p={float(np.mean(np.abs(boot[sc][k][neg_m]) >= abs(obs[k]))):.3f}" for k in ['tg12', 'w12', 'w24', 'wint12', 'wint24', 'supW12', 'supW24']))
W("\n--- PADRÃO DE SINAL DA DIFERENÇA ENTRE REGIMES SOB A NULA LINEAR (RR2-22) ---")
W(f"Observado: dif12 = {obs['dif12']:+.3f} (negativa); dif24 = {obs['dif24']:+.3f} (positiva); grade: dif12 < 0 em {int(obs['nneg12'])} de {len(GRID)} limiares, "
  f"dif24 > 0 em {int(obs['npos24'])} de {len(GRID)}")
for sc in boot:
    bb = boot[sc]
    W(f"[{sc}] P(dif24 > 0, limiar mediano) = {np.mean(bb['dif24'] > 0):.3f} | P(dif12 < 0) = {np.mean(bb['dif12'] < 0):.3f} | "
      f"P(dif12 < 0 e dif24 > 0) = {np.mean((bb['dif12'] < 0) & (bb['dif24'] > 0)):.3f} | "
      f"P(dif24 > 0 nos {len(GRID)} limiares) = {np.mean(bb['allpos24']):.3f} | P(dif24 < 0 nos {len(GRID)} limiares) = {np.mean(bb['npos24'] == 0):.3f} | "
      f"P(dif24 do mesmo sinal nos {len(GRID)} limiares, qualquer sinal) = {np.mean((bb['npos24'] == len(GRID)) | (bb['npos24'] == 0)):.3f} | "
      f"P(dif12 < 0 em todos os limiares) = {np.mean(bb['nneg12'] == len(GRID)):.3f}")
W("\n--- TESTE C4 (H2: LP de J^fam em h=12): por que não há bootstrap sob a nula linear ---")
W("A nula do bootstrap recursivo é a linearidade do VAR, sob a qual o efeito de J^fam NÃO é zero (a IRF do DGP é diferente de zero); "
  "C4 testa efeito nulo, e a nula de efeito zero exigiria outro DGP (J^fam exógeno), o que muda o problema. "
  "O que o mesmo laço calibra, a custo marginal, é o tamanho do teste HAC: a distribuição de (b_LP - IRF_VAR do DGP)/EP_NW sob o DGP linear.")
for sc in boot:
    tc = boot[sc]['t_j12_c']
    W(f"[{sc}] IRF verdadeira do DGP (h=12) = {IRF_J12:+.4f}; LP observada = {obs['j12_b']:+.4f} (EP NW {obs['j12_se']:.4f}, t = {obs['t_j12_0']:+.2f}) | "
      f"rejeição bilateral a 5% da IRF verdadeira com valor crítico 1,96 = {np.mean(np.abs(tc) > 1.96):.3f} | valor crítico bootstrap de 95% de |t| = {np.quantile(np.abs(tc), 0.95):.2f} | "
      f"P(|t_replica| >= |t_obs|) com a nula 'LP = IRF do VAR' = {np.mean(np.abs(tc) >= abs(obs['t_j12_0'])):.4f}")
W("(a última razão é só descritiva: |t_obs| contra a distribuição de |t| centrada na IRF verdadeira; não é o p-valor de H2.)")

W("\n=== G. GRADE DE LIMIARES (completa; usada no texto) ===")
W("limiar | quantil | meses no platô | gamma12 (EP NW) | t gamma12 | dif12 | p Wald12 | dif24 | p Wald24 | no trimming 15%")
for _, r in gridG.iterrows():
    i = list(GRID).index(r['thr'])
    W(f"{r['thr']:5.1f}% | {QGRID[i]:.2f} | {int(r['n_high']):3d} | {r['g12']:+.2f} ({r['seg12']:.2f}) | {r['tg12']:+.2f} | "
      f"{r['dif12']:+.2f} | {r['pw12']:.3f} | {r['dif24']:+.2f} | {r['pw24']:.3f} | {'sim' if TRIM[i] else 'não'}")
W(f"dif12 < 0 em {int((gridG['dif12'] < 0).sum())} de {len(gridG)} limiares; dif24 > 0 em {int((gridG['dif24'] > 0).sum())} de {len(gridG)}; "
  f"gamma12 > 0 em {int((gridG['g12'] > 0).sum())} de {len(gridG)} (t > 1,96 em {int((gridG['tg12'] > 1.96).sum())}); "
  f"p Wald24 < 0,05 em {int((gridG['pw24'] < 0.05).sum())}, p Wald12 < 0,05 em {int((gridG['pw12'] < 0.05).sum())}")

# Figura 6
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.6))
gx = gridG['thr'].values
for ax, est, se, title in [
    (axes[0], gridG['g12'], gridG['seg12'], r'(a) $\hat{\gamma}^{12}$ por limiar'),
    (axes[1], gridG['dif12'], gridG['sedif12'], r'(b) $\hat{\beta}_{alto}^{12}-\hat{\beta}_{mod}^{12}$ por limiar'),
    (axes[2], gridG['dif24'], gridG['sedif24'], r'(c) $\hat{\beta}_{alto}^{24}-\hat{\beta}_{mod}^{24}$ por limiar')]:
    ax.axhline(0, color='black', lw=1, ls='--')
    ax.plot(gx, est, color='#333333', marker='o', lw=1.8)
    ax.fill_between(gx, est - 1.96 * se, est + 1.96 * se, color='#999999', alpha=0.3, label='IC 95% Newey-West')
    ax.axvline(thr, color='#b2182b', lw=1, ls=':', label=f'Mediana ({thr:.2f}%)')
    ax.set_title(title, fontweight='bold'); ax.set_xlabel('Limiar da MM12 da Selic (% a.a.)'); ax.set_ylabel('p.p. acumulados')
    ax.legend(loc='best', fontsize=8)
plt.tight_layout()
for path in [os.path.join(FIG_DIR, "figura6_grade_limiares.png"), os.path.join(PROJECT_ROOT, "figura6_grade_limiares.png")]:
    plt.savefig(path, dpi=300)
plt.close()

with open(os.path.join(RES_DIR, "inferencia_regimes.txt"), "w", encoding="utf-8") as f:
    f.write("=== INFERÊNCIA SOBRE H1 ===\n")
    f.write(f"Limiar {thr:.2f}% a.a.; d.p. do choque {sd:.4f}; base: VAR(6) e LP com sazonais, IC-Br em US$\n\n")
    f.write("\n".join(lines) + "\n")
print("Salvo: resultados/inferencia_regimes.txt")
