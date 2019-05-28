!pip install apyori
# Imports
import pandas as pd
from apyori import apriori
import os

# Url do diretorio
basepath = os.path.abspath('.')
path = os.path.join(basepath, 'dados\\transacoes.txt')

dados = pd.read_csv(path, header=None)

transacoes = []

for i in range(0,6):
    transacoes.append([str(dados.values[i, j]) for j in range(0,3)])
    
regras = apriori(transacoes, min_support = 0.5, min_confidence=0.5)
resultados = list(regras)
resultados_2 = [list(x) for x in resultados]
resultados_3 = []

for j in range(0,7):
    resultados_3.append([list (x) for x in resultados_2[j][2]])

print(resultados_3)