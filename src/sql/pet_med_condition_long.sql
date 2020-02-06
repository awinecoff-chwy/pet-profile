SELECT pets.party_chewy_id AS pet_id, 
       conditions.pet_med_condition_id, 
       conditions.pet_med_condition_nm, 
       CASE 
         WHEN pmc.pet_med_condition_id IS NOT NULL THEN 1 
         ELSE 0 
       END AS med_condition 
FROM   (SELECT DISTINCT pet_med_condition_id, 
                        pet_med_condition_nm 
        FROM   custods.pet_med_condition
        --WHERE pet_med_condition_id != -1 --'UNKNOWN'
	--AND   pet_med_condition_id != 19 --'None'
	) 
        AS conditions 
       CROSS JOIN (SELECT DISTINCT party_chewy_id 
                   FROM   custods.pet_med_condition_rel
	 	   --WHERE pet_med_condition_id != -1 --'UNKNOWN'
		   --AND   pet_med_condition_id != 19 --'None'                   
	           ) AS pets 
       LEFT JOIN custods.pet_med_condition_rel pmc 
              ON conditions.pet_med_condition_id = pmc.pet_med_condition_id 
                 AND pets.party_chewy_id = pmc.party_chewy_id 
WHERE pets.party_chewy_id BETWEEN  38000000 AND 40000000; 
	