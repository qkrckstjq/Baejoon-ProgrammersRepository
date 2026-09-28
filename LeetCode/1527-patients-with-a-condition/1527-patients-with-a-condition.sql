# Write your MySQL query statement below
select * from Patients p
where REGEXP_LIKE(p.conditions, '(^DIAB1|[:space:]DIAB1)')