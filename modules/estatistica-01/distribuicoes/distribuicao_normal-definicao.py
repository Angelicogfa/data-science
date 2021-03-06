import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

itens = [7.57,  6.72,  5.59,  9.56,  4.79,  4.84,  5.87,  10.23,  9.53,  6.99,
         9.51,  9.21,  5.78,  6.72,  8.96,  7.32,  7.64,  8.53,   5.9,   7.93,
         8.82,  8.45,  7.99,  5.77,  4.76,  4.49,  8.97,  6.60,   8.55,  6.30,
         6.54,  5.98,  10.88, 8.92,  7.01,  7.58,  9.47,  6.34,   6.17,  7.46,
         8.78,  7.13,  7.71,  8.06,  7.67,  7.05,  9.66,  4.37,   15.08, 9.20,
         7.64,  5.89,  11.16, 5.35,  5.75,  8.98,  8.74,  8.20,   8.79,  5.80,
         11.7,  5.53,  7.75,  6.54,  9.79,  7.43,  9.14,  5.78,   10.31, 10.12,
         9.68,  8.11,  5.54,  10.41, 8.83,  10.00, 5.54,  10.32,  6.92,  7.93,
         10.14, 9.66,  10.67, 8.17,  8.86,  8.40,  5.15,  6.98,   8.19,  8.72,
         8.76,  8.02,  8.93,  8.54,  3.26,  10.06, 8.18,  2.43,   9.17,  12.00]

print(itens)

print(np.median(itens))
print(np.std(itens, ddof=1))

stats.probplot(itens, plot= plt)
plt.show()

# Funcao distribuição normal
# Z = (x - u) / a
# x = valor a ser obtido
# u = média
# a = desvio padrão
# Z = valor para pesquisa de tabela
# à probabilidade é acomulativa da esquerda para à direita

# Validar se a distribuição é normal:
# à media deve ser o centro de um histograma
# Deve ser simetrico entre os lados de cada eixo do grafico
# Deve encontrar a grande maioria dos dados em no máximo 3 destivos padrões da média
# Pode ser utilizado um driagrama de probabilidade normal
