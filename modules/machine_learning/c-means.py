# import
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

# Carregamento do dataset
iris = datasets.load_iris()

# Executa o modelo que gerará o cluster
r = skfuzzy.cmeans(data=iris.data.T, c=3, m=2, error = 0.05, maxiter = 1000, init=None)

# Obtem apenas o primeiro cluster
previsoes_porcentagem = r[1]

# Obtem a procentagem que o registro podera estar em cada cluster
previsoes_porcentagem[0][0]
previsoes_porcentagem[1][0]
previsoes_porcentagem[2][0]

# Obtem o maior valor de uma determinada coluna
previsoes = previsoes_porcentagem.argmax(axis = 0)
resultado = confusion_matrix(iris.target, previsoes)