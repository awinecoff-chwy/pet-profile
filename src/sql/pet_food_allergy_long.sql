SELECT pets.party_chewy_id AS pet_id, 
       allergies.pet_allergy_id, 
       allergies.pet_allergy_nm,
       CASE 
         WHEN pa.pet_allergy_id IS NOT NULL THEN 1 
         ELSE 0 
       END                 AS food_allergy 
FROM   (SELECT DISTINCT pet_allergy_id, 
                        pet_allergy_nm 
        FROM   custods.pet_allergy
        ) AS allergies 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_allergy_rel
                   ) AS pets 
       LEFT JOIN custods.pet_allergy_rel pa 
              ON allergies.pet_allergy_id = pa.pet_allergy_id 
                 AND pets.party_chewy_id = pa.party_chewy_id
       LEFT JOIN integrate.customer_petprofile_ps pc_int 
               ON pc_int.petprofile_master_id = pets.party_chewy_id
       LEFT JOIN integrate.customer_ps c_int
               ON pc_int.petprofile_customer_master_id = c_int.customer_master_id
WHERE c_int.customer_order_last_placed_dttm > '2019-11-01'
        AND pc_int.petprofile_status = 1
        AND pc_int.petprofile_pettype_description = 'Dog';