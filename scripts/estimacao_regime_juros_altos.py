"""
Projeções Locais dependentes de estado e assimétricas (resposta ao painel independente).

Base: choque do VAR(6) com 11 dummies sazonais e IC-Br em US$; LP com 6 defasagens + 11 dummies sazonais;
estado I_{t-1} = 1{MM12 da Selic > mediana}.

Saídas (resultados/regime_juros_altos_lp.txt):
- Tabela 4: coeficientes por regime, nível do platô e assimetria, com p-valores Newey-West (h+1), EWC e Holm
  (família h ∈ {3,...,24}, aplicada a todos os coeficientes de cabeçalho — REV-12, REV-13);
- banda simultânea sup-t por bootstrap de blocos móveis (pares, bloco 24, B=999) para a Figura 5 (REV-13);
- Tabela 5: bateria de robustez (com p EWC de beta_mod e do Wald, RR2-23), incluindo meta Selic de fim de mês (SGS 432, REV-15) e IC-Br em R$ (REV-29);
- Tabela 6: câmbio por regime.

Autor: Ângelo Augusto Bonvenuto
"""

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

from comum import (COVID, DF, FIG_DIR, FOCUS_COLS, CHEIO_COLS, H_FAMILY, H_REPORT, HORIZONS, PROJECT_ROOT, RES_DIR,
                   SEASONAL, build_system, cum, ewc, holm, identify_shock, lag_controls, ols_hac, plateau_state,
                   state_regs)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10, 'axes.titlesize': 11.2})
rng = np.random.default_rng(12345)


def state_lp(v, dep, shock, state, seasonal=True, extra=None, horizons=range(HORIZONS + 1), asym=False,
             cumulative=True, with_ewc=False):
    ctrls = [lag_controls(v)]
    if seasonal:
        ctrls.append(SEASONAL)
    if extra is not None:
        ctrls.append(extra)
    C = pd.concat(ctrls, axis=1)
    s_pos, s_neg = shock.clip(lower=0.0), shock.clip(upper=0.0)
    out = {}
    for h in horizons:
        y = cum(v[dep], h) if cumulative else 100.0 * (v[dep].shift(-h) - v[dep].shift(1))
        o, d = ols_hac(y, pd.concat(state_regs(shock, state) + [C], axis=1), h)
        r = {k: o.params[c] for k, c in [('b_high', 'sh_high'), ('b_mod', 'sh_mod'), ('gamma', 'gamma')]}
        r.update({'p_high': o.pvalues['sh_high'], 'p_mod': o.pvalues['sh_mod'], 'p_gamma': o.pvalues['gamma'],
                  'se_high': o.bse['sh_high'], 'se_mod': o.bse['sh_mod'], 'se_gamma': o.bse['gamma'],
                  'p_diff': float(o.wald_test('sh_high = sh_mod', scalar=True).pvalue), 'N': len(d),
                  'N_high': int(d['gamma'].sum()), 'k': d.shape[1]})
        if with_ewc:
            r['pe_high'] = ewc(o, d, 'sh_high')[3]
            r['pe_mod'] = ewc(o, d, 'sh_mod')[3]
            r['pe_gamma'] = ewc(o, d, 'gamma')[3]
            r['pe_diff'] = ewc(o, d, contrast={'sh_high': 1.0, 'sh_mod': -1.0})[3]
        if asym:
            oa, da = ols_hac(y, pd.concat([(s_pos * state).rename('sh_pos'), (s_neg * state).rename('sh_neg'),
                                           (shock * (1.0 - state)).rename('sh_mod'), state.rename('gamma'), C], axis=1), h)
            r.update({'b_pos': oa.params['sh_pos'], 'p_pos': oa.pvalues['sh_pos'],
                      'b_neg': oa.params['sh_neg'], 'p_neg': oa.pvalues['sh_neg'],
                      'p_sym': float(oa.wald_test('sh_pos = sh_neg', scalar=True).pvalue)})
            if with_ewc:
                r['pe_pos'] = ewc(oa, da, 'sh_pos')[3]
                r['pe_neg'] = ewc(oa, da, 'sh_neg')[3]
        out[h] = r
    return out


