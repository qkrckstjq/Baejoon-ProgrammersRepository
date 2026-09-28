# Write your MySQL query statement below
select * from Users u
where REGEXP_LIKE(u.mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$', 'c')