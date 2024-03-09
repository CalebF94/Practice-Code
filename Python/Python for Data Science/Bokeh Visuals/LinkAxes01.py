# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Div
from bokeh.layouts import gridplot, column

# load in data
from read_nba_data import phi_gm_stats

output_file('phi_gm_linked_stats.html',
             title='76ers Game Log')

# store the data in a ColumnDataSource
gm_stats_cds = ColumnDataSource(phi_gm_stats)

# Create a CategoricalColorMapper that assigns a color to wins and losses
win_loss_mapper = CategoricalColorMapper(factors=['W', 'L'],
                                         palette = ['green', 'red'])

# Create a dict with the stat name and its corresponding column in the data
stat_names = {'Points': 'teamPTS',
              'Assists': 'teamAST',
              'Rebounds': 'teamTRB',
              'Turnovers': 'teamTO'}

#The figure for each will be held in this dict
stat_figs ={}

# For each stat in the stat_names dict
for stat_label, stat_col in stat_names.items():

    #create a figure
    fig = figure(y_axis_label=stat_label,
                 height=200, width=400, 
                 x_range=(1, 10), 
                 tools=['xpan', 'reset', 'save'])
    
    #configure vbar
    fig.vbar(x='game_num', bottom=0, top=stat_col, source=gm_stats_cds, width=0.9, color=dict(field='winLoss', transform=win_loss_mapper))
    
    #store the figure in the stat_figs dictionary
    stat_figs[stat_label] = fig

#create layout
grid = gridplot([[stat_figs['Points'], stat_figs['Assists']],
                 [stat_figs['Rebounds'], stat_figs['Turnovers']]])

#Link together the x-axes. the slash continues the line
stat_figs['Points'].x_range = \
stat_figs['Assists'].x_range = \
stat_figs['Rebounds'].x_range = \
stat_figs['Turnovers'].x_range

#Add a title for the entire visualization. This is just a long html string
html = """<h3>Philadelphia 76ers Game Log</h3>
<b><i>2017-18 Regular Season</i></b>
<br>
<i>Wins in Green, Losses in Red"""

sup_title = Div(text=html)

show(column(sup_title, grid))