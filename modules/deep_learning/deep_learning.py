#%% Import
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist

#%% Carregamento dos dados
(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()
plt.imshow(X_treinamento[150], cmap='gray')
plt.title(y_treinamento[150])

#%% Reshape dos dados
X_treinamento = X_treinamento.reshape((len(X_treinamento), np.prod(X_treinamento.shape[1:])))
X_teste = X_teste.reshape((len(X_teste), np.prod(X_teste.shape[1:])))

#%% Conversão do tipo dos dados
X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

#%% Redução do tamanho dos dados, visto que o tamanho máximo do conteudo para imagem é 255
X_treinamento /= 255
X_teste /= 255

#%% Criação da matrix de resultado para o neuronio de saida
y_treinamento = np_utils.to_categorical(y_treinamento, 10)
y_teste = np_utils.to_categorical(y_teste, 10)

#%% Criação do modelo
modelo = Sequential()
# Adiciona a primeira camada com 64 neuronios recebendo 784 inputs
# Função de ativação: Relu - Passa o valor se ele for positivo e se for negativo
# retorna zero
modelo.add(Dense(units=64, activation='relu', input_dim=784))
# Camada para zerar dados a fim de evitar o overfit
modelo.add(Dropout(0.2))

modelo.add(Dense(units=64, activation='relu'))
modelo.add(Dropout(0.2))

modelo.add(Dense(units=64, activation='relu'))
modelo.add(Dropout(0.2))

modelo.add(Dense(units=10, activation='softmax'))

#%% Obtem o sumario do modelo
modelo.summary()

modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
historico = modelo.fit(X_treinamento, y_treinamento, epochs=50, validation_data=(X_teste, y_teste))

#%% Obtem os dados historicos utilizados
historico.history.keys()
plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_acc'])

# Gera a matriz de confusão
previsoes = modelo.predict(X_teste)
y_teste_matriz = [np.argmax(t) for t in y_teste]
y_previsoes_matriz = [np.argmax(t) for t in previsoes]
confusao = confusion_matrix(y_teste_matriz, y_previsoes_matriz)

# Preve um novo registro
# Registro imagem 0
y_treinamento[150]
novo = X_treinamento[150]
novo = np.expand_dims(novo, axis = 0)
pred = modelo.predict(novo)
pred = [np.argmax(t) for t in pred]
