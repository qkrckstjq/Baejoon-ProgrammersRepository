# Write your MySQL query statement below
with po as (
    select
    ct.patient_id,
    ct.test_date,
    MIN(test_date) as min_po
    from covid_tests ct
    where ct.result = 'Positive'
    group by patient_id
), temp as (
    select * from po

    union

    select
    ct.patient_id,
    ct.test_date,
    MIN(test_date) as min_ne
    from covid_tests ct
    where (select p.test_date from po p where ct.patient_id = p.patient_id) <= ct.test_date and ct.result = 'Negative'
    group by patient_id
)

select t.patient_id, p.patient_name, p.age, t.recovery_time from (
    select t.patient_id, DATEDIFF(MAX(t.min_po), MIN(t.min_po)) as recovery_time from temp t
    group by t.patient_id
) t
inner join patients p
on t.patient_id = p.patient_id and t.recovery_time != 0
order by t.recovery_time asc, p.patient_name