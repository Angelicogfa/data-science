from os import path
import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

basepath = path.abspath('.')
local = path.join(basepath, 'dados\\co2.csv')
base = pd.read_csv(local)


srn.scatterplot(base.conc, base.uptake, hue = base.Type)

q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

plt.figure()
plt.subplot(1, 2, 1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')

plt.subplot(1, 2, 2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississipi')
plt.tight_layout()

# refrigerado e não refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nh = base.loc[base['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1, 2, 1)
srn.scatterplot(ch.conc, ch.uptake).set_title('Chilled')

plt.subplot(1, 2, 2)
srn.scatterplot(nh.conc, nh.uptake).set_title('Nonchilled')
plt.tight_layout()

local = path.join(basepath, 'dados\\esoph.csv')
base2 = pd.read_csv(local)

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)
srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')