def add_holm(res, keys):
    for k in keys:
        for h, x in zip(H_FAMILY, holm([res[h][k] for h in H_FAMILY])):
            res[h][k + '_holm'] = x


# ---------------------------------------------------------------------------
# 1. Base
# ---------------------------------------------------------------------------
v = build_system()
shock, scale, _ = identify_shock(v)
state, thr, ma12 = plateau_state(v['selic'])
sd = float(shock.std())

d_selic = v['selic'].diff()
neg, pos = (shock < 0) & (state == 1), (shock > 0) & (state == 1)
counts = dict(pos=int(pos.sum()), pos_up=int((pos & (d_selic > 0)).sum()), neg=int(neg.sum()),
              neg_down=int((neg & (d_selic < 0)).sum()), neg_flat=int((neg & (d_selic == 0)).sum()),
              neg_up=int((neg & (d_selic > 0)).sum()), months_high=int((state == 1).sum()))

base = state_lp(v, 'ipca_livres', shock, state, asym=True, with_ewc=True)
add_holm(base, ['p_high', 'p_mod', 'p_gamma', 'p_diff', 'p_pos', 'p_neg'])

# ---------------------------------------------------------------------------
# 2. Bootstrap de blocos móveis (pares; choque fixo) e banda sup-t
# ---------------------------------------------------------------------------
CTRL = pd.concat([lag_controls(v), SEASONAL], axis=1)
H = list(range(HORIZONS + 1))
KEYS = ['sh_high', 'sh_mod', 'gamma']
data = {}
for h in H:
    dd = pd.concat([cum(v['ipca_livres'], h).rename('y')] + state_regs(shock, state) + [CTRL], axis=1)
    data[h] = dd
T0 = len(data[0])
L, B = 24, 999
draws = {k: np.full((B, len(H)), np.nan) for k in KEYS}
pt = {k: np.array([base[h][{'sh_high': 'b_high', 'sh_mod': 'b_mod', 'gamma': 'gamma'}[k]] for h in H]) for k in KEYS}
for b in range(B):
    starts = rng.integers(0, T0 - L, size=int(np.ceil(T0 / L)))
    ids = np.concatenate([np.arange(s, s + L) for s in starts])[:T0]
    for h in H:
        dd = data[h].iloc[ids].dropna()
        X = sm.add_constant(dd.drop(columns='y'), has_constant='add')
        beta = np.linalg.lstsq(X.values, dd['y'].values, rcond=None)[0]
        bp = dict(zip(X.columns, beta))
        for k in KEYS:
            draws[k][b, h] = bp[k]
band = {}
for k in KEYS:
    s = np.nanstd(draws[k], axis=0)
    tmax = np.nanmax(np.abs((draws[k] - np.nanmean(draws[k], axis=0)) / s), axis=1)
    c = float(np.nanquantile(tmax, 0.95))
    band[k] = dict(se=s, c=c, sig_pt=[h for h in H if abs(pt[k][h] / s[h]) > 1.96],
                   sig_sup=[h for h in H if abs(pt[k][h] / s[h]) > c])

# ---------------------------------------------------------------------------
# 3. Robustez (Tabela 5)
# ---------------------------------------------------------------------------
st10, _, _ = plateau_state(v['selic'], 10.0)
st12, _, _ = plateau_state(v['selic'], 12.0)
r_exante = (DF['selic'] - DF['exp_ipca_12m']).rolling(12).mean()
thr_ex = float(r_exante.median())
st_ex = (r_exante > thr_ex).astype(float).shift(1)

v_f = build_system(FOCUS_COLS); sh_f, _, _ = identify_shock(v_f)
v_c = build_system(CHEIO_COLS); sh_c, _, _ = identify_shock(v_c)
sh_ns, _, _ = identify_shock(v, seasonal=False)
v_m = build_system(policy='meta_selic'); sh_m, sc_m, _ = identify_shock(v_m)
v_b = build_system(icbr='brl'); sh_b, _, _ = identify_shock(v_b)

