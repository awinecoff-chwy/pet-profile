
# %%Vertica Connetion Test
import os
import database_conn
import pandas as pd
import vertica_python
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

print ('import complete')


# %%Set python connection variable
connection = vertica_python.connect(**database_conn.bidb.copy()) 

#test_query_count = pd.read_sql('''
#                          select distinct c.party_chewy_id from custods.party_customer c 
#                          inner join chewybi.customers bi on bi.customer_id = c.party_chewy_id
#                          ''', connection).count()

## %%
##count all distinct customers
#all_customers_count = pd.read_sql ('''
#                               SELECT COUNT(DISTINCT customer_master_id)
#                               FROM chewybi.customers
#                               ''', connection).iloc[0]['COUNT']
#
##count only customers that have at least one petprofile
#petprofile_customers_count = pd.read_sql ('''
#                               SELECT COUNT(DISTINCT petprofile_customer_master_id)
 #                              FROM integrate.customer_petprofile_ps
 #                             ''', connection).iloc[0]['COUNT']

pet_customer_query = open('../sql/pet_customer_basic.sql')
pet_customer_df = pd.read_sql_query(pet_customer_query.read(),connection)

food_allergy_query = open('../sql/pet_food_allergy_long.sql') 
food_allergy_df = pd.read_sql_query(food_allergy_query.read(),connection)

med_allergy_query = open('../sql/pet_med_allergy_long.sql') 
med_allergy_df = pd.read_sql_query(med_allergy_query.read(),connection)

med_condition_query = open('../sql/pet_med_condition_long.sql') 
med_condition_df = pd.read_sql_query(med_condition_query.read(),connection)

medication_query = open('../sql/pet_medication_long.sql') 
medication_df = pd.read_sql_query(medication_query.read(),connection)

usa = gpd.read_file(os.getcwd() + '/states_21basic/states.shp')
usa = usa[['STATE_ABBR', 'SUB_REGION', 'STATE_FIPS', 'geometry']]
usa.columns = ['us_state', 'us_subregion', 'state_fips', 'geometry']

#pet_customer_df = pet_customer_df.join(usa,  on='us_state', how='left')
pet_customer_df = pd.merge(pet_customer_df, usa, on='us_state', how='left')

#Convert all profile characteristics to wide format so they can be added as binary variables to the basic pet info table
food_allergy_wide = food_allergy_df.pivot(index='pet_id', columns='pet_allergy_nm', values='food_allergy')
food_allergy_wide.columns = ['fa_' + str(c).lower() for c in food_allergy_wide]
food_allergy_wide = food_allergy_wide.reset_index()

med_allergy_wide = med_allergy_df.pivot(index='pet_id', columns='pet_med_allergy_nm', values='med_allergy')
med_allergy_wide.columns = ['ma_' + str(c).lower() for c in med_allergy_wide]
food_allergy_wide = med_allergy_wide.reset_index()

med_condition_wide = med_condition_df.pivot(index='pet_id', columns='pet_med_condition_nm', values='med_condition')
med_condition_wide.columns = ['mc_' + str(c).lower() for c in med_condition_wide]
med_condition_wide = med_condition_wide.reset_index()


medication_wide = medication_df.pivot(index='pet_id', columns='pet_med_nm', values='medication')
medication_wide.columns = ['m_' + str(c).lower() for c in medication_wide]
medication_wide = medication_wide.reset_index()


#food_allergy_wide.columns = ['fa_' + str(c).lower() for c in food_allergy_wide].reset_index()
#food_allergy_wide = food_allergy_wide.reset_index()

#Convert all profile characteristics to wide format so they can be added as binary variables to the basic pet info table

#med_allergy_wide.columns = ['ma_' + str(c).lower() for c in med_allergy_wide].reset_index()
#med_allergy_wide = med_allergy_wide.reset_index()

conversion_list = [
        {'df': food_allergy_wide, 'col_name':'pet_allergy_nm', 'vals':'food_allergy', 'prefix':'fa_'},
        {'df': med_allergy_wide, 'col_name':'pet_med_allergy_nm', 'vals':'med_allergy', 'prefix':'ma_'},
        {'df': food_allergy_wide, 'col_name':'pet_med_condition_nm', 'vals':'med_condition', 'prefix':'mc_'},
        {'df': medication_wide, 'col_name':'pet_med_nm', 'vals':'medication', 'prefix':'mc_'},       
        ]

for convert in conversion_list:
#    df = convert['df']
    

#
##don't know if this is the best source for this
#products_count = pd.read_sql ('''
#                               SELECT COUNT(DISTINCT product_part_number)
#                               FROM chewybi.products
#                               ''', connection).iloc[0]['COUNT']
#
##don't know if this is the best source for this
#products_pharmacy_count = pd.read_sql ('''
#                               SELECT COUNT(DISTINCT product_part_number)
#                               FROM chewybi.products_pharmacy
#                               ''', connection).iloc[0]['COUNT']
#
#
#petprofile_pet_count = pd.read_sql ('''
#                               SELECT COUNT(DISTINCT party_chewy_id)
#                               FROM custods.party_pet
#                               ''', connection).iloc[0]['COUNT']
#
    
#cust_location = cust_address[['customer_id', 'us_state', 'region']]
#
##cust_prod_joined = pet_cust.set_index('petprofile_customer_id').join(cust_products.set_index('customer_id'), how='inner').join(location.set_index('customer_id'), how='left')
#
