# %%
import pandas as pd

def read():
    towns = []
    state = ""
    with open('data-sets/university_towns.txt', mode='r') as file:
        for line in file:
            if "[edit]" in line:
                state = line.strip()
            else:
                towns.append([state, line])

    towns = pd.DataFrame(towns, columns=["state", "city"])
    return towns

towns = read()
towns.to_csv("data-sets/towns.csv")


# %%
# This cell goes beyond what was covered in the video
state=towns.loc[:, "state"] = towns["state"].str.split("[", expand=True).loc[:, 0]
city = towns["city"].str.split("(", expand=True).loc[:, 0].str.split(")", expand=True).loc[:, 0].str.replace('"', '').str.strip()
college = towns["city"].str.split("(", expand=True).loc[:, 1].str.split(")", expand=True).loc[:, 0]
towns2 = pd.DataFrame(data = {'state': state, 'city': city, 'college': college})
towns2.to_csv("towns2.csv", sep=";", quoting=False)


# %%
# checking whether all states contain the string [edit]
towns.loc[:, 'state'].str.contains("\[edit\]").all()


# %%
import pandas as pd

def read():
    return pd.read_csv("data-sets/towns.csv", index_col=0).assign(
        state = lambda df: df.loc[:, "state"].str.removesuffix("[edit]"),
        city = lambda df: df.loc[:, 'city'].str.extract(r"(.+) \(.*") # Using Regex to find  _( and returns the first capture group
    )

towns = read()
# %%
