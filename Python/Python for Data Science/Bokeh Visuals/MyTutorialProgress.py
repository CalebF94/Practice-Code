# Importing the needed libraries
import numpy as np
from bokeh.io import output_file
from bokeh.plotting import figure, show
# My work count data
day_num = np.linspace(1, 10, 10)
daily_words = [450,628,488,210,287,791,508,639,397,943]
cumulative_words = np.cumsum(daily_words)

output_file('my_tutorial_progress.html', title='My Tutorial Progress')

# Setting up our graph
fig = figure(title='My Tutorial Progress',
             height=400, width=700,
             x_axis_label='Day Number', y_axis_label='Words Written',
             x_minor_ticks=2, y_range=(0,6000),
             toolbar_location=None
             )

# Daily words will be shown as bars
fig.vbar(x=day_num, bottom=0, top=daily_words, color='blue', width=0.75, legend_label='Daily')

# Adding a second element; a line for cumulative words
fig.line(x=day_num, y=cumulative_words, color='gray', line_width=1, legend_label='Cumulative')

fig.legend.location = 'top_left'

show(fig)