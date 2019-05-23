# Import
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# carregamento do dataset
iris = datasets.load_iris()

# Obtem as quantidade dos itens da base
unicos, quantidade = np.unique(iris.target, return_counts = True)

# Gera o modelo de cluster
cluster = KMeans(n_clusters=3)

# Treina o modelo
cluster.fit(iris.data)

# Obtem os centroids
controids = cluster.cluster_centers_
# Obtem do dataset os indices no qual cada instancia foi definida
previsoes = cluster.labels_

# Valida se a quantidade na variavel quantidade está correta (matrix de confusão)
unicos2, quantidade2 = np.unique(previsoes, return_counts=True)

# Renderizando um grafico apenas com o primeiro e segundo atributo 
# do dataset iris.
# Por ser um grafico cartesiano, necessitamos passar os pontos de X e Y
# Obtemos os registros do dataset de acordo com a 'consulta' de previsoes
# de acordo com o cluster
# exemplo -> iris.data[previsoes == 0, 0] - Obtem os itens da primeira coluna do 
# dataset que tiveram como cluster o indice 0
resultados = confusion_matrix(iris.target, previsoes)
plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1],
            c = 'green', label = 'Setosa')
plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1],
            c = 'red', label = 'Versicolor')
plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1],
            c = 'blue', label = 'Virginica')
plt.legend()
