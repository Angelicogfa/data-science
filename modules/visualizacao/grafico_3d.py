from os import path
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

basepath = path.abspath(path.dirname(__file__))
path = path.join(basepath, '../../dados/orchard.csv')
base = pd.read_csv(path)

figura = plt.figure()
eixo = figura.add_subplot(1, 1, 1, projection = '3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_x_label('decrease')
eixo.set_y_label('rowpos')
eixo.set_z_label('colpos')