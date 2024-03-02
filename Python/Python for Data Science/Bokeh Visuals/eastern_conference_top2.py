from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Import data
from read_nba_data import *

output_file('East_top_2_standings_race.html',
            title = 'Eastern Confernce Top 2 Teams Wins Race')


standings_cds=ColumnDataSource(standings)

# create view for each team
celtics_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='BOS'))
raptors_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='TOR'))

east_fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Western Conference Top 2 Teams Wins Race 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None
             )

# Render the race as step lines
east_fig.step(x='stDate', y='gameWon',
         color = '#007A33', legend_label='Celtics',
         source = standings_cds, view=celtics_view)

east_fig.step(x='stDate', y='gameWon',
         color = '#CE1141', legend_label='Raptors',
         source = standings_cds, view=raptors_view)

# move legend
east_fig.legend.location = 'top_left'

show(east_fig)