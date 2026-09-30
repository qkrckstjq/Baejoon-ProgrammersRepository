# Write your MySQL query statement below
select u.user_id, CONCAT(UPPER(SUBSTR(u.name, 1, 1)), LOWER(SUBSTR(u.name, 2))) as name from Users u
order by u.user_id