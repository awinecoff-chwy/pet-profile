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
        --WHERE pet_allergy_id != -1 -- 'UNKNOWN'
        --AND pet_allergy_id != 1 -- 'None'
        ) AS allergies 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_allergy_rel
                   --WHERE pet_allergy_id != -1 --UNKOWN
                   --AND pet_allergy_id != 1 --None
                   ) AS pets 
       LEFT JOIN custods.pet_allergy_rel pa 
              ON allergies.pet_allergy_id = pa.pet_allergy_id 
                 AND pets.party_chewy_id = pa.party_chewy_id 
WHERE pets.party_chewy_id BETWEEN  38000000 AND 40000000;