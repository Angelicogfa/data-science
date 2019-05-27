import random
import numpy
from deap import base, creator, algorithms, tools
import matplotlib.pyplot as plt

# Cria uma classe que conterá os dados
class Produto:
    def __init__(self, nome: str, espaco: float, valor: float):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
    def __str__(self):
        return 'Produto {produto} Valor: {valor} Espaco: {espaco}' \
        .format(produto=self.nome, valor = self.valor, espaco = self.espaco)
        
# Inicializa uma lista com todos os produtos
lista_produtos = []
lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))

# Lista para armazenamento dos valores separados do objeto produto
espacos = []
valores = []
nomes = []

for produto in lista_produtos:
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    nomes.append(produto.nome)

# Limite do caminhão
limite = 3

# Storage e factory para construção do algoritmo genetico
toolbox = base.Toolbox()

# Cria função fitness e registra ele como FitnessMax. Essa
# função ira ser de maximização. O parametro weights indica
# que ele irá selecionar os valores que mais se aproximarem de 1
creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
help(base.Fitness)
# Criação do individuo, ele terá o formato de lista.
# a função de validação fitness será a definida anteriormente, a FitnessMax
creator.create('Individual', list, fitness=creator.FitnessMax)

# Registra para o toolbox o atributo attr_bool, um valor randomico 0 ou 1
toolbox.register('attr_bool', random.randint, 0,1)

# Registra o individuo para a funcao de criação definida anteriormente (Individual), 
# com o atributo attr_bool com o tamanho
# de genes de len(espacos).
# A função tools.initRepeat indica que esse processo ocorrerá n vezes
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, n = len(espacos))

# Registra a população para a função individual, 
# ele será do tipo list 
# A função tools.initRepeat indica que esse processo ocorrerá n vezes
toolbox.register('population', tools.initRepeat, list, toolbox.individual)


def avaliacao(individual):
    nota = 0
    soma_espacos = 0
    for i in range(len(individual)):
       if individual[i] == 1:
           nota += valores[i]
           soma_espacos += espacos[i]
    if soma_espacos > limite:
        nota = 1
    return nota / 100000,

# Registro da função de avaliação
toolbox.register("evaluate", avaliacao)
# Registro da função de cross over para as proximas gerações
# OnePoint: Um ponto de cross over
toolbox.register("mate", tools.cxOnePoint)
# Registro da função de mutação
# mutFlipBit: Mudança de apenas um bit do gene
# indpd: percentual de change de alteração: 1%
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.01)
# Registra o método de seleção dos individuos
# selRoulette: Método de seleção por roleta
# Cada cromossomo vai ser avaliado de acordo com o valor da avaliação
toolbox.register("select", tools.selRoulette)


if __name__ == '__main__':
    random.seed(1)
    # Cria um população com n individuos
    populacao = toolbox.population(n = 20)
    probabilidade_crossover = 1.0
    probabilidade_mutacao = 0.01
    numero_geracoes = 100
    
    estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
    estatisticas.register('max', numpy.max)
    estatisticas.register('min', numpy.min)
    estatisticas.register('mean', numpy.mean)
    estatisticas.register('std', numpy.std)
    
    populacao, info = algorithms.eaSimple(populacao, toolbox, 
                                          probabilidade_crossover, 
                                          probabilidade_mutacao,
                                          numero_geracoes, estatisticas)
    
    melhores = tools.selBest(populacao, 1)
    for individuo in melhores:
        print(individuo)
        print(individuo.fitness)
        soma = 0
        for i in range(len(lista_produtos)):
            if individuo[i] == 1:
                soma += valores[i]
                print('Nome %s R$ %s' % (lista_produtos[i].nome, lista_produtos[i].valor))
        print('Melhor solucao: %s' % soma)
    
    valores_grafico = info.select('max')
    plt.plot(valores_grafico)
    plt.title('Acompanhamento dos valores')
    plt.show()
    
    