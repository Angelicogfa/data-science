#%%
# Importação
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
import os
from statsmodels.tsa.seasonal import seasonal_decompose

#%%
# Carregamento de arquivos
path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, '../../dados/AirPassengers.csv')

dados = pd.read_csv(path, parse_dates = ['Month'],
                    index_col = 'Month',
                    date_parser = lambda date: pd.datetime.strptime(date, '%Y-%m'))

ts = dados['#Passengers']

#%%
# Cria um grafico
plt.plot(ts)

#%%
# decomposição
decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
print(tendencia)
sazonal = decomposicao.seasonal
print(sazonal)
aleatorio = decomposicao.resid
print(aleatorio)

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

plt.subplot(4,1,1)
plt.plot(ts, label='Original')
plt.legend('best')


plt.subplot(4,1,2)
plt.plot(tendencia, label='Tendencia')
plt.legend('best')


plt.subplot(4,1,3)
plt.plot(sazonal, label='Sazonalidade')
plt.legend('best')


plt.subplot(4,1,4)
plt.plot(aleatorio, label='Aleatorio')
plt.legend('best')
plt.tight_layout()