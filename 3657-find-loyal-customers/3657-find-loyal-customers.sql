# Write your MySQL query statement below
select
ct.customer_id
from customer_transactions ct
group by customer_id
having 
sum(case when ct.transaction_type = 'purchase' then 1 else 0 end) >= 3 and
datediff(max(ct.transaction_date), min(ct.transaction_date)) >= 30 and 
sum(case when ct.transaction_type = 'refund' then 1 else 0 end) / count(*) < 0.2
order by ct.customer_id 
