# Processo de analise de dados com data python stack

# 1- Definir o problema a ser resolvido
# 2- Preparação e Exploração dos Dados
# 3 - Criação do Modelo
# 3.1 - Automatizar o processo (desejavel)
# 4 - Apresentação do Resultado   

# Vamos usar uma pesquisa recente nos EUA sobre o mercado de trabalho para programadores
# de software. Nosso objetivo é fazer uma investigação inicial dos dados a fim de detectar
# problemas com os dados, necessidade de mais variáveis, falhas na organização e necessidades 
# de transormação

#%% Imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')
from warnings import filterwarnings
filterwarnings('ignore')
from os import path


#%% Import do dataaset
diretorio = path.join(path.abspath('.'), 'dados')

df = pd.read_csv(path.join(diretorio, 'Dados-Pesquisa.csv'), sep=',', low_memory=False)
df.head()
df.describe()

#%% Distribuição de idade
# A maioria dos profissionais que trabalham como programadores de
# software estão na faixa de idade entre 20 e 30 anos, sendo 25 anos de 
# idade mais frequente
plt.hist(df.Age, bins=60)
plt.xlabel('Idade')
plt.ylabel('Número de Profissionais')
plt.title('Distribuição de idades')
plt.show()

#%% Distribuição de Sexo
# A grande maioria dos profissionais são do sexo masculino

# Definindo a quantidade
labels = df['Gender'].value_counts().index
num = len(df['EmploymentField'].value_counts().index)

# criando a lista de cores
listaHSV = [(x * 1.0 / num, 0.5, 0.5 )for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Grafico de Pizza
fatias, texto = plt.pie(df['Gender'].value_counts(), colors= listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor = (1.05,1))
plt.title('Sexo')
plt.show()

#%% Distribuição de Interesses
# Quais são os principais interesses dos participantes da pesquisa ?
# O principal interesse profissional dos programadores é o desenvolvimento web (Full-Stack, Front-End e Back-end),
# seguido pela área de Data Science

# Definida a quantidade
num = len(df['JobRoleInterest'].value_counts().index)

# Criando a lista de cores
listaHSV = [(i * 1.0 / num, 0.5, 0.5) for i in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df['JobRoleInterest'].value_counts().index
colors = ['OliveDrab', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

# Grafico de Pizza
fatias, texto = plt.pie(df['JobRoleInterest'].value_counts(), colors = listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor = (1.25, 1))
plt.title('Interesse Profissionais')
plt.show()


#%% Distribuição de Empregabilidade
# Quais as áreas de negócio em que os participantes da pesquisa trabalham ?
# A maioria dos programadores trabalham na área de desenvolvimento de software e TI,
# mas outras áreas como finanças e saúde também são siginificativas

# Definindo a quantidade
num = len(df['EmploymentField'].value_counts().index)

# Criando lista de cores
listaHSV = [(x * 1.0 / num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df['EmploymentField'].value_counts().index

# Grafico de pizza
fatias, texto = plt.pie(df['EmploymentField'].value_counts(), colors = listaRGB, startangle= 90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor = (1.3,1))
plt.title('Área de trabalho Atual')
plt.show()

#%% Preferencia de trabalho por idade
# Quais são as preferencias de trabalho por idade
# Perceba que à medida que a idade aumenta, o interesse por trabalho
# freelance também aumenta, sendo o modelo preferido por profissionais
# acima de 60 anos. Profissionais mais jovens preferem trabalhar em 
# Startups ou no seu próprio negócio. Profissionais entre 20 e 50 anos 
# preferem trabalhar em empresas de tamanho médio

# Agrupar dados
df_ageranges = df.copy()
bins = [0, 20, 30, 40, 50, 60, 100]

df_ageranges['AgeRanges'] = pd.cut(df_ageranges['Age'],
                                  bins, 
                                  labels= ['< 20', '20-30', '30-40', '40-50', '50-60', '< 60'])

df2 = pd.crosstab(df_ageranges['AgeRanges'], df_ageranges['JobPref']).apply(lambda x: x/x.sum(), axis = 1)

# help(pd.crosstab)
# Definindo a quantidade
num = len(df_ageranges['AgeRanges'].value_counts().index)

# Definindo a quantidade
num = len(df_ageranges['AgeRanges'].value_counts().index)

# Criando a lista de cores
listaHSV = [(i * 1.0/num, 0.5, 0.5) for i in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Grafico de barras (stacked)
ax1 = df2.plot(kind='bar', stacked=True, color=listaRGB, title = 'Preferencia de trabalho por idade')
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, bbox_to_anchor = (1.5, 1))


#%% Realocação por Idade
# A vontade de buscar um novo emprego diminui com a idade
# Quase 80% das pessoas abaixo de 30 anos estão preparadas para isso

# Agrupando os dados
df3 = pd.crosstab(df_ageranges['AgeRanges'], df_ageranges['JobRelocateYesNo']).apply(lambda x: x/x.sum(), axis = 1)

# Definindo a quantidade
num = len(df_ageranges['AgeRanges'].value_counts().index)

# Criando a lista de cores
listaHSV = [(i * 1.0 / num, 0.5, 0.5) for i in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Grafico de barras
ax1 = df3.plot(kind = 'bar', stacked = True, color = listaRGB, title = 'Realocação por Idade')
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, ['Não', 'Sim'], loc = 'best')

#%% Idade X Horas de Aprendizagem
# Qual a relação entre idade e horas de aprendizagem
# A idade dos profissionais não afeta a quantidade de tenpo gasto com capacitação e treinamento

from warnings import filterwarnings
filterwarnings('ignore')

df9 = df.copy()
df9 = df9.dropna(subset = ['HoursLearning'])
df9 = df9[df['Age'].isin(range(0,70))]

# Definindo os valores de x e y
x = df9['Age']
y = df9['HoursLearning']

# Computando os valores e gerando o grafico
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '*')
plt.plot(x, m * x + b, '*', color = 'red')
plt.xlabel('Idade')
plt.ylabel('Horas de treinamento')
plt.title('Idade por Horas de Treinamento')
plt.show()

#%% Investimento em Capacitação X Expectativa Salarial
# Qual a relação entre investimento em capacidade e expectativa salarial ?
# Os profissionais que investem tempo e dinheiro em capacitação e
# treinamento, em geral, conseguem salários mais altos, embora alguns 
# profissionais esperam altos salários, investindo 0 em treinamento

filterwarnings('ignore')

# Criando subset dos dados
df5 = df.copy()
df5 = df5.dropna(subset = ['ExpectedEarning'])
df5 = df5[df['MoneyForLearning'].isin(range(0, 60000))]

# Definindo os valores de x e y
x = df5['MoneyForLearning']
y = df5['ExpectedEarning']

# Computando os valores e gerando o gráfico
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m * x + b, '-', color = 'red')
plt.xlabel('Investimento em Treinamento')
plt.ylabel('Expectativa Salarial')
plt.title('Investimento em Treinamento vs Expectativa Salarial')
plt.show()

