# Write your MySQL query statement below

with p as (
    select p.id, p.email, rank() over(partition by p.email order by p.id) as d_rank
    from Person p
    )

DELETE ori
FROM Person ori
JOIN p
ON ori.id = p.id
WHERE p.d_rank != 1;



-- select * from mwei