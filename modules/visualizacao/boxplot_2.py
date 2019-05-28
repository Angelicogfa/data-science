from os import path
import pandas as pd
import seaborn as sns

basepath = path.abspath('.')
path = path.join(basepath, 'dados\\trees.csv')
base = pd.read_csv(path)

sns.boxplot(base.Volume).set_title('Arvores')
sns.boxplot(data= base)