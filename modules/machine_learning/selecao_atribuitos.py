# Importação
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
import os

# Url do diretorio
basepath = os.path.abspath('.')
path = os.path.join(basepath, 'dados\\Credit.csv')

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
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state = 0)

# Gera o modelo
modelo = SVC()
modelo.fit(X_treinamento, y_treinamento)

# Treina o modelo
previsoes = modelo.predict(X_teste)

# Gera os percentuais de acerto
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

print("taxa de acerto {acerto} - taxa de erro: {erro}".format(acerto=round(taxa_acerto,2), erro=round(taxa_erro, 2)))

forest = ExtraTreesClassifier()
forest.fit(X_treinamento, y_treinamento)
importancias = forest.feature_importances_

X_treinamento2 = X_treinamento[:, [0,1,2,3]]
X_teste2 = X_teste[:, [0,1,2,3]]

modelo2 = SVC()
modelo2.fit(X_treinamento2, y_treinamento)
previsoes2 = modelo2.predict(X_teste2)

taxa_acerto2 = accuracy_score(y_teste, previsoes2)
taxa_erro2 = 1 - taxa_acerto2
print("taxa de acerto {acerto} - taxa de erro: {erro}".format(acerto=round(taxa_acerto2,2), erro=round(taxa_erro2, 2)))    