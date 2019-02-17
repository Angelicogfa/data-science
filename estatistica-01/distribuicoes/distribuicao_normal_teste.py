from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

dados = norm.rvs(size = 100)
plot = stats.probplot(dados, plot = plt)
plt.show()
stats.shapiro(dados)