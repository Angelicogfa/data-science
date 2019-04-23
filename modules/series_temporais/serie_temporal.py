import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

import os
path = os.path.abspath(os.path.dirname(__file__))

base = pd.read_csv(os.path.join(path, '../../dados/AirPassengers.csv'))
print(base)

# Para converter campo em data é necessario informar a coluna que será formatada 'parse_dates'
# A base de dados lida passará a ter um novo indice, de acordo com a coluna 'index_col'
# O date_parser recebe uma funcao lambda para converter o valor da coluna de parse_dates no 
# argumento da função lambda
base = pd.read_csv(os.path.join(path, '../../dados/AirPassengers.csv'),
                   parse_dates = ['Month'],
                   index_col = 'Month',
                   date_parser = lambda date: pd.datetime.strptime(date, '%Y-%m'))
print(base)

# Obtem todos os indices da base
base.index

# Converte o tipo de dataframe para series
ts = base['#Passengers']
          
# Pesquisa os registros com base nos indices informados, podendo estes serem datas on posições
ts[1]
ts[1:5]
ts['1949-02-01']
ts[datetime(1949, 2,1)]
ts[datetime(1949, 2, 1): datetime(1950, 2, 1)]

# Indices maximos e minimos
ts.index.max()
ts.index.min()

plt.plot(ts)

ts_ano = ts.resample('A').sum()
plt.plot(ts_ano)

ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)

ts_datas= ts['1960-01-01':'1960-12-31']
plt.plot(ts_datas)