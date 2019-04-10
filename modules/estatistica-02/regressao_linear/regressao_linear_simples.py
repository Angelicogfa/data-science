# Instale o pacote no terminal do anaconda
# conda install yeallowbrick

#%% Importação das dependencias e execução dos codigos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

import os
import os.path

path = os.path.abspath(os.path.dirname(__file__))

# Import da base de dados
base = pd.read_csv(os.path.join(path, "../../../dados/cars.csv"))

# Remoção da primeira coluna (nome da coluna) - axis (indica que é coluna)
base = base.drop(["Unnamed: 0"], axis = 1)

# iloc => obtem os registros
# : indica todos as linhas
# 1 indica a primeira coluna
# Obtem todos os registros da coluna 1. values = retorna como array
X = base.iloc[:, 1].values
print(X)
# Variavel dependente
Y = base.iloc[:, 0].values
print(Y)

# Obtem a correção entre os valores a fim de avaliar 
# se os dados podem ser aplicados à um modelo de regressão linear
correlacao = np.corrcoef(X, Y)
print(correlacao)

# Cria uma instancia de regressao linear
modelo = LinearRegression()

# Converte o array em uma matriz para poder gerar o modelo
X = X.reshape(-1, 1)

# Preenche o modelo com os valores de X e Y
modelo.fit(X, Y)

# Intercecção entre x e y (inicio da linha de regressão)
print(modelo.intercept_)

# Coeficiente 
print(modelo.coef_)

#%% 
# Gera o grafico
# scatter - gera o grafico com os pontos 
plt.scatter(X, Y)
# plot - com base nos pontos, gera a linha de melhor ajuste
plt.plot(X, modelo.predict(X), color = 'red')

# Obs - Rode os dois comandos acima simuntaneamente para montar o grafico
# de disperção com a linha de melhor ajuste

# Distancia de parada 22 pés(previsão de qual velocidade estava)
distancia = 22
modelo.intercept_ + modelo.coef_ * distancia
# ou
modelo.predict(np.array(distancia).reshape(-1,1))

# Residuais - Distancia entre os pontos com base na linha de regressão
print(modelo._residues)
#%%
# Gera um novo grafico com base no modelo para melhor visualização dos residuais
visualizador = ResidualsPlot(modelo)
visualizador.fit(X, Y)
visualizador.poof()