rob = [
    ('1. Sem dummies sazonais (VAR e LP)', state_lp(v, 'ipca_livres', sh_ns, state, seasonal=False, horizons=H_FAMILY, with_ewc=True)),
    ('2. Sazonais + COVID-19 (2020:03-2021:06)', state_lp(v, 'ipca_livres', shock, state, extra=COVID.to_frame(), horizons=H_FAMILY, with_ewc=True)),
    ('3. Expectativas Focus 12m (VAR 7 var.)', state_lp(v_f, 'ipca_livres', sh_f, state, horizons=H_FAMILY, with_ewc=True)),
    ('4. IPCA cheio (SGS 433) + Focus 12m', state_lp(v_c, 'ipca_cheio', sh_c, state, horizons=H_FAMILY, with_ewc=True)),
    (f'5. Regime por juro real ex ante (> {thr_ex:.2f}% a.a.)', state_lp(v_f, 'ipca_livres', sh_f, st_ex, horizons=H_FAMILY, with_ewc=True)),
    ('6. Limiar Selic MM12m > 10% a.a.', state_lp(v, 'ipca_livres', shock, st10, horizons=H_FAMILY, with_ewc=True)),
    ('7. Limiar Selic MM12m > 12% a.a.', state_lp(v, 'ipca_livres', shock, st12, horizons=H_FAMILY, with_ewc=True)),
    ('8. Choque de VAR sem sazonais (LP com sazonais)', state_lp(v, 'ipca_livres', sh_ns, state, horizons=H_FAMILY, with_ewc=True)),
    ('9. Meta Selic de fim de mês (SGS 432) no VAR', state_lp(v_m, 'ipca_livres', sh_m, state, horizons=H_FAMILY, with_ewc=True)),
    ('10. IC-Br em R$ (SGS 27574)', state_lp(v_b, 'ipca_livres', sh_b, state, horizons=H_FAMILY, with_ewc=True)),
]
for _, r in rob:
    add_holm(r, ['p_high', 'p_mod', 'p_gamma'])

corr_meta = float(pd.concat([shock, sh_m], axis=1).dropna().corr().iloc[0, 1])
corr_brl = float(pd.concat([shock, sh_b], axis=1).dropna().corr().iloc[0, 1])

# ---------------------------------------------------------------------------
# 4. Câmbio por regime (Tabela 6)
# ---------------------------------------------------------------------------
ptax = state_lp(v, 'l_ptax', shock, state, horizons=H_REPORT, cumulative=False)

# ---------------------------------------------------------------------------
# 5. Figura 5
# ---------------------------------------------------------------------------
h_axis = np.arange(HORIZONS + 1)
arr = lambda k: np.array([base[h][k] for h in h_axis])
fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.6))
ax = axes[0]
ax.axhline(0, color='black', lw=1.0, ls='--')
for key, bk, col, lab, mk, ls in [('b_high', 'sh_high', '#b2182b', f'Platô alto (MM12 > {thr:.2f}% a.a.)', 'o', '-'),
                                  ('b_mod', 'sh_mod', '#2166ac', f'Regime moderado (≤ {thr:.2f}% a.a.)', 's', '--')]:
    b_, se_ = arr(key), arr('se_' + key.split('_')[1])
    ax.plot(h_axis, b_, color=col, lw=2.2, ls=ls, marker=mk, markersize=3.6, label=lab)
    ax.fill_between(h_axis, b_ - 1.96 * se_, b_ + 1.96 * se_, color=col, alpha=0.14)
    c = band[bk]['c']; sb = band[bk]['se']
    ax.plot(h_axis, b_ - c * sb, color=col, lw=0.9, ls=':'); ax.plot(h_axis, b_ + c * sb, color=col, lw=0.9, ls=':')
