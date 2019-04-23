import pandas as pd
import os
from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima
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


modelo = ARIMA(ts, order=(2,1,2))
modelo_treinado = modelo.fit()
modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps=12)
previsoes

eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1970-01-01', ax = eixo, plot_insample=True)

modelo_auto = auto_arima(ts, m = 12, seazonal = True, trace = True)
modelo_auto.summary()
proximos_12 = modelo_auto.predict(m_periods = 12)