

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CDSView, GroupFilter, TabPanel, Tabs
#from bokeh.models.widgets import Tabs, Panel # Depracated

# Import data
from read_nba_data import *

output_file('East_west_top_2_tabbed.html',
            title = 'Confernce Top 2 Teams Wins Race')


standings_cds=ColumnDataSource(standings)

# create view for each team
celtics_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='BOS'))
raptors_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='TOR'))
rockets_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='HOU'))
warriors_view = CDSView(filter=GroupFilter(column_name='teamAbbr', group='GS'))


# Create figure for eastern teams
east_fig = figure(x_axis_type='datetime',
             height=300,
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


#make western conference graph
west_fig = figure(x_axis_type='datetime',
             height=300,
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None
             )

west_fig.step(x='stDate', y='gameWon',
         color = '#CE1141', legend_label='Rockets',
         source = standings_cds, view=rockets_view)

west_fig.step(x='stDate', y='gameWon',
         color = '#006BB6', legend_label='Warriors',
         source = standings_cds, view=warriors_view)

# move legend
west_fig.legend.location = 'top_left'

# Increase width of both figs
west_fig.width = east_fig.width = 800

# Create two panels, one for each conference
east_panel = TabPanel(child=east_fig, title='Eastern Conference')
west_panel = TabPanel(child=west_fig, title='Western Conference')

#Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

#show(column(west_fig, east_fig))
show(tabs)