# %%
# Importação de pacotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

# %%
# Tratamento da base de dados para remoção de coluna
# auto gerada pelo python
base = pd.read_csv("dados/mt_cars.csv")
base = base.drop(['Unnamed: 0'], axis=1)

x = base.iloc[:, 2].values
y = base.iloc[:, 0].values

correlacao = np.corrcoef(x, y)
correlacao

# %%
# Geração do modelo
modelo = LinearRegression()
x = x.reshape(-1, 1)
modelo.fit(x, y)

modelo.coef_
modelo.intercept_
modelo.score(x, y)

# Aplicando uma sintaxe parecida com o R
# Tal implementação é necessaria devido a complexidade
previsoes = modelo.predict(x)
modelo_ajustado = sm.ols(formula='mpg ~ disp', data=base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()

plt.scatter(x, y)
plt.plot(x, previsoes, color='red')

modelo.predict(np.array(200).reshape(-1, 1))

# %%
# Aplicando regressão multipla
# Obtenho as colunas de 1 à 3
x1 = base.iloc[:, 1:4].values
y1 = base.iloc[:, 0].values

# Gero um novo modelo
modelo2 = LinearRegression()
# Preencho o modelo
modelo2.fit(x1, y1)

# Gera o calculo da correlação
modelo2.score(x1, y1)
modelo_ajustado2 = sm.ols(formula='mpg ~ cyl + disp + hp', data=base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

# faz uma previsão
novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
modelo2.predict(novo)