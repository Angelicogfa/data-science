# %%
# Importação de pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

import os
import os.path

path = os.path.abspath(os.path.dirname(__file__))

# %%
# Tratamento da base de dados para remoção de coluna
# auto gerada pelo python
base = pd.read_csv(os.path.join(path, "../../../dados/mt_cars.csv"))
base = base.drop(['Unnamed: 0'], axis=1)
print(base)

x = base.iloc[:, 2].values
print(x)
y = base.iloc[:, 0].values
print(y)

correlacao = np.corrcoef(x, y)
print(correlacao)

# %%
# Geração do modelo
modelo = LinearRegression()
x = x.reshape(-1, 1)
modelo.fit(x, y)

print(modelo.coef_)
print(modelo.intercept_)
print(modelo.score(x, y))

# Aplicando uma sintaxe parecida com o R
# Tal implementação é necessaria devido a complexidade
previsoes = modelo.predict(x)
modelo_ajustado = sm.ols(formula='mpg ~ disp', data=base)
modelo_treinado = modelo_ajustado.fit()
print(modelo_treinado.summary())

plt.scatter(x, y)
plt.plot(x, previsoes, color='red')

modelo.predict(np.array(200).reshape(-1, 1))

# %%
# Aplicando regressão multipla
# Obtenho as colunas de 1 à 3
x1 = base.iloc[:, 1:4].values
print(x1)
y1 = base.iloc[:, 0].values
print(y1)

# Gero um novo modelo
modelo2 = LinearRegression()
# Preencho o modelo
modelo2.fit(x1, y1)

# Gera o calculo da correlação
modelo2.score(x1, y1)
modelo_ajustado2 = sm.ols(formula='mpg ~ cyl + disp + hp', data=base)
modelo_treinado2 = modelo_ajustado2.fit()
print(modelo_treinado2.summary())

# faz uma previsão
novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
print(modelo2.predict(novo))