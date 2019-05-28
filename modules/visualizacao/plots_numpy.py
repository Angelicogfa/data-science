#%% Imports
import matplotlib.pyplot as plt
import numpy as np

#%% Scatter
plt.scatter(np.arange(50), np.random.randn(50))
plt.show()

#%% Plot e Scatter
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50), color = 'r')

ax2 = fig.add_subplot(1,2,2)
ax2.plot(np.arange(50), np.random.randn(50))
plt.show()

#%% Plots diversos
_, ax = plt.subplots(2, 3)
ax[0,1].plot(np.random.randn(50), color = 'green', linestyle = '-')
ax[1,0].hist(np.random.randn(50))
ax[1,2].scatter(np.arange(50), np.random.randn(50), color = 'red')
plt.show()

#%% Controle dos eixos
fig, axes = plt.subplots(1,3, figsize = (12,4))

x = np.linspace(0, 5, 50)
axes[0].plot(x, x**2, x, x**3)
axes[0].set_title('Eixo com range padrão')

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title('Eixos menores')

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0,60])
axes[2].set_xlim([2,5])
axes[2].set_title('Eixos customizados')


#%% Escala
fig, axes = plt.subplots(1, 2, figsize = (10,4))
x = np.linspace(0, 5, 10)
axes[0].plot(x, x ** 2, x, np.exp(x))
axes[0].set_title('Escala Padrão')

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritmica (y)')

#%% Grid
fig, axes = plt.subplots(1, 2, figsize=(10,3))

axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

axes[1].plot(x, x**2, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.5)

#%% Grafico de linhas gemeas
fig, ax1 = plt.subplots()
ax1.plot(x, x**2, lw = 2, color = 'b')
ax1.set_ylabel('Area', fontsize = 18, color = 'b')
for label in ax1.get_yticklabels():
    label.set_color('blue')

ax2 = ax1.twinx()
ax2.plot(x, x**3, lw = 2, color = 'red')
ax2.set_ylabel('Volume', fontsize=18, color = 'r')
for label in ax2.get_yticklabels():
    label.set_color('red')

#%% Diferentes estilos de plots
xx = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

fig, axes = plt.subplots(1,4,figsize = (12,3))

axes[0].scatter(xx, xx + 0.25 * np.random.randn(len(xx)))
axes[0].set_title('scatter')

axes[1].step(n, n**2, lw = 2)
axes[1].set_title('step')

axes[2].bar(n, n**2, align='center', width=0.5, alpha = 0.5)
axes[2].set_title('bar')

axes[3].fill_between(x, x**2, x**3, color = 'green', alpha = 0.5)
axes[3].set_title('fill_between')

#%% Histogramas
n = np.random.randn(100000)
fig, axes = plt.subplots(1,2,figsize = (12,4))

axes[0].hist(n)
axes[0].set_title('Histograma Padrão')
axes[0].set_xlim(min(n), max(n))

axes[1].hist(n, cumulative=True, bins = 50)
axes[1].set_title('Histograma Cumulativo')
axes[1].set_xlim(min(n), max(n))

#%% Color Map
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return (+ alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p))

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
x, y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(x, y).T

fig, ax = plt.subplots()

p = ax.pcolor(x/(2**np.pi), y/(2*np.pi), Z, cmap=cm.RdBu, vmin=np.abs(Z).min(), vmax=np.abs(Z).max())
cb = fig.colorbar(p, ax=ax)

#%% Grafico 3D
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure(figsize = (14,6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(x, y, Z, rstride=4, cstride=4, linewidth =0)

ax = fig.add_subplot(1, 2, 2, projection = '3d')
p = ax.plot_surface(x, y, Z, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)

# Wire frame
fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(1,1,1, projection = '3d')
p = ax.plot_wireframe(x, y, Z, rstride=4, cstride=4)

# Countour plot com projecao
fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(1,1,1, projection = '3d')

ax.plot_surface(x, y, Z, rstride=4, cstride = 4, alpha = 0.25)
cset = ax.contour(x, y, Z, zdir='z', offset=-np.pi, cmap=cm.coolwarm)
cset = ax.contour(x, y, Z, zdir='x', offset=-np.pi, cmap=cm.coolwarm)
cset = ax.contour(x, y, Z, zdir='y', offset=3*np.pi, cmap=cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi)
ax.set_xlim3d(0, 3*np.pi)
ax.set_xlim3d(-np.pi, 2*np.pi)