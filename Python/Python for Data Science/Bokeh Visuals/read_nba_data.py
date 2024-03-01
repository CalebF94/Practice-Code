import pandas as pd

player_stats = pd.read_csv('data/2017-18_playerBoxScore.csv',
                           parse_dates=['gmDate'])

team_stats = pd.read_csv('data/2017-18_teamBoxScore.csv',
                         parse_dates=['gmDate'])

standings = pd.read_csv('data/2017-18_standings.csv',
                        parse_dates=['stDate'])

# print(f'Shape of player_stats: {player_stats.shape}\n')
# print(f'Shape of team_stats: {team_stats.shape}\n')
# print(f'Shape of standings: {standings.shape}\n')

# west_top_2
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
              .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
              .sort_values(['teamAbbr', 'stDate']))