ax.set_title('(a) Inflação acumulada de itens livres por regime\nChoque de +1 p.p. na Selic', fontweight='bold')
ax.set_xlabel('Horizonte (meses)'); ax.set_ylabel('p.p. acumulados'); ax.set_xticks(range(0, HORIZONS + 1, 3))
ax.legend(loc='lower left', frameon=True, fontsize=8.5,
          title='Sombreado: IC 95% Newey-West; pontilhado: banda sup-t 95% (bootstrap)', title_fontsize=7.5)
ax = axes[1]
g = arr('gamma'); sg = arr('se_gamma'); c = band['gamma']['c']; sb = band['gamma']['se']
ax.axhline(0, color='black', lw=1.0, ls='--')
ax.plot(h_axis, g, color='#d95f02', lw=2.2, marker='^', markersize=4.0, label=r'$\hat{\gamma}^h$')
ax.fill_between(h_axis, g - 1.96 * sg, g + 1.96 * sg, color='#d95f02', alpha=0.16, label='IC 95% Newey-West')
ax.plot(h_axis, g - c * sb, color='#d95f02', lw=0.9, ls=':', label='Banda sup-t 95% (bootstrap)')
ax.plot(h_axis, g + c * sb, color='#d95f02', lw=0.9, ls=':')
ax.set_title(r'(b) Nível associado ao platô alto ($\hat{\gamma}^h$)', fontweight='bold')
ax.set_xlabel('Horizonte (meses)'); ax.set_ylabel('p.p. acumulados'); ax.set_xticks(range(0, HORIZONS + 1, 3))
ax.legend(loc='upper left', frameon=True, fontsize=8.5)
plt.tight_layout()
for path in [os.path.join(FIG_DIR, "figura5_regime_juros_altos_lp.png"), os.path.join(PROJECT_ROOT, "figura5_regime_juros_altos_lp.png")]:
    plt.savefig(path, dpi=300)
plt.close()

