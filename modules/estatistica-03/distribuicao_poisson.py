#%%
from scipy.stats import poisson

# Média de acidentes de carro é 2 por dia
# Qual a probabilidade de ocorrer 3 acidentes no dia ?
print(poisson.pmf(3, 2))

# Qual a probabilidade de ocorrer 3 ou menos acidentes no dia ?
print(poisson.cdf(3, 2))

# Qual a probabilidade de ocorrer 3 ou mais acidentes ?
print(poisson.sf(3, 2))