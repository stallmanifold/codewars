select id, 
       name, 
       trim(split_part(characteristics, ',', 1)) as characteristic
from monsters
order by id
