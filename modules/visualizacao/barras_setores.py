# Graficos de barra e graficos de setores para variveis categorias e quando
# se deseja sumarizar os valores

from os import path
import pandas as pd
import matplotlib.pyplot as plt

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\insect.csv')
base = pd.read_csv(path)

agrupado = base.groupby(['spray'])['count'].sum()
agrupado.plot.bar(color = 'gray')

agrupado.plot.pie(legend=True)

help(plt.bar)

