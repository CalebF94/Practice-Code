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

# Find players who took atleast 1 three-point shot during the season
three_takers = player_stats[player_stats['play3PA']>0]

#clean up the player name, placing them in a single column
three_takers['name'] = [f'{p["playFNm"]} {p["playLNm"]}' for _, p in three_takers.iterrows()] #_ corresponds to the index returned by iterrows

# Aggregate the total three point attempts and makes by each player
three_takers = (three_takers.groupby('name')
                 .sum(numeric_only = True)
                 .loc[:, ['play3PA', 'play3PM']]
                 .sort_values('play3PA', ascending=False))

#filter out anyone who didn't take at least 100 three-point shots
three_takers = three_takers[three_takers['play3PA']>=100]

# add column for 3Pt%
three_takers['pct3PM'] = three_takers['play3PM']/three_takers['play3PA']


