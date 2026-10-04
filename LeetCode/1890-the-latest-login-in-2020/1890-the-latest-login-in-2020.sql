# Write your MySQL query statement below
select l.user_id, MAX(l.time_stamp) as last_stamp from Logins l
where YEAR(time_stamp) = 2020
group by l.user_id