#%% Import
import tensorflow as tf

#%% Soma
# Constantes
a = tf.constant(5)
b = tf.constant(9)

print(a)

total = a + b
print(total)

# Sessão TF
with tf.Session() as sess:
    print('Soma de a com b é: %f' % sess.run(total))

#%% Criando os node no grafo computacional
node1 = tf.constant(5, dtype=tf.int32)
node2 = tf.constant(9, dtype=tf.int32)
node3 = tf.add(node1, node2)

sess = tf.Session()
print(sess.run(node3))
sess.close()

#%% Subtração
# Tensores randomícos
rand_a = tf.random_normal([3], 2.0)
rand_b = tf.random_uniform([3], 1.0, 4.0)

print(rand_a)
print(rand_b)

diff = tf.subtract(rand_a, rand_b)

with tf.Session() as sess:
    print('Tensor rand_a:' , sess.run(rand_a))
    print('Tensor rand_b:', sess.run(rand_b))
    print('Substituicao ente os 2 tensores é: ', sess.run(diff))

#%% Divisão
node1 = tf.constant(21, dtype=tf.int32)
node2 = tf.constant(7, dtype=tf.int32)

div = tf.math.divide(node1, node2)

with tf.Session() as sess:
    print('Divisão entre 21 e 7: ', sess.run(div))

#%% Multiplicação
vec_a = tf.linspace(0.0, 3.0, 4)
vec_b = tf.fill([4, 1], 2.0)

print(vec_a)
print(vec_b)

tensor_a = tf.constant([[4., 2.]])
tensor_b = tf.constant([[3.], [7.]])

print(tensor_a)
print(tensor_b)

prod = tf.multiply(tensor_a, tensor_b)

with tf.Session() as sess:
    print(sess.run(tensor_a))
    print(sess.run(tensor_b))
    print('Produto: ', sess.run(prod))


# outro exemplo
mat_a = tf.constant([[2,3], [9,2], [4,5]])
mat_b = tf.constant([[6,4,5], [3,7,2]])

print(mat_a)
print(mat_b)

prod = tf.matmul(mat_a, mat_b)

with tf.Session() as sess:
    print(sess.run(mat_a))
    print(sess.run(mat_b))
    print('Produto: ', sess.run(prod))