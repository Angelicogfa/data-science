import tensorflow as tf

# Criando nodes no grafo computacional
a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)
c = tf.matmul(a, b)

# Executando o grafo computacional
with tf.Session() as sess:
     print(sess.run(c, feed_dict = { a: [[3], [2], [1]], b: [[1,2,3]] }))