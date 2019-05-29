#%% Leitura de imagem como vetor
from os import path
from scipy import misc
import matplotlib.pyplot as plt

diretorio = path.abspath('.')
arquivo = path.join(diretorio, 'dados\\Matplotlib-Mapa.png')

misc.imread(arquivo)
plt.imread(arquivo)


#%% integração Numerica
import numpy as np
from scipy.integrate import quad, dblquad, tplquad

val, abserr = quad(lambda x: np.exp(-x ** 2), np.Inf, np.Inf)
val, abserr

from scipy.integrate import odeint, ode

def dy(y, t, zeta, w0):
    x, p = y[0], y[1]

    dx = p
    dp = -2 * zeta * w0 * p - w0**2 * x
    return [dx, dp]

y0 = [1.0, 0.0]

t = np.linspace(0, 10, 1000)
w0 = 2 * np.pi * 1.0

y1 = odeint(dy, y0, t, args=(0.0, w0))
y2 = odeint(dy, y0, t, args=(0.2, w0))
y3 = odeint(dy, y0, t, args=(1.0, w0))
y4 = odeint(dy, y0, t, args=(5.0, w0))

fig, ax = plt.subplots()
ax.plot(t, y1[:, 0], 'k', label='Não Abafado', linewidth = 0.25)
ax.plot(t, y2[:, 0], 'r', label='Pouco Abafado')
ax.plot(t, y3[:, 0], 'w', label='Criticamente Abafado')
ax.plot(t, y4[:, 0], 'g', label='Perigiosamente Abafado')
ax.legend()


#%% Fourier Transformation
import scipy.fftpack as fft

N = len(t)
dt = t[1] - t[0]

F = fft.fft(y2[:, 0])

w = fft.fftfreq(N, dt)

fig, ax = plt.subplots(figsize = (9,3))
ax.plot(w, np.abs(F))

#%% Algebra Linear
import scipy.linalg as lin
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([1,2,3])

# Resolvendo um sistema de equação linear
x = lin.solve(A, B)
x

A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

evals, evecs = lin.eig(A)
evals
evecs
lin.svd(A)

#%% Otimização
from scipy import optimize

def f(x):
    return 4 * x **3 + (x - 2)**2 + x ** 4

fig, ax = plt.subplots()
x = np.linspace(-5, 3, 100)
ax.plot(x, f(x))

x_min = optimize.fmin(f, -0.5)
x_min


#%% Estatistica
from scipy import stats

Y = stats.norm()
x = np.linspace(-5,5,100)

fig, axes = plt.subplots(3, 1, sharex=True)
axes[0].plot(x, Y.pdf(x))
axes[1].plot(x, Y.cdf(x))
axes[2].hist(Y.rvs(size=1000), bins = 50)
Y.mean(), Y.std(), Y.var()

#%% T-test
t_statistic, p_value = stats.ttest_ind(Y.rvs(size = 1000), Y.rvs(1000))
t_statistic, p_value