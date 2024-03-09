# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, NumeralTickFormatter, Range1d
from bokeh.layouts import gridplot

# load in data
from read_nba_data import phi_gm_stats_2

output_file('phi_gm_linked_selections.html',
             title='76ers Percentages vs. Win-Loss')

# store the data in a ColumnDataSource
gm_stats_cds = ColumnDataSource(phi_gm_stats_2)

# Create a CategoricalColorMapper that assigns a color to wins and losses
win_loss_mapper = CategoricalColorMapper(factors=['W', 'L'],
                                         palette = ['green', 'red'])


toolList = ['lasso_select', 'tap', 'reset', 'save']

pctFig = figure(title='2PT FG % vs 3PT FG %, 17-18 Regular Season',
                height=400, width=400, tools=toolList,
                x_axis_label='2PT FG%', y_axis_label='3PT FG%')

# draw circle
pctFig.circle(x='team2P%', y='team3P%', source=gm_stats_cds,
              size=12, color='black')

pctFig.xaxis[0].formatter = NumeralTickFormatter(format='00.0%')
pctFig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

totFig = figure(title='Team Points vs Opp points, 17-18 Regular Season',
                height=400, width=400, tools=toolList,
                x_axis_label='Team Points', y_axis_label='Opp Points')


totFig.square(x='teamPTS', y='opptPTS', source=gm_stats_cds,
              size=10, 
              color=dict(field='winLoss', transform=win_loss_mapper))


#above line is loss, below line is win
totFig.line([1, 200], [1, 200])
totFig.x_range =totFig.y_range =  Range1d(80,140)


grid = gridplot([[pctFig, totFig]])

show(grid)

