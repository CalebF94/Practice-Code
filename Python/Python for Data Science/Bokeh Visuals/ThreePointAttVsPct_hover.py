# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter, HoverTool

# Import data
from read_nba_data import three_takers

#output to a file
output_file('three_point_att_vs_pct.html',
            title='Three-Point Attempts vs. Percentage')

#Store data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

#Specify the selection tools to be made available
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Format the tooltip from video 4
tooltips = [
    ('Player', '@name'), #label will be 'Player' and it will the name field
    ('Three-Pointers Made', '@play3PM'),
    ('Three-Pointers Attempted', '@play3PA'),
    ('Three-Point Percentage', '@pct3PM{00.0%}')]

#create the figure
fig = figure(height=400, width=600,
             x_axis_label = 'Three Point Shots Attempted',
             y_axis_label = 'Percentage Made',
             title = '3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-2018',
             toolbar_location = 'below',
             tools=select_tools)

# add the hovertool to the figure
fig.add_tools(HoverTool(tooltips=tooltips))

# Format the y-axis label as percentages
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# add square representing each player
fig.square(
    x='play3PA',
    y='pct3PM',
    source=three_takers_cds,
    color='royalblue',
    selection_color='deepskyblue',
    nonselection_color='lightgray',
    nonselection_alpha=0.3
)

show(fig)