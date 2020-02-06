SELECT pets.party_chewy_id                                       AS pet_id, 
       pt.pet_type_nm, 
       pets.pet_nm, 
       pets.gender_cd, 
       pb.pet_breed_nm, 
       pb.size_cd                                                AS breed_size, 
       pets.size_type_cd                                         AS pet_size, 
       pets.birth_dt, 
       Datediff(dd, pets.birth_dt, Getdate())                    AS 
       pet_age_in_days, 
       Round(Datediff(dd, pets.birth_dt, Getdate()) / 365.25, 2) AS 
       pet_age_in_years, 
       pets.life_stage_cd, 
       pets.weight, 
       pets.weight_type_cd, 
       pets.create_dt, 
       pets.update_dt, 
       pc_int.petprofile_id, 
       pc_int.petprofile_master_id, 
       pc_int.petprofile_customer_id, 
       pc_int.petprofile_customer_master_id, 
       pc_int.petprofile_status                                  AS 
       profile_status, 
       ( CASE 
           WHEN pc_int.petprofile_status = 0 THEN 'inactive' 
           WHEN pc_int.petprofile_status = 1 THEN 'active' 
           WHEN pc_int.petprofile_status = 2 THEN 'deleted' 
           WHEN pc_int.petprofile_status = 3 THEN 'verified' 
           WHEN pc_int.petprofile_status = 4 THEN 'cancelled' 
           ELSE 'unknown' 
         END )                                                   AS 
       profile_status_desc, 
       pc_int.petprofile_status_reason                           AS 
       profile_status_reason, 
       ( CASE 
           WHEN pc_int.petprofile_status_reason = 0 THEN 'deceased' 
           WHEN pc_int.petprofile_status_reason = 1 THEN 'switched retailer' 
           WHEN pc_int.petprofile_status_reason = 2 THEN 'other' 
           ELSE 'unknown' 
         END )                                                   AS 
       profile_status_desc, 
       ad.customer_address_city, 
       ad.customer_address_state                                 AS us_state, 
       ad.customer_address_zip, 
       c_int.customer_full_name, 
       ad.customer_address_last_order_flag, 
       c_int.gross_average_order_value, 
       c_int.net_average_order_value, 
       c_int.customer_autoship_active_flag, 
       c_int.customer_order_shipped_consistency 
FROM   custods.party_pet AS pets 
       LEFT JOIN custods.pet_type pt 
              ON pt.pet_type_id = pets.pet_type_id 
       LEFT JOIN custods.pet_breed pb 
              ON pb.pet_breed_id = pets.pet_breed_id 
       LEFT JOIN integrate.customer_petprofile_ps pc_int 
              ON pc_int.petprofile_master_id = pets.party_chewy_id 
       LEFT JOIN integrate.customer_ps c_int 
              ON pc_int.petprofile_customer_master_id = c_int.customer_master_id 
       LEFT JOIN chewybi.customer_addresses ad 
              ON pc_int.petprofile_customer_id = ad.customer_id 
WHERE  ad.customer_address_last_order_flag = 'true' 