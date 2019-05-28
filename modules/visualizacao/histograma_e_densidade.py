from os import path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

basepath = path.abspath('.')
local = path.join(basepath, 'dados\\trees.csv')
base = pd.read_csv(local)

sns.distplot(base.Volume, bins=10, axlabel='Volume').set_title('Arvores')
local = path.join(basepath, 'dados\\chicken.csv')
base2 = pd.read_csv(local)

agrupado = base2.groupby(['feed'])['weight'].sum()

plt.figure()
plt.subplot(3,2,1)
sns.distplot(base2[base2['feed'] == 'horsebean'].weight, hist= False).set_title('horsebean')

plt.subplot(3,2,2)
sns.distplot(base2[base2['feed'] == 'casein'].weight).set_title('casein')

plt.subplot(3,2,3)
sns.distplot(base2[base2['feed'] == 'linseed'].weight).set_title('linseed')

plt.subplot(3,2,4)
sns.distplot(base2[base2['feed'] == 'meatmeal'].weight).set_title('meatmeal')

plt.subplot(3,2,5)
sns.distplot(base2[base2['feed'] == 'soybean'].weight).set_title('soybean')

plt.subplot(3,2,6)
sns.distplot(base2[base2['feed'] == 'sunflower'].weight).set_title('sunflower')
plt.tight_layout()