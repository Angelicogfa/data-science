# import 
from sklearn import datasets
from sklearn.model_selection import train_test_split
# from yellowbrick.classifier import ConfusionMatrix
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix

# Carregamento da base de dados
base = datasets.load_iris()
previsores = base.data
classe = base.target

# Faz uma transformação para criar um neuronio que conterá os resultados
# da classe da forma que a rede necessita
classe_dummy = np_utils.to_categorical(classe)

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe_dummy, test_size = 0.3, random_state = 0)



# Cria o modelo
modelo = Sequential()
modelo.add(Dense(units = 5, input_dim = 4))
modelo.add(Dense(units = 4))
modelo.add(Dense(units = 3, activation = 'softmax'))

modelo.summary()

# Compila o modelo
modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
modelo.fit(X_treinamento, y_treinamento, epochs = 1000, validation_data = (X_teste, y_teste))

# Faz previsoes
previsoes = modelo.predict(X_teste)

# Converte os dados para true ou false
previsoes = (previsoes > 0.5)

# Obtem a coluna com o maior valor
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsao_matrix = [np.argmax(t) for t in previsoes]

# Gera a matriz de confusao
confusao = confusion_matrix(y_teste_matrix, y_previsao_matrix)