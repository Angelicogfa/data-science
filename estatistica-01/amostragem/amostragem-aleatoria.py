import pandas as pd
import numpy as np

# Lê o conteudo do arquivo csv
base = pd.read_csv("dados/iris.csv")
base

# Obtem a quantidade de linhas e colunas
base.shape

# define uma chave para armazenar sempre a mesma geração de item
# se a chave não existe ele cria e define os valores gerados
# se existir, exibe os mesmos valores obtidos anteriormente
np.random.seed(1)

# Amostra aleatoria - (a) = valores a serem gerados (size) = Tamanho da amostrage (replace) = Amostragem por reposição (p) = probabilidade de sair os itens com base 
# no mesmo array o elemento (a)
amostra = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.5, 0.5])

# Quantidade de itens
len(amostra)

# Quantidade de itens com opção 1
len(amostra[amostra == 1])

# Quantidade de itens com opção 0
len(amostra[amostra == 0])