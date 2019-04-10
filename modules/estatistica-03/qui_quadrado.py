#%% 
# Importação
import numpy as np
from scipy.stats import chi2_contingency

#%%
# Execução
novela = np.array([[10, 6], [43,32]])
chi2_contingency(novela)