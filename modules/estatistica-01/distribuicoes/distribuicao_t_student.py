from scipy.stats import t
import numpy as np

# Média de salario dos cientistas de dados = R$ 75,00 por hora
# Amostra com 9 funcionarios e desvio padrão = 10

# Qual a probabilidade de selecionar um cientista de dados e salario
# ser menor que 80 por hora
print(t.cdf(1.5, 8))

# Qual a probabilidade do salario ser maior que  80 ?
print(t.sf(1.5, 8) * 100)
# ou 
print(1- t.cdf(1.5, 8))