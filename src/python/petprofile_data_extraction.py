
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
usa.head()
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
#pet_cust = pd.read_sql('''
#                       SELECT pets.party_chewy_id                                       AS pet_id, 
#                               pt.pet_type_nm, 
#                               pets.pet_nm, 
#                               pets.gender_cd, 
#                               pb.pet_breed_nm, 
#                               pb.size_cd                                                AS breed_size, 
#                               pets.size_type_cd                                         AS pet_size, 
#                               pets.birth_dt, 
#                               Datediff(dd, pets.birth_dt, Getdate())                    AS 
#                               pet_age_in_days, 
#                               Round(Datediff(dd, pets.birth_dt, Getdate()) / 365.25, 2) AS 
#                               pet_age_in_years, 
#                               pets.life_stage_cd, 
#                               pets.weight, 
#                               pets.weight_type_cd, 
#                               pets.create_dt, 
#                               pets.update_dt, 
#                               pc_int.petprofile_id, 
#                               pc_int.petprofile_master_id, 
#                               pc_int.petprofile_customer_id, 
#                               pc_int.petprofile_customer_master_id, 
#                               pc_int.petprofile_status                                  AS 
#                               profile_status, 
#                               ( CASE 
#                                   WHEN pc_int.petprofile_status = 0 THEN 'inactive' 
#                                   WHEN pc_int.petprofile_status = 1 THEN 'active' 
#                                   WHEN pc_int.petprofile_status = 2 THEN 'deleted' 
#                                   WHEN pc_int.petprofile_status = 3 THEN 'verified' 
#                                   WHEN pc_int.petprofile_status = 4 THEN 'cancelled' 
#                                   ELSE 'unknown' 
#                                 END )                                                   AS 
#                               profile_status_desc, 
#                               pc_int.petprofile_status_reason                           AS 
#                               profile_status_reason, 
#                               ( CASE 
#                                   WHEN pc_int.petprofile_status_reason = 0 THEN 'deceased' 
#                                   WHEN pc_int.petprofile_status_reason = 1 THEN 'switched retailer' 
#                                   WHEN pc_int.petprofile_status_reason = 2 THEN 'other' 
#                                   ELSE 'unknown' 
#                                 END )                                                   AS 
#                               profile_status_desc, 
#                               ad.customer_address_city, 
#                               ad.customer_address_state                                 AS us_state, 
#                               ad.customer_address_zip, 
#                               c_int.customer_full_name, 
#                               ad.customer_address_last_order_flag, 
#                               c_int.gross_average_order_value, 
#                               c_int.net_average_order_value, 
#                               c_int.customer_autoship_active_flag, 
#                               c_int.customer_order_shipped_consistency 
#                        FROM   custods.party_pet AS pets 
#                               LEFT JOIN custods.pet_type pt 
#                                      ON pt.pet_type_id = pets.pet_type_id 
#                               LEFT JOIN custods.pet_breed pb 
#                                      ON pb.pet_breed_id = pets.pet_breed_id 
#                               LEFT JOIN integrate.customer_petprofile_ps pc_int 
#                                      ON pc_int.petprofile_master_id = pets.party_chewy_id 
#                               LEFT JOIN integrate.customer_ps c_int 
#                                      ON pc_int.petprofile_customer_master_id = c_int.customer_master_id 
#                               LEFT JOIN chewybi.customer_addresses ad 
#                                      ON pc_int.petprofile_customer_id = ad.customer_id 
#                        WHERE  ad.customer_address_last_order_flag = 'true'; 
#                       ''', connection)
#
#
## ============================================================================= This may be wrong
## pet_cust = pd.read_sql('''
##                        SELECT cpp.petprofile_id, --customer, pet, profile base query
##                                cpp.petprofile_master_id, 
##                                pp.party_chewy_id   AS pet_party_chewy_id, 
##                                cpp.petprofile_customer_id, 
##                                cpp.petprofile_customer_master_id, 
##                                pc.party_chewy_id   AS customer_party_chewy_id, 
##                                pc.create_by        AS customer_create_by, 
##                                c.customer_full_name, 
##                                c.customer_registration_dttm, 
##                                pc.registration_dt  AS pc_registration_dt, 
##                                cpp.petprofile_petname, 
##                                pp.pet_nm           AS party_pet_name, 
##                                cpp.petprofile_pettype_id, 
##                                cpp.petprofile_pettype_description, 
##                                cpp.petprofile_petbreed_description, 
##                                cpp.petprofile_petbreed_size_type, 
##                                cpp.petprofile_gender, 
##                                cpp.petprofile_weight, 
##                                cpp.petprofile_size_type, 
##                                cpp.petprofile_birthday, 
##                                cpp.petprofile_birthday_estimated,
##                                DATEDIFF(DD, cpp.petprofile_birthday, GETDATE()) AS pet_age_in_days,
##                                ROUND(DATEDIFF(DD, cpp.petprofile_birthday, GETDATE())/365.25, 2) AS pet_age_in_years,
##                                cpp.petprofile_lifestage, 
##                                pc.source_system_id AS pc_source_system_id, 
##                                pp.source_system_id AS pp_source_system_id 
##                         FROM   integrate.customer_petprofile_ps cpp 
##                                LEFT JOIN custods.party_customer pc --may be able to remove this at some point. Right now this is here to both check alignment of userids and also because source_system_id is sometimes different for users' info and their associated pets' info
##                                       ON cpp.petprofile_customer_master_id = pc.party_chewy_id 
##                                LEFT JOIN custods.party_pet pp 
##                                       ON cpp.petprofile_master_id = pp.party_chewy_id 
##                                LEFT JOIN integrate.customer_ps c 
##                                       ON cpp.petprofile_customer_id = c.customer_id
##                         WHERE cpp.petprofile_pettype_description = 'Dog'
##                         ORDER BY cpp.petprofile_customer_id
##                         LIMIT 10000; 
##                         ''', connection)
## 
## 
## =============================================================================
#
#
##Need to create a separate one hot encoded column for each allergy
#pet_food_algy = pd.read_sql('''
#                            SELECT pets.party_chewy_id as ods_pet_id, 
#                                   allergies.pet_allergy_id, 
#                                   allergies.pet_allergy_nm, 
#                                   CASE 
#                                     WHEN pa.pet_allergy_id IS NOT NULL THEN 1 
#                                     ELSE 0 
#                                   end AS food_allergy 
#                            FROM   (SELECT DISTINCT pet_allergy_id, 
#                                                    pet_allergy_nm 
#                                    FROM   custods.pet_allergy) AS allergies 
#                                   CROSS JOIN (SELECT DISTINCT party_chewy_id 
#                                               FROM   custods.pet_allergy_rel) AS pets 
#                                              LEFT JOIN custods.pet_allergy_rel pa 
#                                                     ON allergies.pet_allergy_id = pa.pet_allergy_id 
#                                                        AND pets.party_chewy_id = pa.party_chewy_id 
#                            ORDER  BY pets.party_chewy_id, 
#                                      allergies.pet_allergy_id 
#                            LIMIT  10000; 
#                     
#                    ''' , connection)
#
##Need to create a separate one hot encoded column for each allergy
#pet_med_algy = pd.read_sql('''
#                           SELECT pets.party_chewy_id as ods_pet_id, 
#                                   allergies.pet_med_allergy_id, 
#                                   allergies.pet_med_allergy_nm, 
#                                   CASE 
#                                     WHEN pma.pet_med_allergy_id IS NOT NULL THEN 1 
#                                     ELSE 0 
#                                   end AS med_allergy 
#                            FROM   (SELECT DISTINCT pet_med_allergy_id, 
#                                                    pet_med_allergy_nm 
#                                    FROM   custods.pet_med_allergy) AS allergies 
#                                   CROSS JOIN (SELECT DISTINCT party_chewy_id 
#                                               FROM   custods.pet_med_allergy_rel) AS pets 
#                                              LEFT JOIN custods.pet_med_allergy_rel pma 
#                                                     ON allergies.pet_med_allergy_id = 
#                                                        pma.pet_med_allergy_id 
#                                                        AND pets.party_chewy_id = pma.party_chewy_id 
#                            ORDER  BY pets.party_chewy_id, 
#                                      allergies.pet_med_allergy_id 
#                            LIMIT  10000; 
# 
#                    ''' , connection)
#
#pet_med_cond = pd.read_sql('''
#                          SELECT pets.party_chewy_id, 
#                                   conditions.pet_med_condition_id, 
#                                   conditions.pet_med_condition_nm, 
#                                   CASE 
#                                     WHEN pmc.pet_med_condition_id IS NOT NULL THEN 1 
#                                     ELSE 0 
#                                   end AS med_condition 
#                            FROM   (SELECT DISTINCT pet_med_condition_id, 
#                                                    pet_med_condition_nm 
#                                    FROM   custods.pet_med_condition) AS conditions 
#                                   CROSS JOIN (SELECT DISTINCT party_chewy_id 
#                                               FROM   custods.pet_med_condition_rel) AS pets 
#                                              LEFT JOIN custods.pet_med_condition_rel pmc 
#                                                     ON conditions.pet_med_condition_id = 
#                                                        pmc.pet_med_condition_id 
#                                                        AND pets.party_chewy_id = pmc.party_chewy_id 
#                            ORDER  BY pets.party_chewy_id, 
#                                      conditions.pet_med_condition_id 
#                            LIMIT  10000;
#                    ''' , connection)
#
##May want to separate out product features from orders stuff
#cust_products = pd.read_sql('''
#                          SELECT o.customer_id, 
#                               o.order_key, 
#                               o.order_id, 
#                               p.product_id, 
#                               p.product_part_number, 
#                               olcm.product_key, 
#                               olcm.customer_key, 
#                               olcm.customer_address_key,
#                               o.customer_address_id,  
#                               o.order_status, 
#                               o.order_placed_dttm,
#                               p.product_type, 
#                               p.product_name,
#                               p.product_purchase_brand,  
#                               o.order_count_of_items, 
#                               o.order_count_of_unique_items, 
#                               o.order_count_of_unique_items_pharmacy, 
#                               olcm.order_line_each_price, 
#                               olcm.order_line_total_price, 
#                               olcm.order_line_currency, 
#                               p.product_category_level1, 
#                               p.product_category_level2, 
#                               p.product_category_level3,
#                               p.product_price,
#                               p.product_list_price,
#                               p.product_weight,
#                               p.product_weight_uom,
#                               p.product_rating_avg, 
#                               p.product_rating_cnt, 
#                               p.product_attr_special_diet, 
#                               p.product_lifestage, 
#                               p.product_ingredients, 
#                               p.product_keywords 
#                        FROM   chewybi.orders_pharmacy AS o 
#                               LEFT JOIN chewybi.order_line_cost_measures_pharmacy AS olcm 
#                                      ON olcm.order_key = o.order_key 
#                               LEFT JOIN chewybi.products_pharmacy AS p 
#                                      ON p.product_key = olcm.product_key
#                        WHERE p.product_category_level1 = 'Dog'
#                        LIMIT  10000; 
#                    ''' , connection)
#
#cust_address = pd.read_sql('''
#                            SELECT customer_id, 
#                                   customer_address_city, 
#                                   customer_address_state AS us_state, 
#                                   customer_address_zip, 
#                                   ( CASE 
#                                       WHEN customer_address_state = 'CT' 
#                                             OR customer_address_state = 'ME' 
#                                             OR customer_address_state = 'MA' 
#                                             OR customer_address_state = 'NH' 
#                                             OR customer_address_state = 'RI' 
#                                             OR customer_address_state = 'VT' THEN 'NewEngland' 
#                                       WHEN customer_address_state = 'NJ' 
#                                             OR customer_address_state = 'NY' 
#                                             OR customer_address_state = 'PA' THEN 'MidAtlantic' 
#                                       WHEN customer_address_state = 'IN' 
#                                             OR customer_address_state = 'IL' 
#                                             OR customer_address_state = 'MI' 
#                                             OR customer_address_state = 'OH' 
#                                             OR customer_address_state = 'WI' THEN 'ENCentral' 
#                                       WHEN customer_address_state = 'IA' 
#                                             OR customer_address_state = 'KS' 
#                                             OR customer_address_state = 'MN' 
#                                             OR customer_address_state = 'MO' 
#                                             OR customer_address_state = 'NE' 
#                                             OR customer_address_state = 'ND' 
#                                             OR customer_address_state = 'SD' THEN 'WNCentral' 
#                                       WHEN customer_address_state = 'DE' 
#                                             OR customer_address_state = 'DC' 
#                                             OR customer_address_state = 'FL' 
#                                             OR customer_address_state = 'GA' 
#                                             OR customer_address_state = 'MD' 
#                                             OR customer_address_state = 'NC' 
#                                             OR customer_address_state = 'SC' 
#                                             OR customer_address_state = 'VA' 
#                                             OR customer_address_state = 'WV' THEN 'SAtlantic' 
#                                       WHEN customer_address_state = 'AL' 
#                                             OR customer_address_state = 'KY' 
#                                             OR customer_address_state = 'MS' 
#                                             OR customer_address_state = 'TN' THEN 'ESCentral' 
#                                       WHEN customer_address_state = 'AR' 
#                                             OR customer_address_state = 'LA' 
#                                             OR customer_address_state = 'OK' 
#                                             OR customer_address_state = 'TX' THEN 'WSCentral' 
#                                       WHEN customer_address_state = 'AZ' 
#                                             OR customer_address_state = 'CO' 
#                                             OR customer_address_state = 'ID' 
#                                             OR customer_address_state = 'NM' 
#                                             OR customer_address_state = 'MT' 
#                                             OR customer_address_state = 'UT' 
#                                             OR customer_address_state = 'NV' 
#                                             OR customer_address_state = 'WY' THEN 'Mountain' 
#                                       WHEN customer_address_state = 'AK' 
#                                             OR customer_address_state = 'CA' 
#                                             OR customer_address_state = 'HI' 
#                                             OR customer_address_state = 'OR' 
#                                             OR customer_address_state = 'WA' THEN 'Pacific' 
#                                       ELSE 'NoRegion' 
#                                     end )                AS region 
#                            FROM   chewybi.customer_addresses 
#                            WHERE  customer_address_last_order_flag = 'true' 
#                            LIMIT  10000; 
#                            ''', connection)
#                                   
#cust_location = cust_address[['customer_id', 'us_state', 'region']]
#
##cust_prod_joined = pet_cust.set_index('petprofile_customer_id').join(cust_products.set_index('customer_id'), how='inner').join(location.set_index('customer_id'), how='left')
#
