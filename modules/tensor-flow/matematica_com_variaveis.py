# Import
import tensorflow as tf

# Criando um node no grafo computacional
node = tf.Variable(tf.zeros([2,2]))

# Executando o grafo computacional
sess = tf.Session()

# Iniciando as variaveis
sess.run(tf.global_variables_initializer())

# Avaliando o node
print('\nTensor original:\n ', sess.run(node))

# Adicionando element-wise no tensor
node = node.assign(node + tf.ones([2,2]))

# Avaliando o node novamente
print('\nTensor depois da edição:\n ', sess.run(node))

# Encerra a sessão
sess.close()