# -*- coding: utf-8 -*-
# O grafico de densidade são utilizados para conhecer a forma da distribuição dos dados

from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\trees.csv')

base = pd.read_csv(path)

plt.hist(base.iloc[:,  1], bins = 10)
sns.distplot(base.iloc[:, 1], bins=10, hist=True, kde=True, color='blue', hist_kws={ 'edgecolor': 'black'})