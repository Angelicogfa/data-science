import pandas as pd
from sklearn.model_selection import train_test_split
import os
import os.path

path = os.path.abspath('.')

# importa o pacote
iris = pd.read_csv(os.path.join(path, 'dados\\iris.csv'))
print(iris)

# obtem a quantidade de itens para a propriedade class
print(iris['class'].value_counts())

# obtem apenas uma parte dos dados (da coluna 0 a 4)
print(iris.iloc[: 0:4])

# Obtem os dados de treino e teste de acordo com uma coluna definida (class) - O percentual de teste é quantidade
# de itens que serão selecionados para o valor de y
x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size=0.5, stratify=iris.iloc[:, 4])

print(x)
print(y)

# obtem a quantidade de itens
print(y.value_counts())