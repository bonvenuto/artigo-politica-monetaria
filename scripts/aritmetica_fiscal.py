"""
Aritmética fiscal do corte da Selic (itens REV-08, REV-21 a REV-24, RR2-09 a RR2-12 do painel independente).

Insumos com fonte, data e conceito (Tabela de insumos fiscais):
- SGS/BCB: DBGG (13762), DLSP (4513), NFSP nominal e primária em 12 meses (5727, 5793), IPCA 12m (13522),
  PIB acumulado em 12 meses (4382), Selic (4189).
- Tesouro Nacional, Relatório Mensal da Dívida (RMD) de setembro de 2026 (divulgado em 29/10/2026): participação de
  títulos de taxa flutuante e de títulos indexados a índices de preços (IPCA) na DPF, estoque da DPF, custo médio
  em 12 meses, prazo médio e percentual vincendo em 12 meses.

Decomposição da dívida: Selic/flutuante (x), indexada ao IPCA (x_IPCA; custo nominal acompanha a inflação, logo
Δcusto = ω·Δī no cenário fisheriano), prefixada e cambial (sem ajuste: custo nominal não muda).
Variação da razão dívida/PIB no primeiro ano, a partir de b_t = b_{t-1}(1+i)/(1+g) - s:
  db ≈ x·Δī_1/(1+g) - b·(1+ī)·Δg/(1+g)^2 + x_IPCA·Δg/(1+g),   Δg = ω·Δī_1
(crescimento real inalterado; o terceiro termo devolve o alívio dos indexados, tratados no segundo como prefixados).

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
           prazo_medio=4.10, vincendo_12m=0.1995,
           # Indexados a índices de preços (IPCA): 23,59% da DPF em set/2026 (agosto: 23,22%). Fonte: Tesouro Nacional,
           # RMD de setembro de 2026 (29/10/2026), apresentação/texto; conferido em reportagem do Poder360 sobre o RMD
           # (o PDF não pôde ser baixado diretamente nesta execução). Prefixados 21,14%; câmbio ≈ 3,7%.
           indexados=0.2359, indexados_ago=0.2322, prefixados=0.2114, cambio=0.037)

dbgg, dlsp = comp.loc[REF, 'dbgg'], comp.loc[REF, 'dlsp']
nfsp_nom, prim = comp.loc[REF, 'nfsp_nominal_12m'], comp.loc[REF, 'nfsp_primario_12m']
juros = nfsp_nom - prim
ipca12 = comp.loc[REF, 'ipca_12m']
g_nom = comp.loc[REF, 'pib_12m'] / comp.loc[REF_1, 'pib_12m'] - 1
selic = base.loc[REF, 'selic']
pib_set = comp.loc['2026-09-01', 'pib_12m'] / 1e3  # R$ bilhões
x_dpf = RMD['flutuante'] * RMD['dpf_bi'] / pib_set * 100
x_dbgg = RMD['flutuante'] * dbgg
x_ipca = RMD['indexados'] * RMD['dpf_bi'] / pib_set * 100
i_impl_dlsp = juros / comp.loc[REF_1, 'dlsp'] * (1 + g_nom) * 100
d_dbgg = dbgg - comp.loc[REF_1, 'dbgg']
d_dlsp = dlsp - comp.loc[REF_1, 'dlsp']
i_bar = RMD['custo_dpf'] / 100
auto_dbgg = (i_bar - g_nom) / (1 + g_nom) * dbgg
TARGET = 7.5
dI = TARGET - selic


def db(x, b, di1, omega, ibar=i_bar, g=g_nom, xi=None):
    xi = x_ipca if xi is None else xi
    dg = omega * di1 / 100
    return x * (di1 / 100) / (1 + g) - b * (1 + ibar) * dg / (1 + g) ** 2 + xi * dg / (1 + g)


def omega_star(x, b, di1, **kw):
    d0, d1 = db(x, b, di1, 0, **kw), db(x, b, di1, 1, **kw)
    return -d0 / (d1 - d0)


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
    f.write(f"Indexados ao IPCA (RMD set/2026, {RMD['indexados']*100:.2f}% da DPF; ago {RMD['indexados_ago']*100:.2f}%): x_IPCA = {x_ipca:.1f}% PIB; "
            f"prefixados {RMD['prefixados']*100:.2f}%; câmbio ≈ {RMD['cambio']*100:.1f}%\n")
    f.write(f"Taxa implícita dos juros nominais sobre a DLSP: {i_impl_dlsp:.2f}% a.a.\n")
    f.write(f"Termo bola-de-neve (ī - g)/(1+g)·b, base DBGG, ī = custo médio DPF {RMD['custo_dpf']:.2f}%: {auto_dbgg:+.2f} p.p. PIB/ano; "
            f"taxa relativa (ī - g)/(1+g) = {(i_bar - g_nom)/(1+g_nom)*100:.2f}%\n")
    snow_dlsp = (i_impl_dlsp / 100 - g_nom) / (1 + g_nom) * comp.loc[REF_1, 'dlsp']
    f.write(f"Termo bola-de-neve, base NFSP/DLSP: (i_impl - g)/(1+g)·DLSP_t-1 = ({i_impl_dlsp:.2f}% - {g_nom*100:.2f}%)/(1+g) x {comp.loc[REF_1, 'dlsp']:.2f} = {snow_dlsp:+.2f} p.p. PIB/ano\n")
    f.write(f"Variação observada em 12 meses (ago/25 a ago/26): DBGG {d_dbgg:+.2f} p.p.; DLSP {d_dlsp:+.2f} p.p.\n")
    f.write(f"\nCorte proposto: de {selic:.2f}% para {TARGET:.1f}% => Δi = {dI:+.2f} p.p.; corte gradual em 12 meses => Δī_1 = {dI/2:+.2f} p.p.\n")
    W = [-0.5, 0, 0.5, 1]
    f.write("\n=== PRIMEIRO ANO: variação da razão DBGG/PIB (p.p. do PIB; negativo = alívio) ===\n")
    f.write("Equação: db = x·Δī_1/(1+g) - b(1+ī)Δg/(1+g)^2 + x_IPCA·Δg/(1+g); Δg = ω·Δī_1. ω<0: o corte eleva a inflação (previsão convencional); "
            "custos de desancoragem e de prêmio a termo NÃO são modelados.\n")
    f.write("x \\ ω                                         | " + " | ".join(f"ω={w:+.1f}" for w in W) + " | ω* (db=0)\n")
    ex = RMD['flutuante']
    for xl, x in [(f'DPF flutuante ({x_dpf:.1f}% PIB)', x_dpf), (f'flutuante x DBGG ({x_dbgg:.1f}% PIB)', x_dbgg)]:
        for di1, lab in [(dI / 2, 'gradual'), (dI, 'imediato')]:
            f.write(f"{xl:32s} Δī_1={di1:+.2f} ({lab:8s}) | " + " | ".join(f"{db(x, dbgg, di1, w):+.2f}" for w in W)
                    + f" | {omega_star(x, dbgg, di1):.2f}\n")
    f.write("\nSem o termo dos indexados (equação anterior, indexados tratados como prefixados), para comparação:\n")
    for xl, x in [(f'DPF flutuante ({x_dpf:.1f}% PIB)', x_dpf), (f'flutuante x DBGG ({x_dbgg:.1f}% PIB)', x_dbgg)]:
        for di1, lab in [(dI / 2, 'gradual'), (dI, 'imediato')]:
            f.write(f"{xl:32s} Δī_1={di1:+.2f} ({lab:8s}) | " + " | ".join(f"{db(x, dbgg, di1, w, xi=0):+.2f}" for w in W)
                    + f" | {omega_star(x, dbgg, di1, xi=0):.2f}\n")
    f.write(f"\nJustificativa da linha 'flutuante x DBGG' ({RMD['flutuante']*100:.1f}% da DBGG = {x_dbgg:.1f}% PIB): aplica a participação das taxas flutuantes na DPF "
            "ao conceito mais amplo de dívida (DBGG), que inclui as operações compromissadas do Banco Central, remuneradas à Selic e fora da DPF. "
            "É um limite superior da exposição à Selic: supõe que a DBGG tenha a mesma composição da DPF, o que o dado público não permite verificar sem "
            "o estoque de compromissadas (alternativa: DPF flutuante + compromissadas, SGS/BCB; não incorporada aqui).\n")
    f.write("\nGrade de sensibilidade x × Δi (ω = 0; corte gradual; db em p.p. do PIB): linhas x (% PIB), colunas Δi total (p.p.)\n")
    for x in [30, 36.1, 42.8, 50]:
        f.write(f"x={x:5.1f} | " + " | ".join(f"Δi={d:+.1f}: {db(x, dbgg, d / 2, 0):+.2f}" for d in [-2, -4, -6.44]) + "\n")
    f.write("\n=== REGIME PERMANENTE (não é primeiro ano): toda a dívida refinanciada a 7,5% ===\n")
    f.write("Δī = 7,5 - custo médio do estoque (e não o corte da Selic); x = b = DBGG; sem prêmio a termo; curva paralela.\n")
    f.write("Termo dos indexados = 0: com todo o estoque repactuado, o custo nominal de todos os títulos já cai com Δī (incluí-lo contaria o efeito duas vezes).\n")
    for lab, c in [('custo médio DPF', RMD['custo_dpf']), ('custo médio DPMFi', RMD['custo_dpmfi'])]:
        dm = TARGET - c
        f.write(f"  {lab} {c:.2f}%: Δī = {dm:+.2f} p.p. | " + " | ".join(f"ω={w:+.1f}: {db(dbgg, dbgg, dm, w, xi=0):+.2f}" for w in W)
                + f" | ω* = {omega_star(dbgg, dbgg, dm, xi=0):.2f}\n")
    dm = TARGET - RMD['custo_dpf']
    f.write(f"  Conferência ω=0, DPF: {dbgg:.2f} x ({dm:+.2f}) / (1+g) = {dbgg*dm/(1+g_nom)/100:+.2f} p.p. PIB (ensaio: cerca de 4% do PIB, p. 11)\n")
    f.write(f"  Ritmo de rolagem: {RMD['vincendo_12m']*100:.1f}% da DPF vence em 12 meses; prazo médio {RMD['prazo_medio']:.1f} anos\n")
print(f"Salvo: {out}")
