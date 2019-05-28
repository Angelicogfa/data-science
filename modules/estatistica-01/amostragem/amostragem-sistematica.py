import numpy as np
import pandas as pd
from math import ceil

import os
import os.path

path = os.path.abspath('.')


# define um tamanho para a população
populacao = 150

# define um tamanho para a amostragem
amostra = 15

# obtem a quantidade de itens
k = ceil(populacao / amostra)

# gera um numero aleatorio com base em k (o +1 é para definir que o valor máximo obtido possa ser alçancado)
r = np.random.randint(low = 1, high = k + 1, size = 1)
r

# acumula os itens com base no valor inicial
acumulador = r[0]
sorteado = []

# efetua um for itentando e contatenando os valores
for i in range(amostra):
    sorteado.append(acumulador)
    acumulador += k

sorteado

# Obtem a base iris
base = pd.read_csv(os.path.join(path, "dados\\iris.csv"))

# Carrega os itens com base nos indices
base_final = base.loc[sorteado]
print(base_final)

