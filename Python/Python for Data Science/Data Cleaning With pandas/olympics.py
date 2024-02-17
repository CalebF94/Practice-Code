# Video 3: Exploring the Olympic Data

# %%
import pandas as pd

def read():
    return pd.read_csv("data-sets/olympics.csv", header=1).rename(columns={
        "Unnamed: 0": "country",
        "? Summer": "summer_olympics",
        "01 !": "summer_golds",
        "02 !": "summer_silvers",	
        "03 !": "summer_bronze",
        "Total": "summer_total",
        "? Winter": "winter_olympics",
        "01 !.1": "winter_golds",
        "02 !.1": "winter_silvers",	
        "03 !.1": "winter_bronze",
        "Total.1": "winter_total",
        "? Games": "total_games",
        "01 !.2": "total_golds",
        "02 !.2": "total_silvers",	
        "03 !.2": "total_bronze",
        "Combined total": "combined_total",

    })

olympics = read()

# %%
# using the location indexer to return rows. Inclusive
olympics.loc[0:5]


# %%
united_countries =olympics.loc[:, 'country'].str.contains('United')
olympics.loc[united_countries, :]
# %%
