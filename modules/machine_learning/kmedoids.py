# Import
from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

# Gera o modelo do cluster, apenas com os dados da primeira e segunda coluna
cluster = kmedoids(iris.data[:, 0:2], [3,12,20])
cluster.get_medoids()
# treina o cluster
cluster.process()

# Obtem as previsoes
previsoes = cluster.get_clusters()
# Obtem os medoids (centros utilizados)
medoides = cluster.get_medoids()

# Gera um objeto de visualização do cluster
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, data = iris.data[:, 0:2], marker='*', markersize=15)
v.show()

lista_previsoes = []
lista_real = []

for i in range(len(previsoes)):
    print('---------')
    print(i)
    print('---------')
    for j in range(len(previsoes[i])):
        print(j)
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
        
lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)

resultados = confusion_matrix(lista_real, lista_previsoes)