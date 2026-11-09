"""
Coleta das séries complementares do SGS/BCB (resposta ao painel independente).

Séries:
  29042  IC-Br em dólares (US$)                       -> ic_br_usd   (substitui a 27574, que está em R$)
  432    Meta Selic definida pelo Copom (diária)      -> meta_selic  (valor do último dia do mês)
  29035  Comprometimento c/ serviço da dívida, sem habitacional (% renda, c/ ajuste)
  29036  Comprometimento c/ amortização (% renda, c/ ajuste)  [29033 + 29036 = 29034]
  29038  Endividamento sem habitacional (% renda 12m)
  13762  DBGG (% PIB)          4513  DLSP (% PIB)
  5727   NFSP nominal 12m (% PIB)   5793  NFSP primário 12m (% PIB; positivo = déficit)
  13522  IPCA acumulado em 12 meses (%)   4382  PIB acumulado em 12 meses (R$ milhões)

Saídas: data/base_complementar_bcb.csv e data/safra_dados.txt (data de extração de cada base, gravada no momento
do download, e hash SHA-256 de cada CSV).
Autor: Ângelo Augusto Bonvenuto
"""

import datetime as dt
import hashlib
import os

import pandas as pd
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "base_complementar_bcb.csv")

MENSAIS = {
    'ic_br_usd': 29042, 'servico_sem_hab': 29035, 'amortizacao': 29036, 'endiv_sem_hab': 29038,
    'dbgg': 13762, 'dlsp': 4513, 'nfsp_nominal_12m': 5727, 'nfsp_primario_12m': 5793,
    'ipca_12m': 13522, 'pib_12m': 4382,
}


def sgs(code, inicio='01/01/2004', fim=None):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json&dataInicial={inicio}"
    if fim:
        url += f"&dataFinal={fim}"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    d = pd.DataFrame(r.json())
    d['data'] = pd.to_datetime(d['data'], format='%d/%m/%Y')
    return d.set_index('data')['valor'].astype(float)


BASE = os.path.join(ROOT, "data", "base_macro_bcb.csv")
BASE_SERIES = {
    'selic': 4189, 'ipca_livres': 11428, 'ipca_comerc': 4447, 'ipca_adm': 4449, 'ipca_cheio': 433,
    'endividamento': 29037, 'servico_divida': 29034, 'juros_divida': 29033, 'ibc_br': 24364, 'ptax': 3696,
    'ic_br': 27574,   # IC-Br em R$ (mantido para a especificação de robustez; a base usa a 29042, em US$)
}


def focus_ipca_12m():
    url = ("https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/"
           "ExpectativasMercadoInflacao12Meses?$filter=Indicador%20eq%20'IPCA'%20and%20"
           "Suavizada%20eq%20'S'%20and%20baseCalculo%20eq%200&$select=Data,Mediana&$format=json")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    d = pd.DataFrame(r.json()['value'])
    d['Data'] = pd.to_datetime(d['Data'])
    return d.set_index('Data')['Mediana'].astype(float).resample('MS').mean()


SAFRA = os.path.join(ROOT, "data", "safra_dados.txt")
extracao_base = None   # data de extração da base principal, gravada no instante do download
if not os.path.exists(BASE):
    print("Base principal ausente: baixando data/base_macro_bcb.csv")
    extracao_base = dt.date.today().isoformat()
    base = pd.DataFrame({nome: sgs(code) for nome, code in BASE_SERIES.items()})
    base['exp_ipca_12m'] = focus_ipca_12m()
    base = base.loc['2005-03-01':'2026-08-01'].dropna()
    base.index.name = 'data'
    base.to_csv(BASE)

cols = {}
for nome, code in MENSAIS.items():
    print(f"SGS {code} -> {nome}")
    cols[nome] = sgs(code)

print("SGS 432 -> meta_selic (último dia de cada mês)")
# Séries diárias: a API limita cada consulta a 10 anos
meta = pd.concat([sgs(432, '01/01/2004', '31/12/2012'), sgs(432, '01/01/2013', '31/12/2021'),
                  sgs(432, '01/01/2022')])
meta = meta[~meta.index.duplicated()]
cols['meta_selic'] = meta.resample('MS').last()

df = pd.DataFrame(cols).sort_index().loc['2004-01-01':]
df.index.name = 'data'
df.to_csv(OUT)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


# Data de extração da base principal: a do download desta execução; se a base já existia (não foi baixada agora),
# preserva a data registrada anteriormente neste arquivo; sem registro, usa a data de modificação do arquivo.
if extracao_base is not None:
    linha_base = f"base_macro_bcb.csv extraída em {extracao_base} da API SGS/BCB e Olinda/Focus"
else:
    anterior = None
    if os.path.exists(SAFRA):
        with open(SAFRA, encoding="utf-8") as fh:
            anterior = next((l.strip() for l in fh if l.startswith("base_macro_bcb.csv extraída em")), None)
    if anterior:
        linha_base = anterior
    else:
        mtime = dt.date.fromtimestamp(os.path.getmtime(BASE)).isoformat()
        linha_base = f"base_macro_bcb.csv: extração original não registrada; arquivo modificado em {mtime}"
with open(SAFRA, "w", encoding="utf-8") as f:
    f.write(f"base_complementar_bcb.csv extraída em {dt.date.today().isoformat()} da API SGS/BCB\n")
    f.write(linha_base + "\n")
    f.write(f"SHA-256 base_macro_bcb.csv: {sha256(BASE)}\n")
    f.write(f"SHA-256 base_complementar_bcb.csv: {sha256(OUT)}\n")
print(f"Salvo: {OUT} ({len(df)} linhas)")
