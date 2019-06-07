# !pip install tensorflow -U --user
import tensorflow as tf
import numpy as np
tf.__version__

# tensores com n dimensoes
np.array(3).shape # Tensor Rank 0 é um escalar, nesse exemplo o shape é ()
np.array([1,2,3]).shape # Tensor rank 1 é um vetor, nesse caso o shape é (3,)
np.array([[1,2,3], [4,5,6]]).shape # Tensor rank 2 é uma matriz, nesse caso com shape (2,3)
np.array([[[1,2,3]], [[4,5,6]]]).shape # Tensor rank 3 é um tensor, nesse caso com shape (2, 1, 3)

# Comparação entre np e tf
a = np.zeros((2,2))
b = np.ones((2,2))

np.sum(b, axis=1)
a.shape
np.reshape(a, (1,4))
b * 5 + 1
np.dot(a, b)
a[0,0], a[:,0], a


c = tf.zeros((2,2))
d = tf.ones((2,2))

tf.reduce_sum(d, reduction_indices=[1])
d.get_shape()
tf.reshape(c, (1,4))
d * 5 + 1
tf.matmul(c,d)
c[0,0], c[:,0], c[0,:]


# Exemplo de grafo com calculo aplicando uma formula
# h = ReLU(Wx + b)

# onde:
# h: saida (hipotese/previsão)
# W: pesos
# x: inputs
# b: bias
# ReLU: função de calculo linear
