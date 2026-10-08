# Write your MySQL query statement below
select * from Users u
where u.email REGEXP '^[a-zA-Z0-9_]+@{1}[a-zA-Z]+\\.com$'
order by u.user_id