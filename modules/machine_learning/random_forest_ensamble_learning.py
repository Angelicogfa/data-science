# Importação
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import os

# Url do diretorio
basepath = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(basepath, '../../dados/Credit.csv')

# Carregando dados
credito = pd.read_csv(path)
# Separando dados da classe
previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:, 20].values

# Convertendo valores das colunas categorias para numericas
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

# Fragmentando a massa em teste e treino
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state =0)

# Geração do modelo
floresta = RandomForestClassifier(n_estimators=100)
floresta.fit(X_treinamento, y_treinamento)

previsoes = floresta.predict(X_teste)

confusao = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto


floresta.estimators_
floresta.estimators_[1]