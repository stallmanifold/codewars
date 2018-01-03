SELECT id, 
       name, 
       trim(split_part(characteristics, ',', 1)) AS characteristic
FROM monsters
ORDER BY id