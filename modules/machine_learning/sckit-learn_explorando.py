#%% Imports
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

#%% O dataset boston já esta disponivel no scikit-learn. Precisamos carrega-lo

from sklearn.datasets import load_boston
boston = load_boston()

type(boston)
boston.data.shape
print(boston.DESCR)
# Nomes das colunas explanatorias
print(boston.feature_names)
# Valores da coluna preditiva (valor)
print(boston.target)

#%% Converter o dataset em um dataframe pandas
df = pd.DataFrame(boston.data)
df.head()

# Atribuindo o nome das propriedades para as colunas que estão indixadas
# numericamente
df.columns = boston.feature_names
df.head()

# Criando uma coluna preço
# e atribuindo os valores à ela
df['PRICE'] = boston.target
df.head()

#%% Analisando os dados
# Não queremos o preço da casa com variavel depdente
X = df.drop('PRICE', axis= 1)
Y = df.PRICE

plt.scatter(df.RM, Y)
plt.xlabel('Média do numero de quartos por casa')
plt.ylabel('Preço da casa')
plt.title('Relação entre número de quartos e preço')
plt.show()

#%% Treinar o modelo
from sklearn.linear_model import LinearRegression

regre = LinearRegression()
type(regre)

regre.fit(X, Y)

print('Coeficiente:',  regre.intercept_)
print('Numero de coeficientes:', len(regre.coef_))

# Prevendo o modelo com os proprios dados de treino
regre.predict(X)

# Comparando os valores reais com os previstos
plt.scatter(df.PRICE, regre.predict(X))
plt.xlabel('Preço Original')
plt.ylabel('Preço Previsto')
plt.title('Preço Original x Preço Previsto')
plt.show()

mse = np.mean((df.PRICE - regre.predict(X)) ** 2)
print('Erro médio quadrado:', mse)

# Aplicando a regressão à uma unica variavel de explicação e calculando o MSE
regre = LinearRegression()
regre.fit(X[['PTRATIO']], df.PRICE)
mse2 = np.mean((df.PRICE - regre.predict(X[['PTRATIO']])) ** 2)
print('Erro médio quadrado 2:',mse2)

#%% Dividindo base em treino e teste manualmente

X_treino = X[:-50]
X_teste = X[-50:]

Y_treino = Y[:-50]
Y_teste = Y[-50:]

print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)


# Dividindo a base em treino e teste via função
from sklearn.model_selection import train_test_split
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, df.PRICE, test_size = 0.30, random_state = 5)

help(train_test_split)
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

regre = LinearRegression()
regre.fit(X_treino, Y_treino)

pred_treino = regre.predict(X_treino)
pred_teste = regre.predict(X_teste)

# Comparando preços originais X preços previstos

plt.scatter(regre.predict(X_treino), regre.predict(X_treino) - Y_treino, c='b', s=40, alpha=0.5)
plt.scatter(regre.predict(X_teste), regre.predict(X_teste) - Y_teste, c='g', s=40, alpha=0.5)
plt.hlines(y = 0, xmin= 0, xmax= 50, colors='r')
plt.ylabel('Residuo')
plt.title('Residual Plot - Treino (azul) X Teste (verde)')
plt.show()
#%%
