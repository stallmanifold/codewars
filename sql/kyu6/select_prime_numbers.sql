with primes (num) as (
    select generate_series(2, 99)
)
select num as prime
from primes primes1
where num not in (
    select primes1.num
    from primes primes2 
    where primes2.num < primes1.num
      and mod(primes1.num, primes2.num) = 0
)
limit 25