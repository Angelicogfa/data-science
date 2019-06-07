#%% Imports
import numpy as np
from os import path
import tensorflow as tf
import matplotlib.pyplot as plt

#%% Definição de hyperparametros do parametros
learning_rate = 0.01
training_epochs = 10000
display_step = 200

#%% Definindo o dataset de treino e teste para um modelo de 
# preços e tamanhos de casas
# Dataset de treino
train_x = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.67,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])

n_sample = len(train_x)

# Dataset de teste
test_x = np.array([6.83,4.668,8.9,7.91,5.7,8.7,3.1,2.1])
test_y = np.array([1.84,2.273,3.2,2.831,2.92,3.24,1.35,1.03])

#%% Placeholders e variaveis
# Placeholders para as variaveis preditorias (x) e para variaveis target (y)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# Pesos e bias do modelo
W = tf.Variable(np.random.randn(), name="weigth")
b = tf.Variable(np.random.randn(), name='bias')

#%% Construindo o modelo linear
# Construindo a formula do modelo de regressão linear: y = W*X + b
linear_model = W * x + b

# Mean Squared Error (Erro quadrado médio)
const = tf.reduce_sum(tf.square(linear_model - y)) / (2 * n_sample)

# Otimização com gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(const)

#%% Executando o grafo computacional, treinando e testando o modelo
# Definindo a inicialização das variaveis
init = tf.global_variables_initializer()

# Iniciando a sessão
with tf.Session() as sess:
    # Iniciando as variaveis
    sess.run(init)

    # Treinanmento do modelo
    for epoch in range(training_epochs):

        # Otimização com Gradiente Descent
        sess.run(optimizer, feed_dict = { x: train_x, y: train_y })

        # Display de cada epoch
        if (epoch + 1) % display_step == 0:
            c = sess.run(const, feed_dict = { x: train_x, y: train_y })
            print('Epoch:{0:6} \t Cost:{1:10.4} \t W:{2:6.4} \t b:{3:6.4}'.format(epoch + 1, c, sess.run(W), sess.run(b)))

    # Imprimindo os parâmetros finais do modelo
    print('\nOtimização Concluída!')
    training_cost = sess.run(const, feed_dict = { x: train_x, y: train_y })
    print('Custo final do treinamento:', training_cost, ' - W Final:', sess.run(W), ' - b Final: ', sess.run(b), '\n')

    # Visualizando o resultado
    plt.plot(train_x, train_y, 'ro', label = 'Dados Originais')
    plt.plot(train_x, sess.run(W) * train_x + sess.run(b), label = 'Linha de Regrassão')
    plt.legend()
    plt.show()

    # Testando o modelo
    testing_cost = sess.run(tf.reduce_sum(tf.square(linear_model - y)) / (2 * test_x.shape[0]), feed_dict = { x: test_x, y: test_y })

    print('Custo final em teste: ', testing_cost)
    print('Diferença Média Quadrada Absoluta', abs(training_cost - testing_cost))

    # Display em teste
    plt.plot(test_x, test_y, 'bo', label = 'Dados em Teste')
    plt.plot(train_x, sess.run(W) * train_x + sess.run(b), label = 'Linha de Regressão')
    plt.legend()
    plt.show()

sess.close()

#%%
