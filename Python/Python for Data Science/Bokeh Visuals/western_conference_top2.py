from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Import data
from read_nba_data import *

output_file('west_top_2_standings_race.html',
            title = 'Western Confernce Top 2 Teams Wins Race')

# isolate data for each team
rockets_data = west_top_2[west_top_2[:, 'teamAbbr']=='HOU']
warriors_data = west_top_2[west_top_2[:, 'teamAbbr']=='GS']

# Create a column data source
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Western Conference Top 2 Teams Wins Race 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None
             )

# Render the race as step lines
fig.step(x='stDate', y='gameWon',
         color = '#CE1141', legend='Rockets',
         source = rockets_cds)

fig.step(x='stDate', y='gameWon',
         color = '#006BB6', legend='Warriors',
         source = warriors_cds)

# move legend
fig.legend.location = 'top_left'

show(fig)