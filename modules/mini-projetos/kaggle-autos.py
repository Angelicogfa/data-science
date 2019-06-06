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
# Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo 
# de caixa de câmbio

df.head()
plt.figure(figsize=(12,8))
axies = sns.barplot(x='vehicleType', y='price', data=df, hue='gearbox')
axies.set_title('Preço Médio dos veículos por tipo de veículo e tipo de caixa de câmbio')
axies.xaxis.set_label_text('Tipo de veículo', fontdict = { 'size':12})
axies.yaxis.set_label_text('Preço médio', fontdict = { 'size':12})
plt.show()

#%% Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio
# Crie um Barplot com a Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio

df.head()
plt.figure()
axies = sns.barplot(x= 'vehicleType', y  = 'powerPS', data=df, hue='gearbox')
axies.set_title('Potência média do veículo por tipo de veiculo e tipo de caixa de câmbio')
axies.xaxis.set_label_text('Tipo de veículos', fontdict = { 'size':12})
axies.yaxis.set_label_text('Potência Média', fontdict = { 'size':12})
plt.show()

#%% Calulos
# Calcule a média de preço por marca e por veículo
media = pd.DataFrame()

for b in list(df['brand'].unique()):
    for vt in list(df['vehicleType'].unique()):
        preco = df[(df['brand'] == b) & (df['vehicleType'] == vt)]['price'].mean()
        media = media.append(pd.DataFrame({ 'brand': b, 'vehicleType': vt, 'avgPrice': preco }, index=[0]))
media = media.reset_index()
del media['index']
media['avgPrice'].fillna(0, inplace=True)
media['avgPrice'].isnull().value_counts()
media['avgPrice'] = media['avgPrice'].astype(int)
media.head()

#%% Preço médio de um veículo por marca, bem como tipo de veículo
# Crie um Heatmap com Preço médio de um veículo por marca, bem como tipo de veículo
med = media.pivot('brand', 'vehicleType', 'avgPrice')
figure, ax = plt.subplots(figsize=(15,20))
sns.heatmap(med, linewidths=1, cmap='YlGnBu', annot=True, ax=ax, fmt='d')
ax.set_title('Heatmap - Preço médio de um veículo por marca e tipo de veículo', fontdict={ 'size': 20 })
ax.xaxis.set_label_text('Tipo de Veículo', fontdict={ 'size': 20 })
ax.yaxis.set_label_text('Marca', fontdict={ 'size': 20 })
plt.show()