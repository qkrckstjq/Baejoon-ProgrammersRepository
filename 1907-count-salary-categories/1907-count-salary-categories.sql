# Write your MySQL query statement below

with a as (
    select 
    case
        when a.income < 20000
        then "Low Salary"
        when a.income > 50000
        then "High Salary"
        else "Average Salary"
    end as category
    from Accounts a
)
select a.category, count(*) as accounts_count from a
where a.category = 'Low Salary'

union 

select 'Average Salary', count(*) as accounts_count from a
where a.category = 'Average Salary'

union

select a.category, count(*) as accounts_count from a
where a.category = 'High Salary'