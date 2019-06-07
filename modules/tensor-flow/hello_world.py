import tensorflow as tf

tf.__version__

# Cria um tensor
# Esse tensor é adicionado como um nó ao grafo
hello = tf.constant('Hello, TensorFlow!')
print(hello)

# Inicia a sessão TensorFlow
sess = tf.Session()
print(sess)

# Executa o grafo computacional
print(sess.run(hello))
sess.close()