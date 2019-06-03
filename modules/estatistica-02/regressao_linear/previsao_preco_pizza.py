# Suponha que você queira prever o preço da pizza. Para isso, vamos criar um modelo de regressão 
# linear para preve o preço da piza, baseado em um atributo da pizza que podemos observar. Vamos modelar
# a relação entre o tamanho (diametro) de uma pizza e seu preço. Escreveremos então um programa com sckit-learn,
# que preve o preço da pizza dado seu diametro

#%% Importe
import matplotlib.pyplot as plt
import numpy as numpy

#%% Definição dos registros
class Pizza:
    def __init__(self, diametro, preco):
        self.diametro = diametro
        self.preco = preco

registros = [
    Pizza(7, 8),
    Pizza(10, 11),
    Pizza(15, 16),
    Pizza(30, 38.5),
    Pizza(45, 52),
]

diametros = [p.diametro for p in registros]
precos = [p.preco for p in registros]

#%% Analise exploratoria dos registros
plt.figure()
plt.xlabel('Diametros (cm)')
plt.ylabel('Preço (R$)')
plt.title('Diametro x Preco')
plt.plot(diametros, precos, 'r.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()

#%% Importando o modelo de regressão linear
from sklearn.linear_model import LinearRegression
import numpy as np

# Preparando os dados de treino
X = np.array(diametros).reshape(-1,1)
Y = np.array(precos).reshape(-1,1)

# Criando o modelo
modelo = LinearRegression()
type(modelo)

modelo.fit(X, Y)
previsao = modelo.predict(np.array(20).reshape(-1, 1))
print('O preço da pizza de um diametro de 20 cm é %.2f' % previsao)
print('Coeficiente: \n', modelo.coef_)
print('MSE (mean square error): \n', np.mean((modelo.predict(X) - Y) ** 2))
print('Score de variação: %.2f' % modelo.score(X, Y))

# representando a regressão linear
plt.scatter(X, Y, color = 'b')
plt.plot(X, modelo.predict(X), color = 'r', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks()
plt.yticks()
plt.show()