# ---------------------------------------------------------------------------
# 6. Relatório
# ---------------------------------------------------------------------------
out = os.path.join(RES_DIR, "regime_juros_altos_lp.txt")
P3 = lambda x: f"{x:.3f}"
with open(out, "w", encoding="utf-8") as f:
    f.write("=== LPs DEPENDENTES DE ESTADO (VAR e LP com sazonais; IC-Br em US$) ===\n")
    f.write(f"Limiar (mediana da MM12 da Selic) = {thr:.2f}% a.a. | P55 = {scale:.4f} | d.p. do choque = {sd:.4f} | "
            f"min {shock.min():+.3f} max {shock.max():+.3f} | d.p. no platô = {shock[state == 1].std():.4f}\n")
    f.write(f"Meses no platô: {counts['months_high']} | surpresas + no platô: {counts['pos']} (Selic subiu em {counts['pos_up']}) | "
            f"surpresas - no platô: {counts['neg']} (Selic caiu {counts['neg_down']}, estável {counts['neg_flat']}, subiu {counts['neg_up']})\n\n")
    f.write("--- TABELA 4: coef (p NW) {p EWC} [p Holm, família h=3..24] ---\n")
    for h in H_REPORT:
        r = base[h]
        hb = lambda k: P3(r[k + '_holm']) if k + '_holm' in r else '  -  '
        f.write(f"h={h:2d} N={r['N']} N_alto={r['N_high']} N_mod={r['N'] - r['N_high']} | alto {r['b_high']:+.3f} ({P3(r['p_high'])}) {{{P3(r['pe_high'])}}} [{hb('p_high')}] | "
                f"mod {r['b_mod']:+.3f} ({P3(r['p_mod'])}) {{{P3(r['pe_mod'])}}} [{hb('p_mod')}] | "
                f"Wald alto=mod ({P3(r['p_diff'])}) {{{P3(r['pe_diff'])}}} [{hb('p_diff')}] | "
                f"gamma {r['gamma']:+.3f} ({P3(r['p_gamma'])}) {{{P3(r['pe_gamma'])}}} [{hb('p_gamma')}] || "
                f"b+ {r['b_pos']:+.3f} ({P3(r['p_pos'])}) {{{P3(r['pe_pos'])}}} [{hb('p_pos')}] | "
                f"b- {r['b_neg']:+.3f} ({P3(r['p_neg'])}) {{{P3(r['pe_neg'])}}} [{hb('p_neg')}] | p sim {P3(r['p_sym'])}\n")
    f.write("\n--- Por choque de 1 d.p. ---\n")
    for h in H_REPORT:
        r = base[h]
        f.write(f"h={h:2d} | alto {r['b_high']*sd:+.3f} | mod {r['b_mod']*sd:+.3f} | b+ {r['b_pos']*sd:+.3f} | b- {r['b_neg']*sd:+.3f}\n")
    f.write(f"\n--- BOOTSTRAP DE BLOCOS (pares, bloco {L}, B={B}; choque fixo) ---\n")
    for k in KEYS:
        f.write(f"{k:8s}: c sup-t = {band[k]['c']:.2f} | h signif. pontual (EP boot) {band[k]['sig_pt']} | h signif. sup-t {band[k]['sig_sup']}\n")
        for h in [9, 12, 18, 24]:
            f.write(f"    h={h}: est {pt[k][h]:+.3f} | EP boot {band[k]['se'][h]:.3f} | t {pt[k][h]/band[k]['se'][h]:+.2f}\n")
    f.write("\n--- TABELA 5: ROBUSTEZ — coef (p NW) {p EWC} [p Holm] ---\n")
    f.write(f"corr(choque base, choque meta Selic) = {corr_meta:.3f}; corr(choque base, choque IC-Br R$) = {corr_brl:.3f}\n")
    for name, r in rob:
        f.write(f"\n[{name}]\n")
        for h in H_FAMILY:
            x = r[h]
            f.write(f"h={h:2d} | alto {x['b_high']:+.3f} ({P3(x['p_high'])}) [{P3(x['p_high_holm'])}] | "
                    f"mod {x['b_mod']:+.3f} ({P3(x['p_mod'])}) {{{P3(x['pe_mod'])}}} [{P3(x['p_mod_holm'])}] | "
                    f"gamma {x['gamma']:+.3f} ({P3(x['p_gamma'])}) {{{P3(x['pe_gamma'])}}} [{P3(x['p_gamma_holm'])}] | "
                    f"Wald {P3(x['p_diff'])} {{{P3(x['pe_diff'])}}} | N={x['N']} N_alto={x['N_high']} N_mod={x['N'] - x['N_high']}\n")
    f.write("\n--- Rejeições do Wald alto=mod na bateria (5%), 10 especificações x 6 horizontes = 60 testes; contagem também por h=12 e h=24 ---\n")
    nw_all = [(n, h, r[h]['p_diff'], r[h]['pe_diff']) for n, r in rob for h in H_FAMILY]
    f.write(f"NW: {sum(p < 0.05 for _, _, p, _ in nw_all)} de {len(nw_all)}; EWC: {sum(pe < 0.05 for _, _, _, pe in nw_all)} de {len(nw_all)}\n")
    for hh in [12, 24]:
        sel_ = [(n, p, pe) for n, h, p, pe in nw_all if h == hh]
        f.write(f"h={hh}: NW {sum(p < 0.05 for _, p, _ in sel_)} de {len(sel_)}; EWC {sum(pe < 0.05 for _, _, pe in sel_)} de {len(sel_)}\n")
    f.write("Atenção: as especificações e os horizontes compartilham amostra, choque e controles; os testes são fortemente correlacionados, "
            "e a contagem de rejeições não tem a distribuição binomial usada no argumento 'por acaso'.\n")
    f.write("\n--- TABELA 6: CÂMBIO 100 x [ln PTAX(t+h) - ln PTAX(t-1)] ---\n")
    for h in H_REPORT:
        r = ptax[h]
        f.write(f"h={h:2d} | alto {r['b_high']:+.3f} ({P3(r['p_high'])}) | mod {r['b_mod']:+.3f} ({P3(r['p_mod'])}) | Wald {P3(r['p_diff'])}\n")
print(f"Salvo: {out}")
