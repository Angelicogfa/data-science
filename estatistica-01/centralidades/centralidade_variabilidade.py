import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
# Media
np.mean(jogadores)

# Mediana
np.median(jogadores)

# Quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.50, 0.75, 1])
quartis

# Desvio padrão
np.std(jogadores, ddof = 1)

stats.describe(jogadores)
