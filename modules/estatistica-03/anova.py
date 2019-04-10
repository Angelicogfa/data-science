import pandas as pd
import os
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(my_path, '../../dados/iris.csv')
registros = pd.read_csv(path)
print(registros)

 