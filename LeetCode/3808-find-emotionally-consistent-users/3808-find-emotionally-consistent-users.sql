# Write your MySQL query statement below
with temp as (
    select 
    r.user_id,
    r.reaction,
    count(*) as reaction_cnt
    from reactions r
    where r.user_id in
        (
            select r.user_id from reactions r
            group by r.user_id
            having count(distinct r.content_id) >= 5
        )
    group by r.user_id, r.reaction    
),
react as (
    select *, dense_rank() over (partition by t.user_id order by reaction_cnt desc) as rk from temp t
)
select a.user_id, a.reaction as dominant_reaction, round(max_react / total_react, 2) as reaction_ratio from (
    select 
    a.user_id,
    a.reaction,
    max(a.reaction_cnt) over (partition by a.user_id) as max_react,
    sum(a.reaction_cnt) over (partition by a.user_id) as total_react,
    a.rk
    from react a
) a
where max_react / total_react >= 0.6 and rk = 1
order by reaction_ratio desc, a.user_id asc

