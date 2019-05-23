# divisão de telas

from os import path
import pandas as pd
import matplotlib.pyplot as plt

basepath = path.abspath(path.dirname(__file__))
path = path.join(basepath, '../../dados/trees.csv')
base = pd.read_csv(path)

plt.figure(1)

# girth com volume
plt.subplot(2,2,1)
help(plt.subplot)
plt.scatter(base.Girth, base.Volume)

# girth com height
plt.subplot(2,2,2)
help(plt.subplot)
plt.scatter(base.Girth, base.Height)

# height com volume
plt.subplot(2,2,3)
help(plt.subplot)
plt.scatter(base.Height, base.Volume)

# histograma volume
plt.subplot(2,2,4)
help(plt.subplot)
plt.hist(base.Volume)
