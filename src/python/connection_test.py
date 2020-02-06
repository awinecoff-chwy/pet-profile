
# %%Vertica Connetion Test
import os
import database_conn
import pandas as pd
import vertica_python

print ('import complete')


# %%Set python connection variable
connection = vertica_python.connect(**database_conn.bidb.copy()) 

## use the following to load records from vertica in pd df:
test= pd.read_sql('''select * from chewybi.product_attributes limit 10''', connection)
test.head()


# %%

