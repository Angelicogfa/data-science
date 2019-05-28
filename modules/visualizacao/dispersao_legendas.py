# Grafico de dispersão com legendas para comparar variaveis categorias
# associação de valores numericos com valores categoricos
from os import path
import pandas as pd
import matplotlib.pyplot as plt

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\co2.csv')
base = pd.read_csv(path)

x = base.conc
y = base.uptake

unicos = list(set(base.Treatment))

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])
plt.legend(loc='lower right')
