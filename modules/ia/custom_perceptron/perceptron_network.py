import numpy as np
from modules.ia.custom_perceptron.perceptron import Perceptron

class PerceptronNetwork:
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