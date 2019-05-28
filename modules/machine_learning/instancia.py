# Importação
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from scipy import stats
import os

# Url do diretorio
basepath = os.path.abspath('.')
path = os.path.join(basepath, 'dados\\Credit.csv')

# Carregamento do modelo
iris = datasets.load_iris()
stats.describe(iris.data)

# Separação dos dados
previsores = iris.data
classe = iris.target

X_trinamento, X_teste, Y_treinamento, Y_teste = train_test_split(previsores, classe, test_size = 0.3, random_state = 0)

# Criação do modelo
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_trinamento, Y_treinamento)

# Gera as previsoes de testes
previsoes = knn.predict(X_teste)

# Valida o modelo
confusao = confusion_matrix(Y_teste, previsoes)
taxa_acerto = accuracy_score(Y_teste, previsoes)
taxa_erro = 1- taxa_acerto

print("taxa de acerto {acerto} - taxa de erro: {erro}".format(acerto=round(taxa_acerto,2), erro=round(taxa_erro, 2)))

