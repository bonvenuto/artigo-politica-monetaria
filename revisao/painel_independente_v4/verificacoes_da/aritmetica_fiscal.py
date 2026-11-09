"""
Aritmética fiscal do corte da Selic — versão 4 (itens REV-08, REV-21 a REV-24 do painel independente).

Insumos com fonte, data e conceito (Tabela de insumos fiscais):
- SGS/BCB: DBGG (13762), DLSP (4513), NFSP nominal e primária em 12 meses (5727, 5793), IPCA 12m (13522),
  PIB acumulado em 12 meses (4382), Selic (4189).
- Tesouro Nacional, Relatório Mensal da Dívida (RMD) de setembro de 2026: participação de títulos de taxa
  flutuante na DPF, estoque da DPF, custo médio em 12 meses, prazo médio e percentual vincendo em 12 meses.

Cenários para a variação da razão dívida/PIB no primeiro ano, a partir de b_t = b_{t-1}(1+i)/(1+g) - s:
  db ≈ x·Δī_1/(1+g) - b·(1+ī)·Δg/(1+g)^2,
com x = estoque remunerado à Selic (% PIB), Δī_1 = variação média da Selic no primeiro ano (corte gradual em
12 meses: metade do corte total), Δg = ω·Δī_1 (repasse fisheriano à inflação e ao PIB nominal, ω ∈ {0, 0,5, 1};
crescimento real inalterado).

Autor: Ângelo Augusto Bonvenuto
"""

import os

import pandas as pd

from comum import PROJECT_ROOT, RES_DIR

comp = pd.read_csv(os.path.join(PROJECT_ROOT, "data", "base_complementar_bcb.csv"), index_col=0, parse_dates=True)
base = pd.read_csv(os.path.join(PROJECT_ROOT, "data", "base_macro_bcb.csv"), index_col=0, parse_dates=True)

REF = pd.Timestamp('2026-08-01')
REF_1 = pd.Timestamp('2025-08-01')
# RMD set/2026 (Tesouro Nacional; tabela 2.1 e seções 2.1, 3.1, 3.2 e 4.1)
RMD = dict(dpf_bi=9382.95, flutuante=0.5160, flutuante_ago=0.5274, custo_dpf=12.63, custo_dpmfi=13.03,
           prazo_medio=4.10, vincendo_12m=0.1995)

dbgg, dlsp = comp.loc[REF, 'dbgg'], comp.loc[REF, 'dlsp']
nfsp_nom, prim = comp.loc[REF, 'nfsp_nominal_12m'], comp.loc[REF, 'nfsp_primario_12m']
juros = nfsp_nom - prim
ipca12 = comp.loc[REF, 'ipca_12m']
g_nom = comp.loc[REF, 'pib_12m'] / comp.loc[REF_1, 'pib_12m'] - 1
selic = base.loc[REF, 'selic']
pib_set = comp.loc['2026-09-01', 'pib_12m'] / 1e3  # R$ bilhões
x_dpf = RMD['flutuante'] * RMD['dpf_bi'] / pib_set * 100
x_dbgg = RMD['flutuante'] * dbgg
i_impl_dlsp = juros / comp.loc[REF_1, 'dlsp'] * (1 + g_nom) * 100
d_dbgg = dbgg - comp.loc[REF_1, 'dbgg']
d_dlsp = dlsp - comp.loc[REF_1, 'dlsp']
i_bar = RMD['custo_dpf'] / 100
auto_dbgg = (i_bar - g_nom) / (1 + g_nom) * dbgg
TARGET = 7.5
dI = TARGET - selic


def db(x, b, di1, omega, ibar=i_bar, g=g_nom):
    dg = omega * di1 / 100
    return x * (di1 / 100) / (1 + g) - b * (1 + ibar) * dg / (1 + g) ** 2


