
# %%
import pandas as pd

# This cell simply creates a function out the eda cell at the bottom of the notebook
def clean_date_of_publication(books):
    return pd.to_numeric(
        books.loc[:, 'date_of_publication'].str.extract(
            r"(\d{4})", # this is extracting the series of four consecutive digits i.e the year
            expand = False #without this line pd.extract will return a dataframe. We need a series
        ).fillna(0), # this fills the na values with a 0
        downcast="unsigned" # this reduces the size of the series by changing type of the integer used
    ) 

def clean_place_of_publication(books):
    return (
        books.loc[:, "place_of_publication"]
        .str.replace(r".*London.*", "London", regex=True)
        .str.replace(r".*Plymouth.*", "Plymouth", regex=True)
        .str.replace(r".*Oxford.*", "Oxford", regex=True)
        .str.replace(r"-", " ", regex=True)
)

def read():
    return (
        # making column names lower case and changing the column name for the id field
        pd.read_csv("data-sets\BL-Flickr-Images-Book.csv")
        .rename(columns = lambda header: header.lower().replace(" ","_"))
        .rename(columns={"identifier": "id"})
        #Dropping/removing unneeded columns. Just list columns to drop inside a list
        .drop(
            columns=[
                'edition_statement', 
                'contributors',
                'corporate_author', 
                'corporate_contributors', 
                'former_owner',
                'engraver', 
                'issuance_type', 
                'shelfmarks'
            ]
        )
        #id is the unique identifier for this data set (books.loc[:, 'id'].is_unique returns True)
        .set_index("id")
        .assign(
            date_of_publication= clean_date_of_publication,
            place_of_publication = clean_place_of_publication
            )
    )

books = read()

# %%
#eda cell
# we're going to be working on the date aof publication field

#note that some of the dates are na
print(f'Total number of na values in the "date_of_publication" field is {books.loc[:, "date_of_publication"].isna().sum()}')

pd.to_numeric(
    books.loc[:, 'date_of_publication'].str.extract(
        r"(\d{4})", # this is extracting the series of four consecutive digits i.e the year
        expand = False #without this line pd.extract will return a dataframe. We need a series
    ).fillna(0), # this fills the na values with a 0
    downcast="unsigned" # this reduces the size of the series by changing type of the integer used
)


# %%
#eda cell number 2

#books with dashes in the name
books.loc[books.loc[:, 'place_of_publication'].str.contains("-"), 'place_of_publication']

#This code will be used to define a function at the beginning of the top block
(books.loc[:, "place_of_publication"]
 .str.replace(r".*London.*", "London", regex=True)
 .str.replace(r".*Plymouth.*", "Plymouth", regex=True)
 .str.replace(r".*Oxford.*", "Oxford", regex=True)
 .str.replace(r"-", " ", regex=True)
)
# %%
