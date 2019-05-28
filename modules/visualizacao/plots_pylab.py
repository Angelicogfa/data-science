#%% Imports
# !pip install pylab -U --user
from pylab import *
import matplotlib.pyplot as plt
import matplotlib as mpl

#%% Grafico de linha
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1,0.8,0.8])
axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Grafico de linha')


#%% Grafico de linha com duas figuras
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_xlabel('y')
axes1.set_title('Figura Principal')

axes2.plot(x, y, 'g')
axes2.set_xlabel('x')
axes2.set_xlabel('y')
axes2.set_title('Figura Secundaria')

figura, axes = plt.subplots(nrows = 1, ncols = 2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Titulo')
figura.tight_layout()