SELECT pets.party_chewy_id AS pet_id, 
       allergies.pet_med_allergy_id, 
       allergies.pet_med_allergy_nm, 
       CASE 
         WHEN pma.pet_med_allergy_id IS NOT NULL THEN 1 
         ELSE 0 
       END                 AS med_allergy 
FROM   (SELECT DISTINCT pet_med_allergy_id, 
                        pet_med_allergy_nm 
        FROM   custods.pet_med_allergy) AS allergies 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_allergy_rel) AS pets 
       LEFT JOIN custods.pet_med_allergy_rel pma 
              ON allergies.pet_med_allergy_id = pma.pet_med_allergy_id 
                 AND pets.party_chewy_id = pma.party_chewy_id 
ORDER  BY pets.party_chewy_id, 
          allergies.pet_med_allergy_id; 