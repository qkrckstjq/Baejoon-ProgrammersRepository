# Write your MySQL query statement below
with comp as (
    select c.visited_on, count(*) as cnt, sum(c.amount) as "sum" from Customer c
    group by c.visited_on
),
result as (
    select c1.visited_on, sum(c2.sum) as amount, sum(c2.sum) / count(c1.visited_on) as average_amount, count(c1.visited_on) as cnt from comp c1
    left join comp c2
    on c1.visited_on between DATE_SUB(c2.visited_on, INTERVAL 6 DAY) and c2.visited_on
    group by c1.visited_on
)
select DATE_ADD(r.visited_on, INTERVAL 6 DAY) as visited_on, r.amount, round(average_amount, 2) as average_amount from result r
where r.cnt = 7
order by r.visited_on 
    