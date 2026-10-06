# Write your MySQL query statement below
select 
t.transaction_date,
sum(
    case
        when t.amount % 2 = 1
        then t.amount
        else 0
    end
) as odd_sum,
sum(
    case
        when t.amount % 2 = 0
        then t.amount
        else 0
    end
) as even_sum
from transactions t
group by t.transaction_date
order by t.transaction_date