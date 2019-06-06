#%% Imports
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")

#%% Dataset
clean_data_path = "dados\\autos.csv"
df = pd.read_csv(os.path.join(os.path.abspath('.'), clean_data_path),encoding="latin-1")

#%%  Distribuição de Veículos com base no Ano de Registro
#  Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
dist = sns.distplot(df['yearOfRegistration'], kde=True, color='g')
dist.set_title('Distribuição de veiculos com base no ano de registro')
dist.set(xlabel='Ano de Registro', ylabel='Densidade (KDE)')
plt.tight_layout()

#%% Variação da faixa de preço pelo tipo de veículo
# Crie um Boxplot para avaliar os outliers
boxplot = df.boxplot(column=['price'], by='vehicleType', return_type='axes', figsize=(12,8))
boxplot['price'].set_xlabel('Tipo de Veiculo', fontsize=15)
boxplot['price'].set_ylabel('Range de Preço', fontsize=15)
boxplot['price'].set_title('Analise de outliers', fontsize=18)
 
# ou

plt.figure(figsize=(12,8))
item = sns.boxplot('vehicleType', 'price', data=df)
item.set_title('Analise de outliers', color = 'red')
item.set(xlabel = 'Tipo de veiculo', ylabel='Range de preços')
plt.show()

#%% Contagem total de veículos à venda conforme o tipo de veículo
# Crie um Count Plot que mostre o número de veículos pertencentes a cada categoria 
plt.figure(figsize=(12,8))
item = sns.countplot('vehicleType',  data=df)
item.set(xlabel='Tipo de Veiculo')
item.set(ylabel='Total de Veiculos Para Venda')
item.set_title('Contagem total de veículos à venda conforme o tipo de veículo', color = 'red')
plt.show()

# ou

g = sns.factorplot(x='vehicleType', data=df, kind='count', palette='BuPu', size = 6, aspect=1.5)
g.ax.xaxis.set_label_text('Tipo de Veiculo', fontdict={ 'size': 16 })
g.ax.yaxis.set_label_text('Total de Veículos para Venda', fontdict={ 'size': 16 })
g.ax.set_title('Contagem total de veículos conforme o tipo de veículo', fontdict={ 'size': 18 })

for p in g.ax.patches:
    g.ax.annotate((p.get_height()), (p.get_x() + 0.1, p.get_height() + 500))

#%% Número de veículos pertencentes a cada marca
# Crie um Plot que mostre o número de veículos pertencentes a cada marca
plt.figure(figsize=(12,8))
item = sns.countplot(y='brand', data = df)
item.set(xlabel='Número de veiculos')
item.set(ylabel='Marca')
item.set_title('Veículos por marca')
plt.show()

# ou 
plt.figure(figsize=(12,8))
g = sns.factorplot(y='brand', data=df, kind='count',  size = 6, aspect = 1.5)
g.ax.xaxis.set_label_text('Numero de Veículos', fontdict={ 'size':16 })
g.ax.yaxis.set_label_text('Marcas', fontdict={ 'size':16 })
g.ax.set_title('Veiculos por marca')

plt.show()

#%% Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
# Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio


