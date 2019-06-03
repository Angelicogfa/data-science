#%% !pip install bokeh -U --user
import bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnarDataSource
from bokeh.transform import factor_cmap
# from bokeh.palettes import Spectral16

#%% Grafico de linha
output_notebook()
output_file("Bokeh-Grafico-Interativo.html")
p = figure()

type(p)

p.line([1,2,3,4,5], [6,7,2,4,5], line_width = 2)
show(p)

#%% Grafico de barras
output_file("Bokeh-Grafico-Barras.html")

fruits = ['Maças', 'Peras', 'Tangerinas', 'Uvas', 'Melancias', 'Morangos']
counts = [5,3,4,2,4,6]

source = ColumnarDataSource(data=dict(fruits = fruits, counts = counts))

p = figure(x_range = fruits, plot_height = 350, toolbar_location=None, title = 'Contagem de frutas')

p.vbar(x='fruits',
       top = 'counts',
       width = 0.9,
       source = source,
       legend = 'fruits',
       line_color = 'white',
       fill_color = factor_cmap('fruits', palette=None, factors=fruits))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 9
p.legend.orientation = 'horizontal'
p.legend.location = 'top_center'
show(p)

#%% Construindo um scatter plot
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = 'Iris Morphology')
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers['petal_length'], flowers['petal_width'], color = colors, fill_alpha = 0.2, size = 10)
output_file('Bokeh_grafico_iris.html', title= 'iris.py exemplo')
show(p)
