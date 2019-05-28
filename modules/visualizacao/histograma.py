# -*- coding: utf-8 -*-
# O grafico de histograma serve para ilustrar como uma determinada amostra ou população
# está distribuida

from os import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\trees.csv')

base = pd.read_csv(path)

histograma= np.histogram(base.iloc[:, 1], bins = 2)

plt.hist(base.iloc[:,1], bins=6)
plt.title('Arvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')