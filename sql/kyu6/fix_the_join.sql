SELECT 
  job.job_title,
  round((SUM(job.salary) / COUNT(people)), 2)::float as average_salary,
  COUNT(people.id) as total_people,
  round(SUM(job.salary), 2)::float as total_salary
FROM people JOIN job ON people.id = job.id
GROUP BY job.job_title
ORDER BY average_salary DESC
