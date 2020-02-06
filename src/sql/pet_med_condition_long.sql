SELECT pets.party_chewy_id AS pet_id, 
       conditions.pet_med_condition_id, 
       conditions.pet_med_condition_nm, 
       CASE 
         WHEN pmc.pet_med_condition_id IS NOT NULL THEN 1 
         ELSE 0 
       END AS med_condition 
FROM   (SELECT DISTINCT pet_med_condition_id, 
                        pet_med_condition_nm 
        FROM   custods.pet_med_condition) AS conditions 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_condition_rel) AS pets 
       LEFT JOIN custods.pet_med_condition_rel pmc 
              ON conditions.pet_med_condition_id = pmc.pet_med_condition_id 
                 AND pets.party_chewy_id = pmc.party_chewy_id 
ORDER  BY pets.party_chewy_id, 
          conditions.pet_med_condition_id; 