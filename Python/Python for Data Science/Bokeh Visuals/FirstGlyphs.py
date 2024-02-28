# import needed bokeh packages
from bokeh.io import output_file
from bokeh.plotting import figure, show

#my x,y coordinates
x = [1,2,1]
y = [1,1,2]

# output the visualization to a static HTML file
output_file('first_glyphs.html', title='First Glyphs')

fig = figure(title = 'My Coordinates',
             height = 300, width=300,
             x_range=(0, 3), y_range=(0,3),
             toolbar_location = 'above'
             )

# Draw the coordinates as circles
fig.circle(x=x, y=y,
           color='green', size=10, alpha=0.5
           )

show(fig)