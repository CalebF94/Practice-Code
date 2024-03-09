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


# Philly data isolated
phi_gm_stats= (team_stats[(team_stats['teamAbbr']=='PHI') & (team_stats['seasTyp']=='Regular')]
               .loc[:,['gmDate',
                      'teamPTS',
                      'teamTRB',
                      'teamAST',
                      'teamTO',
                      'opptPTS']
                      ]
                .sort_values('gmDate'))

phi_gm_stats['game_num'] = range(1, len(phi_gm_stats)+1)

#Add a win loss column
win_loss = []
for _, row in phi_gm_stats.iterrows():

    #If sixers score more than their opponents then W
    if row['teamPTS'] > row['opptPTS']:
        win_loss.append('W')
    else:
        win_loss.append('L')

phi_gm_stats['winLoss'] = win_loss


#Isolate relevant data for 76ers Scatter Plots
phi_gm_stats_2 = (team_stats[(team_stats['teamAbbr'] == 'PHI') &
                             (team_stats['seasTyp'] == 'Regular')]
                 .loc[:, ['gmDate',
                          'team2P%',
                          'team3P%',
                          'teamPTS',
                          'opptPTS']]
                 .sort_values('gmDate'))

# Add game number
phi_gm_stats_2['game_num'] = range(1, len(phi_gm_stats_2) + 1)

# Derive a win_loss column
win_loss = []
for _, row in phi_gm_stats_2.iterrows():

    # If the 76ers score more points, it's a win
    if row['teamPTS'] > row['opptPTS']:
        win_loss.append('W')
    else:
        win_loss.append('L')

# Add the win_loss data to the DataFrame
phi_gm_stats_2['winLoss'] = win_loss