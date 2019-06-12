# Workflow
# 1) Definição de problema de negócio
# 2) Preparação dos dados
# 3) Seleção do algoritmo
# 4) Treinamento do modelo
# 5) Teste e Avaliação do modelo

# Definição do objetivo
# Construção de um modelo de machine learning para prever a ocorrência de diabetes tendo esse modelo 70% ou mais de acertividade

# importação das bibliotecas
import pickle
from os import path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregamento dos dados
diretorio = path.join(path.abspath('.'), 'dados')
df = pd.read_csv(path.join(diretorio, 'pima-data.csv'))

# Verificando o shape 
df.shape

# Verificando as primeiras linhas do dataset
df.head()

# Verificando as ultimas linhas do dataset
df.tail()

# Verificando se existem valores nulos
df.isnull().values.any()

# Verificando a correlação entre variaveis
# Correlação não implica em casualidade

def plot_corr(df, size = 10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize = (size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

plot_corr(df)

# Visualizando a correlação em tabela
# Coeficiente de correlação:
# +1 - Forte correlação positiva
# 0 - Não há correlação
# -1 - forte correlação negativa
df.corr()

# Ajustando valores da classe de categorica para quantitativa
df['diabetes'] = df['diabetes'].map(lambda x: 1 if x == True else 0)
df.head()

# Verificando como os dados estão distribuidos
classTrue = len(df[df['diabetes'] == 1])
classFalse = len(df[df['diabetes'] == 0])
print('Numero de casos verdadeiros: {0} ({1:2.2f}%)'.format(classTrue, (classTrue / (classTrue + classFalse) * 100)))
print('Numero de casos falsos: {0} ({1:2.2f}%)'.format(classFalse, (classFalse / (classTrue + classFalse) * 100)))

# Spliting
# 70% para dados de treino e 30% para dados de testes

# Seleção de variaveis preditoras (feature selection)
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp','thickness','insulin','bmi','diab_pred','age']

# Seleção de variavel alvo (target)
atributo_alvo = ['diabetes']

# Criando objetos
X = df[atributos].values
Y = df[atributo_alvo].values

# Definindo a taxa de split
split_test_size = 0.3

# Criando a divisão
x_train, x_test, y_train, y_test =  train_test_split(X, Y, test_size = split_test_size, random_state = 42)

# Imprimindo os resultados
print('{0:0.2f}% nos dados de treino'.format((len(x_train)/len(df.index))*100))
print('{0:0.2f}% nos dados de teste'.format((len(x_test)/len(df.index))*100))

print('Original class true: {0} ({1:0.2f}%)'.format(len(df.loc[df['diabetes'] == 1]), len(df.loc[df['diabetes'] == 1])/len(df.index) * 100))
print('Original class false: {0} ({1:0.2f}%)'.format(len(df.loc[df['diabetes'] == 0]), len(df.loc[df['diabetes'] == 0])/len(df.index) * 100))
print('')
print('Training class true: {0} ({1:0.2f}%)'.format(len(y_train[y_train[:] == 1]), len(y_train[y_train[:] == 1])/len(y_train) * 100))
print('Training class false: {0} ({1:0.2f}%)'.format(len(y_train[y_train[:] == 0]), len(y_train[y_train[:] == 0])/len(y_train) * 100))
print('')
print('Test class true: {0} ({1:0.2f}%)'.format(len(y_test[y_test[:] == 1]), len(y_test[y_test[:] == 1])/len(y_test) * 100))
print('Test class false: {0} ({1:0.2f}%)'.format(len(y_test[y_test[:] == 0]), len(y_test[y_test[:] == 0])/len(y_test) * 100))

# Valores missing ocultos
# Verificando se existem valores nulos
df.isnull().values.any()

df.head()
print('Linhas no data frame {0}'.format(len(df)))
print('Linhas missing glucose_conc: {0}'.format(len(df.loc[df['glucose_conc'] == 0])))
print('Linhas missing diastolic_bp: {0}'.format(len(df.loc[df['diastolic_bp'] == 0])))
print('Linhas missing thickness: {0}'.format(len(df.loc[df['thickness'] == 0])))
print('Linhas missing insulin: {0}'.format(len(df.loc[df['insulin'] == 0])))
print('Linhas missing bmi: {0}'.format(len(df.loc[df['bmi'] == 0])))
print('Linhas missing age: {0}'.format(len(df.loc[df['age'] == 0])))

# Tratamento Dados Missing - Impute
# Substituindo os valores igual a zero pela média dos dados
preenche_0 = Imputer(missing_values = 0, strategy = 'mean', axis = 0)

# Substituindo os valores iguais a zero, pela media dos dados
x_train = preenche_0.fit_transform(x_train)
x_test = preenche_0.fit_transform(x_test)

# Construindo e treinamento o modelo
# Utilizando o modelo preditivo
modelo_v1 = GaussianNB()

# treinando o modelo
modelo_v1.fit(x_train, y_train.ravel())

# Verificando a exatidão do modelo treinado
nb_predict_train = modelo_v1.predict(x_train)
print('Exatidão do modelo (treino): {0:0.4f}%'.format(accuracy_score(y_train, nb_predict_train) * 100))
print('')

# Verificando a exatidão no modelo de dados de teste
nb_predict_test = modelo_v1.predict(x_test)
print('Exatidão do modelo (teste): {0:0.4f}%'.format(accuracy_score(y_test, nb_predict_test) * 100))
print('')

# Métricas
print('Confusion Metrix')

print('{0}'.format(confusion_matrix(y_test, nb_predict_test, labels=[1,0])))
print('')

print('Classification Report')
print(classification_report(y_test, nb_predict_test, labels=[1,0]))

# Otimizando o modelo com RandomFlorest
modelo_v2 = RandomForestClassifier(random_state = 42)
modelo_v2.fit(x_train, y_train.ravel())

# Vericando os dados de treino
rf_predict_train = modelo_v2.predict(x_train)
print('Exatidão do modelo (treino): {0:0.4f}%'.format(accuracy_score(y_train, rf_predict_train) * 100))
print('')

# Verificando os dados de teste
rf_predict_test = modelo_v2.predict(x_test)
print('Exatidão do modelo (teste): {0:0.4f}%'.format(accuracy_score(y_test, rf_predict_test) * 100))

print('Confusion Metrix')

print('{0}'.format(confusion_matrix(y_test, rf_predict_test, labels=[1,0])))
print('')

print('Classification Report')
print(classification_report(y_test, rf_predict_test, labels=[1,0]))

# Regressão logistica
modelo_v3 = LogisticRegression(C = 0.7, random_state = 42)
modelo_v3.fit(x_train, y_train.ravel())

# Vericando os dados de treino
rl_predict_train = modelo_v3.predict(x_train)
print('Exatidão do modelo (treino): {0:0.4f}%'.format(accuracy_score(y_train, rl_predict_train) * 100))
print('')

# Verificando os dados de teste
rl_predict_test = modelo_v3.predict(x_test)
print('Exatidão do modelo (teste): {0:0.4f}%'.format(accuracy_score(y_test, rl_predict_test) * 100))

print('Confusion Metrix')

print('{0}'.format(confusion_matrix(y_test, rl_predict_test, labels=[1,0])))
print('')

print('Classification Report')
print(classification_report(y_test, rl_predict_test, labels=[1,0]))

# Resumindo
# Extraindo dos dados de testes

# Modelo usando algoritmo Naive Bayes           = 0.7359
# Modelo usando algoritmo Random Forest         = 0.7100
# Modelo usando algoritmo Regressão Logistica   = 0.7446

# Salvando o modelo no formato binario
filename = 'modelo_treinado_v3.sav'
pickle.dump(modelo_v3, open(path.join(diretorio, filename), 'wb'))

# Carregando o modelo e fazendo previsões com novos conjuntos de dados
# (x_test, y_test dever ser novos conjuntos de dados preparados com o 
# procedimento de limpeza e transformação adequados)
load_model = pickle.load(open(path.join(diretorio, filename), 'rb'))
type(load_model)
resultado1 = load_model.predict(x_test[15].reshape(1,-1))
print(resultado1)
resultado2 = load_model.predict(x_test[18].reshape(1,-1))
print(resultado2)