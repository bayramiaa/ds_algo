/* find 2nd highest salary */
SELECT max(salary)
FROM salesperson
WHERE salary != (SELECT max(salary) from salesperson);

/* find nth */
SELECT *
FROM salesperson as s1
WHERE (
    SELECT COUNT(DISTINCT(s2.salary))
    FROM salesperson as s2
    WHERE s2.salary > s1.salary
    ) = 1;

/* name of all salespeople that do not have a order with samsonic */
SELECT name
FROM salesperson
WHERE id NOT in (
  SELECT orers.salesperson_id
  FROM orers, customers
  WHERE orers.cust_id = customers.id
  and customers.name = 'samsonic'
  )

/* > x orders */
SELECT name
FROM salesperson, orers
WHERE salesperson.id = orers.salesperson_id
GROUP BY name, salesperson_id
HAVING count(salesperson_id) > 2

/*   all members of department if max salary is 80k for that dept
*/
SELECT e1.*
FROM employees AS e1
INNER JOIN(
  SELECT department_id, MAX(salary) AS max_salary
  FROM employees
  GROUP BY department_id
  ) AS e2
ON e1.department_id = e2.department_id
AND e2.max_salary = 80000;

/* highest slary by dept */
SELECT e1.*
FROM employees AS e1
INNER JOIN(
  SELECT department_id, MAX(salary) AS max_salary
  FROM employees
  GROUP BY department_id
  ) AS e2
ON e1.department_id = e2.department_id
AND e1.salary = e2.max_salary;
*/

/* second highest salary */

SELECT *
FROM employees
WHERE salary = (
  SELECT MAX(salary) AS max_salary
  FROM employees
  WHERE salary != (SELECT MAX(salary) from employees)
  );


/* nth highest */

SELECT *
FROM employees
WHERE salary = (
  SELECT salary
  FROM employees AS e1
  WHERE (SELECT COUNT(DISTINCT(e2.salary)) FROM employees AS e2 WHERE e2.salary > e1.salary) = 2
  );

/* create view */
CREATE VIEW dog_food AS
SELECT id, name
FROM customers




















































