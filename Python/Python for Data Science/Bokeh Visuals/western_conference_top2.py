from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Import data
from read_nba_data import *

output_file('west_top_2_standings_race.html',
            title = 'Western Confernce Top 2 Teams Wins Race')

## This was the process used in video 3
# isolate data for each team
# rockets_data = west_top_2[west_top_2[:, 'teamAbbr']=='HOU']
# warriors_data = west_top_2[west_top_2[:, 'teamAbbr']=='GS']

#  #Video 3: Created two column data sources and
# rockets_cds = ColumnDataSource(rockets_data)
# warriors_cds = ColumnDataSource(warriors_data)

## This is the process using Groupfilter and CDS view from video 4
west_cds=ColumnDataSource(west_top_2)

# create view for each team
rockets_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='HOU'))
warriors_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='GS'))

west_fig = figure(x_axis_type='datetime',
             height=300, width=600,
             title='Western Conference Top 2 Teams Wins Race 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None
             )

# Render the race as step lines from video 3
# west_fig.step(x='stDate', y='gameWon',
#          color = '#CE1141', legend='Rockets',
#          source = rockets_cds)

# west_fig.step(x='stDate', y='gameWon',
#          color = '#006BB6', legend='Warriors',
#          source = warriors_cds)

# From Video 4
west_fig.step(x='stDate', y='gameWon',
         color = '#CE1141', legend_label='Rockets',
         source = west_cds, view=rockets_view)

west_fig.step(x='stDate', y='gameWon',
         color = '#006BB6', legend_label='Warriors',
         source = west_cds, view=warriors_view)

# move legend
west_fig.legend.location = 'top_left'

show(west_fig)