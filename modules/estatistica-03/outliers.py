import os
import os.path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyod.models.knn import KNN

path = os.path.abspath('.')

iris = pd.read_csv(os.path.join(path, 'dados\\iris.csv'))
print(iris)

plt.boxplot(iris.iloc[:, 1], showfliers=True)
outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1)]

sepal_width = np.array(iris.iloc[:, 1])
sepal_width = sepal_width.reshape(-1, 1)

detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_
print(previsoes)
plt.plot(detector.labels_)