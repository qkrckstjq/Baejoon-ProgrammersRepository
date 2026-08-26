# Write your MySQL query statement below
select round((count(*) / (select count(distinct(player_id)) from Activity)), 2) as fraction from Activity a1
left join (select a.player_id, MIN(a.event_date) as second_login from Activity a group by a.player_id) a2
on a1.player_id = a2.player_id and a1.event_date = a2.second_login + interval 1 day
where a2.player_id is not null

-- select *, (select count(*) from Activity) from Activity