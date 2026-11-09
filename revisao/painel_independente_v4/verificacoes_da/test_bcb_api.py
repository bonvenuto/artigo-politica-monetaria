import pandas as pd
import requests

series_dict = {
    'selic_efetiva': 4189,
    'ipca_livres': 4447,
    'ipca_administrados': 4448,
    'ipca_cheio': 433,
    'endividamento': 19880,
    'comprometimento': 19882,
    'ibc_br': 24364,
    'ptax': 3696,
    'ic_br': 27574
}

for name, code in series_dict.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=json"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            df = pd.DataFrame(data)
            print(f"OK: {name} (code {code}) - {len(df)} rows, from {df['data'].iloc[0]} to {df['data'].iloc[-1]}")
        else:
            print(f"FAIL: {name} (code {code}) - status {r.status_code}")
    except Exception as e:
        print(f"ERROR: {name} (code {code}) - {e}")
