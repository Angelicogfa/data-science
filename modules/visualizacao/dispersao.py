# -*- coding: utf-8 -*-
# Grafico de dispersão: Verificar se existe uma relação entre variaveis continuas
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

basepath = path.abspath(path.dirname(__file__))
path = path.join(basepath, '../../dados/trees.csv')

base = pd.read_csv(path)
plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'black', marker= '*')
plt.title('Arvores')
plt.xlabel('Volume')
plt.ylabel('Cirunferência')

plt.plot(base.Girth, base.Volume)

sns.regplot(base.Girth, base.Volume, data=base, x_jitter=0.2, fit_reg=False)