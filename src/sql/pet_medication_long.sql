SELECT pets.party_chewy_id as pet_id, 
       medications.pet_med_id, 
       medications.pet_med_nm, 
       CASE 
         WHEN pmc.pet_med_id IS NOT NULL THEN 1 
         ELSE 0 
       END AS med_condition 
FROM   (SELECT DISTINCT pet_med_id, 
                        pet_med_nm 
        FROM   custods.pet_med
        --WHERE pet_med_id != -1 --'UNKNOWN'
        --AND pet_med_id != 38 --'None'
        ) AS medications 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_rel
                   --WHERE pet_med_id != -1 --'UNKNOWN'
                   --AND pet_med_id != 38 --'None'
                   ) AS pets 
       LEFT JOIN custods.pet_med_rel pmc 
              ON medications.pet_med_id = pmc.pet_med_id 
                 AND pets.party_chewy_id = pmc.party_chewy_id 
WHERE pets.party_chewy_id BETWEEN  38000000 AND 40000000; 