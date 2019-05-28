# Detecção de outliers (variaveis que estão fora do padrão);
# Analisar a distribuição da variavel
# Comprara a distribuição de varias variaveis

from os import path
import pandas as pd
import matplotlib.pyplot as plt

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\trees.csv')
base = pd.read_csv(path)

plt.boxplot(base.Volume, vert= False)
plt.boxplot(base.Volume, vert= False, showfliers= False)
plt.boxplot(base.Volume, vert= False, showfliers= False, notch=True)

plt.boxplot(base.Volume, vert= False, showfliers= False, notch=True, patch_artist=True)
plt.title('Arvores')
plt.xlabel('Volume')

plt.boxplot(base)

plt.boxplot(base.Volume, vert=False)
plt.boxplot(base.Girth, vert=False)
plt.boxplot(base.Height, vert=False)


