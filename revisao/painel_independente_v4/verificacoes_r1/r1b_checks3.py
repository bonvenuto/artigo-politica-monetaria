"""F das 11 dummies sazonais sobre a inflação de itens livres sem defasagens (origem do 'p < 1e-11'?)."""
import os, sys
import pandas as pd, statsmodels.api as sm
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'pkg', 'scripts'))
from comum import SEASONAL, build_system
v = build_system()
for lab, sl in [('amostra toda', slice(None)), ('a partir de 2005-09', slice('2005-09-01', None))]:
    d = pd.concat([v['ipca_livres'].rename('y'), SEASONAL], axis=1).loc[sl].dropna()
    o = sm.OLS(d['y'], sm.add_constant(d.drop(columns='y'))).fit()
    print(lab, 'F só dummies =', round(float(o.fvalue), 2), 'p =', f'{o.f_pvalue:.2e}')
