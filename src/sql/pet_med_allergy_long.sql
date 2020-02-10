SELECT pets.party_chewy_id AS pet_id, 
       allergies.pet_med_allergy_id, 
       allergies.pet_med_allergy_nm, 
       CASE 
         WHEN pma.pet_med_allergy_id IS NOT NULL THEN 1 
         ELSE 0 
       END                 AS med_allergy 
FROM   (SELECT DISTINCT pet_med_allergy_id, 
                        pet_med_allergy_nm 
        FROM   custods.pet_med_allergy
        --WHERE pet_med_allergy_id != -1 --'UNKNOWN'
        --AND pet_med_allergy_id != 29 --'None'
        ) AS allergies 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_allergy_rel
                   --WHERE pet_med_allergy_id != -1 --'UNKNOWN'
                   --AND pet_med_allergy_id != 29 --'None'
                   ) AS pets 
       LEFT JOIN custods.pet_med_allergy_rel pma 
              ON allergies.pet_med_allergy_id = pma.pet_med_allergy_id 
                 AND pets.party_chewy_id = pma.party_chewy_id 
       LEFT JOIN integrate.customer_petprofile_ps pc_int 
               ON pc_int.petprofile_master_id = pets.party_chewy_id
       LEFT JOIN integrate.customer_ps c_int
               ON pc_int.petprofile_customer_master_id = c_int.customer_master_id
WHERE c_int.customer_order_last_placed_dttm > '2019-11-01'
        AND pc_int.petprofile_status = 1
        AND pc_int.petprofile_pettype_description = 'Dog';