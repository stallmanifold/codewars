SELECT id, name
FROM departments
WHERE id IN (
  SELECT department_id
  FROM sales
  WHERE sales.price > 98
)
