#%%
from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar 3 caras
prop = binom.pmf(3, 5, 0.5)
prop

# Passar por 4 sinais de 4 tempos. Qual a probabilidade de pegar sinal verde
# 1, 2, 3 ou 4 vezes
sinal1 = binom.pmf(0, 4, 0.25)
sinal1

sinal2 = binom.pmf(1, 4, 0.25)
sinal2

sinal3 = binom.pmf(2, 4, 0.25)
sinal3

sinal4 = binom.pmf(3, 4, 0.25)
sinal4

sinal5 = binom.pmf(4, 4, 0.25)
sinal5

# se for um sinal de 2 tempos
sinal2tempo = binom.pmf(4, 4, 0.5)
sinal2tempo

# Probabilidade comulativa
cumulativa = binom.cdf(4, 4, 0.25)
cumulativa

# Concurso com 12 questões com 4 opções cada, onde eu acerte 7
binom.pmf(7, 12, 0.25)

binom.pmf(12, 12, 0.25)