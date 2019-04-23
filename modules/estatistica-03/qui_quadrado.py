#%% 
# Importação
import numpy as np
from scipy.stats import chi2_contingency

#%%
# Execução
novela = np.array([[10, 6], [43,32]])
print(novela)
print(chi2_contingency(novela))


jogos = np.array([[41,18], [34,7]])
jogos
print(chi2_contingency(jogos))