#%%
# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

import os
import os.path

path = os.path.abspath('.')

#%%
# Importação do dataset
base = pd.read_csv(os.path.join(path, "dados\\Eleicao.csv"), sep = ";")
print(base)

#%%
# Geração de grafico
plt.scatter(base.DESPESAS, base.SITUACAO)

#%%
# Dados estatisticos
base.describe()
np.corrcoef(base.DESPESAS, base.SITUACAO)

#%%
# Obtem os valores dos campos
x = base.iloc[:, 2].values
x = x[:, np.newaxis]
y = base.iloc[:, 1].values
y

#%%
# Criação do modelo
modelo = LogisticRegression()
modelo.fit(x, y)

print(modelo.coef_)
print(modelo.intercept_)

print(plt.scatter(x, y))

#%%
# Geração de numeros aleatorios, entre 10 e 300. 100 registros
x_teste = np.linspace(10, 3000, 100)

#%%
# Definindo uma função de sigmoide para geração da linha do grafico
def model(x):
    return 1 / (1 + np.exp(-x))

#%% 
# Geração do grafico
r = model(x_teste * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(x_teste, r, color = 'red')

#%%
# Efetuando novas previsoes
base_previsoes = pd.read_csv(os.path.join(path, "dados\\NovosCandidatos.csv"), sep = ";")

despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
previoes_teste = modelo.predict(despesas)
print(previoes_teste)

#%% 
# Mesclando a base com os dados de previsoes com o resultado
base_previsoes = np.column_stack([base_previsoes, previoes_teste])
print(base_previsoes)