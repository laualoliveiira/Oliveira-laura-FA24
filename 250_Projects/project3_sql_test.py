#%%
import pandas as pd 
import numpy as np
import sqlite3

# %%
# careful to list your path to the file or save it in the same place as your .qmd or .py file
sqlite_file = 'lahmansbaseballdb.sqlite'
con = sqlite3.connect(sqlite_file)

q = 'SELECT * FROM allstarfull LIMIT 5'
results = pd.read_sql_query(q,con)

results
#%%
q = '''
    SELECT * 
    FROM sqlite_master 
    WHERE type='table'
    '''
table = pd.read_sql_query(q,con)
table.filter(['name'])
# %%