out = os.path.join(RES_DIR, "aritmetica_fiscal.txt")
with open(out, "w", encoding="utf-8") as f:
    f.write("=== TABELA DE INSUMOS FISCAIS (referência: ago/2026, salvo indicação) ===\n")
    f.write(f"DBGG (SGS 13762): {dbgg:.2f}% PIB | DLSP (SGS 4513): {dlsp:.2f}% PIB\n")
    f.write(f"NFSP nominal 12m (SGS 5727): {nfsp_nom:.2f}% PIB | NFSP primária 12m (SGS 5793): {prim:.2f}% PIB (positivo = déficit)\n")
    f.write(f"Juros nominais 12m (5727 - 5793): {juros:.2f}% PIB\n")
    f.write(f"IPCA 12m (SGS 13522): {ipca12:.2f}% | crescimento do PIB nominal 12m (SGS 4382, ago/26 sobre ago/25): {g_nom*100:.2f}%\n")
    f.write(f"Selic (SGS 4189, ago/2026): {selic:.2f}% a.a.\n")
    f.write(f"RMD set/2026: DPF R$ {RMD['dpf_bi']:.2f} bi; taxa flutuante {RMD['flutuante']*100:.2f}% (ago: {RMD['flutuante_ago']*100:.2f}%); "
            f"custo médio 12m DPF {RMD['custo_dpf']:.2f}% (DPMFi {RMD['custo_dpmfi']:.2f}%); prazo médio {RMD['prazo_medio']:.2f} anos; "
            f"vincendo em 12m {RMD['vincendo_12m']*100:.2f}%\n")
    f.write(f"PIB 12m set/2026 (SGS 4382): R$ {pib_set:.1f} bi\n")
    f.write(f"Exposição à Selic: DPF flutuante = {x_dpf:.1f}% PIB; participação flutuante x DBGG = {x_dbgg:.1f}% PIB\n")
    f.write(f"Taxa implícita dos juros nominais sobre a DLSP: {i_impl_dlsp:.2f}% a.a.\n")
    f.write(f"Termo (ī - g)/(1+g)·b com ī = custo médio DPF e b = DBGG: {auto_dbgg:+.2f} p.p. PIB/ano; "
            f"taxa relativa (ī - g)/(1+g) = {(i_bar - g_nom)/(1+g_nom)*100:.2f}%\n")
    f.write(f"Variação observada em 12 meses (ago/25 a ago/26): DBGG {d_dbgg:+.2f} p.p.; DLSP {d_dlsp:+.2f} p.p.\n")
    f.write(f"\nCorte proposto: de {selic:.2f}% para {TARGET:.1f}% => Δi = {dI:+.2f} p.p.; corte gradual em 12 meses => Δī_1 = {dI/2:+.2f} p.p.\n")
    f.write("\n=== CENÁRIOS: variação da razão DBGG/PIB no 1º ano (p.p. do PIB; negativo = alívio) ===\n")
    f.write("x \\ ω (repasse fisheriano)  |  ω=0 (inflação rígida) | ω=0,5 | ω=1 (Fisher pleno)\n")
    for xl, x in [(f'DPF flutuante ({x_dpf:.1f}% PIB)', x_dpf), (f'flutuante x DBGG ({x_dbgg:.1f}% PIB)', x_dbgg)]:
        for di1, lab in [(dI / 2, 'gradual'), (dI, 'imediato')]:
            f.write(f"{xl:32s} Δī_1={di1:+.2f} ({lab:8s}) | " + " | ".join(f"{db(x, dbgg, di1, w):+.2f}" for w in [0, 0.5, 1]) + "\n")
    f.write("\nGrade de sensibilidade (ω = 0; corte gradual): linhas x (% PIB), colunas Δi total (p.p.)\n")
    for x in [30, 36.1, 42.8, 50]:
        f.write(f"x={x:5.1f} | " + " | ".join(f"Δi={d:+.1f}: {db(x, dbgg, d / 2, 0):+.2f}" for d in [-2, -4, -6.44]) + "\n")
    f.write("\nRegime permanente (toda a dívida refinanciada ao novo patamar, curva paralela a Δi, sem prêmio a termo):\n")
    for w in [0, 0.5, 1]:
        f.write(f"  ω={w}: db = {db(dbgg, dbgg, dI, w):+.2f} p.p. PIB/ano (limite superior do alívio com ω=0: {-db(dbgg, dbgg, dI, 0):.2f})\n")
    f.write(f"  Ritmo de rolagem: {RMD['vincendo_12m']*100:.1f}% da DPF vence em 12 meses; prazo médio {RMD['prazo_medio']:.1f} anos\n")
    f.write("\nNúmero da versão 3 (0,50 x 82,5 x 5,5 = 2,27% PIB): nominal, imediato, base DBGG, sem repasse e sem gradualismo.\n")
print(f"Salvo: {out}")
