from modules.ia.custom_perceptron.perceptron import Perceptron
from modules.ia.custom_perceptron.activate_function import *
from typing import List, Dict
import numpy as np

class NetworkPerceptron:
    
    def __init__(self):
        self.__number_layers = 0
        self.__layers = []
        self.__perceptron_layers = []

    def add_layer(self, count_perceptron: int, action_function: callable([[float], float]), inputs: int = 0):
        '''
        Add a layer to the network.

        count perceptron: Number of perceptrons in the layer
        action_function: Activation function
        Inputs: Quantity of inputs in the first layer
        '''
        perceptrons = []
        quantidade_inputs: int = inputs

        if self.__number_layers > 0:
            last_layers = self.__perceptron_layers[self.__number_layers - 1]
            quantidade_inputs = len(last_layers['perceptrons'])
        
        for i in range(count_perceptron):
            perceptrons.append(Perceptron(quantidade_inputs, action_function))

        item = { 'number_layer': self.__number_layers, 'perceptrons': perceptrons }
        self.__perceptron_layers.append(item)
        self.__number_layers += 1
        
    def train(self, data: np.ndarray):
        for line in data:
            print('inputs data: {}'.format(line))
            value_line = line
            for index, layers in enumerate(self.__perceptron_layers):
                print('train layer {}'.format(index))
                new_value_line = []
                for index_perceptron, perceptron in enumerate(layers['perceptrons']):
                    print('Layer {}: perceptron {}'.format(index, index_perceptron))
                    value_train = perceptron.train(value_line)
                    new_value_line.append(value_train)
                value_line = np.array(new_value_line)
            print('Predict value: {} - data: {}'.format(value_line, line))
            print(''.center(20, '-'))
            print('')

    def predict(self, data: np.ndarray) -> np.ndarray:
        predicted_value = np.array([])
        for line in data:
            value_line = line
            for layers in self.__perceptron_layers:
                new_value_line = []
                for perceptron in layers['perceptrons']:
                    new_value_line.append(perceptron.train(value_line))
                value_line = np.array(new_value_line)
            predicted_value = value_line
        return predicted_value

net = NetworkPerceptron()
net.add_layer(3, action_function=function_sigmoide, inputs = 2)
net.add_layer(2, action_function=function_sigmoide)
net.add_layer(2, action_function=function_sigmoide)


net.train(np.array([[0,0], [0,1], [1,0], [1,1]]))
value = net.predict(np.array([[1,0]]))
print(value)

