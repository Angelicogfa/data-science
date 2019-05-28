#%%
import pandas as pd
import numpy as np
import os
import os.path

path = os.path.abspath('.')

# Lê o conteudo do arquivo csv
base = pd.read_csv(os.path.join(path, 'dados\\iris.csv'))
print(base)

# Obtem a quantidade de linhas e colunas
print(base.shape)

# define uma chave para armazenar sempre a mesma geração de item
# se a chave não existe ele cria e define os valores gerados
# se existir, exibe os mesmos valores obtidos anteriormente
np.random.seed(1)

# Amostra aleatoria - (a) = valores a serem gerados (size) = Tamanho da amostrage (replace) = Amostragem por reposição (p) = probabilidade de sair os itens com base 
# no mesmo array o elemento (a)
amostra = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.5, 0.5])

# Quantidade de itens
print(len(amostra))

# Quantidade de itens com opção 1
print(len(amostra[amostra == 1]))

# Quantidade de itens com opção 0
print(len(amostra[amostra == 0]))