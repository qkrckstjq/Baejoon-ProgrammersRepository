CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select MAX(e.salary) from 
      (select salary, (DENSE_RANK() OVER(order by salary desc)) as d_rank from Employee) e
      where e.d_rank = N
  );
END