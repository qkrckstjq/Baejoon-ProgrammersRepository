/* Write your PL/SQL query statement below */

select
e.employee_id,
e.employee_name,
LEVEL,
(
    SELECT COUNT(*)
    FROM Employees c
    START WITH c.employee_id = e.employee_id
    CONNECT BY PRIOR c.employee_id = c.manager_id
) - 1 AS team_size,
(
    SELECT sum(salary)
    FROM Employees c
    START WITH c.employee_id = e.employee_id
    CONNECT BY PRIOR c.employee_id = c.manager_id
) AS budget
from Employees e
start with e.manager_id is null
connect by prior employee_id = manager_id
order by LEVEL asc, budget desc, e.employee_name asc