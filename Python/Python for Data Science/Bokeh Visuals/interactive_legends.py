from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row

#import data
from read_nba_data import player_stats

#Create an output html file
output_file('lebron_vs_durant.html',
            title='Lebron James vs. Kevin Durant')

#store the data in a ColumnDataSource
player_gm_stats = ColumnDataSource(player_stats)

#Create a view for each player
lebron_filters = [GroupFilter(column_name='playFNm', group="LeBron"), 
                  GroupFilter(column_name='playLNm', group='James')]

lebron_view = CDSView(source=player_gm_stats,
                      filter=lebron_filters)


durant_filters = [GroupFilter(column_name='playFNm', group="Kevin"), 
                  GroupFilter(column_name='playLNm', group='Durant')]

durant_view = CDSView(source=player_gm_stats,
                      filter=durant_filters)


#consolidate the common keyword args in dicts
common_figure_kwargs = {
    'width': 400,
    'x_axis_label': 'Points',
    'toolbar_location': None
}

common_circle_kwargs = {
    'x': 'playPTS',
    'y': 'playTRB',
    'source': player_gm_stats,
    'size': 12,
    'alpha': 0.7
}

common_lebron_kwargs = {
    'view': lebron_view,
    'color': '#002859',
    'legend_label': 'Lebron James'
}

common_durant_kwargs = {
    'view': durant_view,
    'color': '#FFC324',
    'legend_label': 'Kevin Durant'
}


# Create the two figures
hide_fig = figure(**common_figure_kwargs,
                  title='Click Legend to HIDE data',
                  y_axis_label='Rebounds')

hide_fig.circle(**common_circle_kwargs, **common_lebron_kwargs)
hide_fig.circle(**common_circle_kwargs, **common_durant_kwargs)


mute_fig = figure(**common_figure_kwargs,
                  title='Click Legend to MUTE data',
                  y_axis_label='Rebounds')

mute_fig.circle(**common_circle_kwargs, **common_lebron_kwargs, muted_alpha=0.1)
mute_fig.circle(**common_circle_kwargs, **common_durant_kwargs, muted_alpha=0.1)

#Add Interactivity
hide_fig.legend.click_policy = 'hide'
hide_fig.legend.click_policy = 'mute'

show(row(hide_fig, mute_fig))