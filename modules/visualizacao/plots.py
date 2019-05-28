#%% !pip install matplotlib -U --user
import matplotlib as mpt
import matplotlib.pyplot as plt

#%% Versao
mpt.__version__

#%% Plot basico
plt.plot([1,3,5], (2,5,7))
plt.show()

#%% Plot com dados
x = [1,4,5]
y = [3,7,2]

plt.plot(x, y)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 2')
plt.title('Teste plot')
plt.show()

#%% Grafico de barras
x = [2,4,6,8,10]
y = [6,7,8,2,4]

plt.bar(x, y, label = 'Barras', color = 'r')
plt.legend()
plt.show()


#%% Grafico de barras
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label = 'Barra 1', color = 'r')
plt.bar(x2, y2, label = 'Barra 2', color = 'g')
plt.legend()
plt.show()

#%%
idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
ids = [x for x in range(len(idades))]
plt.bar(ids, idades)
plt.show()

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(idades, bins, histtype='bar', rwidth=0.8)
plt.show()

plt.hist(idades, bins, histtype='stepfilled', rwidth=0.8)
plt.show()

#%% scatterplot
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,7,8]

plt.scatter(x, y, label = 'Pontos', color = 'r', marker='o', s = 100)
plt.legend()
plt.show()

#%% Stack plot
dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'w'])
plt.show()

#%% Pie chart
fatias = [7,2,2,13]
atividades = ['dormir', 'comer', 'trabalhar', 'passear']
colunas = ['c', 'm', 'r', 'w']

plt.pie(fatias, labels= atividades, colors=colunas, startangle=90, shadow=True, explode=(0,0,0,0))
plt.show()