import numpy as np

class Perceptron:
    def __init__(self, inputs: int, function: callable([[float], float])):
        self.__inputs = inputs
        self.__action_function = function
        self.bias: float = np.random.randn()
        self.pesos = np.random.randn(self.__inputs)

    def train(self, data: np.ndarray) -> float:
        if (len(data) == 0):
            raise IndexError('Não existem dados para treinamento')
        if data.shape[0] != self.__inputs:
            raise IndexError('Quantidade de inputs incorretos')
        return self.__train_model(data)

    def __train_model(self, data: np.ndarray) -> float:
        result = np.sum(np.dot(data, self.pesos)) + self.bias
        self.__output_value = self.__action_function(result)
        return self.__output_value

    @property
    def output_value(self):
        return self.__output_value
