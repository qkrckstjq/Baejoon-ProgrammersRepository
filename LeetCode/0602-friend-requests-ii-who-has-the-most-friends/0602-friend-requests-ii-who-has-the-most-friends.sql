# Write your MySQL query statement below
select r.requester_id as id, count(*) as num from (
    select * from RequestAccepted r
    union all
    select r1.accepter_id as requster_id, r1.requester_id as accepter_id, r1.accept_date from RequestAccepted r1) r
group by r.requester_id
order by num desc
limit 1

-- select * from RequestAccepted r
-- union all
-- select r1.accepter_id as requster_id, r1.requester_id as accepter_id, r1.accept_date from RequestAccepted r1
