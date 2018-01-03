WITH primes (num) AS (
    SELECT generate_series(2, 99)
)
SELECT num AS prime
FROM primes primes1
WHERE num NOT IN (
    SELECT primes1.num
    FROM primes primes2 
    WHERE primes2.num < primes1.num
      AND mod(primes1.num, primes2.num) = 0
)
LIMIT 25