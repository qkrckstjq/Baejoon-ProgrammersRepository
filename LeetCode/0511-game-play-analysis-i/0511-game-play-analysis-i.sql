# Write your MySQL query statement below
select a.player_id, a.event_date as first_login from (select *, rank() over(partition by a.player_id order by a.event_date) as d_rank from Activity a) a
where a.d_rank = 1