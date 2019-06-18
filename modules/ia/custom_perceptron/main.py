import numpy as np
from itertools import permutations
from modules.ia.custom_perceptron.perceptron import Perceptron
from modules.ia.custom_perceptron.activate_function import function_sigmoide, function_step_binary, function_softmax

data = np.array([[0,0], [0,1], [1,0], [1,1]])
labels = np.array([0,1,1,0]).reshape(-1,1)

p1 = Perceptron(2, function_sigmoide)
print('p1 - bias: {0:1.3f} - pesos: {1}'.format(p1.bias, p1.pesos))
p2 = Perceptron(2, function_sigmoide)
print('p2 - bias: {0:1.3f} - pesos: {1}'.format(p2.bias, p2.pesos))
p3 = Perceptron(2, function_step_binary)
print('p3 - bias: {0:1.3f} - pesos: {1}'.format(p3.bias, p3.pesos))
for item in data:
    possiveis = np.array(list(permutations(item, len(item))))
    v1 = p1.train(possiveis[0])
    v2 = p2.train(possiveis[1])
    result = p3.train(np.array([v1, v2]))
    print('Valor 1: {0:1.3f} Valor 2: {1:1.3f} - Previsão: {2}'.format(v1, v2, result))