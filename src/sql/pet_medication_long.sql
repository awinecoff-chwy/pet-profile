SELECT pets.party_chewy_id as pet_id, 
       medications.pet_med_id, 
       medications.pet_med_nm, 
       CASE 
         WHEN pmc.pet_med_id IS NOT NULL THEN 1 
         ELSE 0 
       END AS medication
FROM   (SELECT DISTINCT pet_med_id, 
                        pet_med_nm 
        FROM   custods.pet_med

        ) AS medications 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_rel
                   ) AS pets 
       LEFT JOIN custods.pet_med_rel pmc 
              ON medications.pet_med_id = pmc.pet_med_id 
                 AND pets.party_chewy_id = pmc.party_chewy_id 
       LEFT JOIN integrate.customer_petprofile_ps pc_int 
               ON pc_int.petprofile_master_id = pets.party_chewy_id
       LEFT JOIN integrate.customer_ps c_int
               ON pc_int.petprofile_customer_master_id = c_int.customer_master_id
       LEFT JOIN custods.party_pet pp 
              ON pp.party_chewy_id = pets.party_chewy_id  
       LEFT JOIN custods.pet_type pt 
              ON pt.pet_type_id = pp.pet_type_id       
WHERE c_int.customer_order_last_placed_dttm > '2019-11-01'
        AND pc_int.petprofile_status = 1
        AND pt.pet_type_nm = 'Dog';