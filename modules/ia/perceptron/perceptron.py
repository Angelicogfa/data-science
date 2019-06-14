import numpy as np
from math import exp

class Perceptron:
    def __init__(self, inputs: int):
        self.__inputs = inputs
        self.bias: float = np.random.rand()
        self.pesos = np.random.rand(self.__inputs)

    def train(self, data: np.ndarray) -> int:
        if (len(data) == 0):
            raise IndexError('Não existem dados para treinamento')
        if data.shape[0] != self.__inputs:
            raise IndexError('Quantidade de inputs incorretos')
        return self.__train_model(data)

    def __train_model(self, data: np.ndarray) -> int:
        result = np.sum(np.dot(data, self.pesos)) + self.bias
        return self.__action_function(result)        

    def __action_function(self, value) -> int:
        # Função de etapa binaria
        return 1 if value >= 1 else 0
        # sigmoide
        # return 1 / (1 + exp(-value))
        # tah
        # return 2 / (1 + exp(-2 * value)) - 1
        # ReLu
        # return value if value > 0 else 0
        # softmax
        # e = np.exp(value - np.max(value))
        # return e / e.sum()

class NetworkPerceptron:
    def __init__(self):
        self.__error = 0.0
        self.__size_data = 0

    def train(self, data: np.array, labels: np.array, epochs: int = 10, learning_rate = 0.5):

        if(len(data.shape) < 2):
            raise IndexError('Invalid data shape.')
        
        self.__error = 0.00
        self.__size_data = data.shape[1]
        self.__perceptron = Perceptron(self.__size_data)
        erro = True

        for epoch in range(epochs):
            deuerro = False
            if erro:
                print('Epoch {}'.format(epoch))
                for i, line in enumerate(data):
                    result = self.__perceptron.train(line)
                    while (result != labels[i]):
                        print('Ajustando modelo')
                        deuerro = True
                        self.__adjust_model(line, labels[i], result, learning_rate)
                        result = self.__perceptron.train(line)
                erro = deuerro
            else:
                print('Treinamento finalizado')
                break

    def __adjust_model(self, values: np.array, expected: int, value: int, learning_rate: float):
        self.__perceptron.bias += learning_rate * (expected - value) * (-1/2)
        self.__perceptron.pesos += learning_rate * (expected - value) * values / 2

    def predict(self, data_model: np.array) -> np.array:

        results = []
        if len(data_model.shape) > 1:
            if data_model.shape[1] != self.__size_data:
                raise IndexError('Shape size is incompatible with model train')

            for line in data_model:
                results.append(self.__perceptron.train(line))
            
        else:
            if data_model.shape[0] != self.__size_data:
                raise IndexError('Shape size is incompatible with model train')
            
            results.append(self.__perceptron.train(data_model))
        
        return results


rede = NetworkPerceptron()
datas = np.array([[-5.4, 6.1],[-5.9, 3.7],[-2.8, 2.9],[3.1, 7.7],[5.1, 6.3],[5.2, 4.4]])
labels = np.array([1,1,1,0,0,0])
labels.shape

rede.train(datas, labels, 50)
teste = np.array([2.2,5.4])
len(teste.shape)
rede.predict(teste)

teste2 = np.array([[-5.4, 6.1], [5.2,4.4]])
len(teste2.shape)
rede.predict(teste2)



