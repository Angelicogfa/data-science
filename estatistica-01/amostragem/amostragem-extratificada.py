import pandas as pd
from sklearn.model_selection import train_test_split

# importa o pacote
iris = pd.read_csv("dados/iris.csv")

# obtem a quantidade de itens para a propriedade class
iris['class'].value_counts()

# obtem apenas uma parte dos dados (da coluna 0 a 4)
iris.iloc[: 0:4]

# Obtem os dados de treino e teste de acordo com uma coluna definida (class) - O percentual de teste é quantidade
# de itens que serão selecionados para o valor de y
x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size=0.5, stratify=iris.iloc[:, 4])

# obtem a quantidade de itens
y.value_counts()