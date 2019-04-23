import pandas as pd
import scipy as sc
import os
import matplotlib.pylab as plt

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

ts = base['#Passengers']
plt.plot(ts)
# Média geral
ts.mean()

# Media do periodo de um ano
ts['1960-01-01':'1960-12-31'].mean()

# Media movel
media_movel= ts.rolling(window = 12).mean()
media_movel

# media movel dos ultimos 12 meses
ts[0:12].mean()
ts[1:13].mean()

plt.plot(ts)
plt.plot(media_movel, color= 'red')

# Busca os doze registros anteriores e faz uma média movel desses periodos para prever os
# proximos registros
previsoes = []
for i in range(1, 13):
    # print(i)
    superior = len(media_movel) - i
    inferior= superior - 11
    print(superior)
    print(inferior)
    print('-----')
    previsoes.append(media_movel[inferior:superior].mean())
    
previsoes = previsoes[::-1]
previsoes
plt.plot(previsoes)