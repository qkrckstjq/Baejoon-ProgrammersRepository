# Write your MySQL query statement below
select a.machine_id, round(avg(a.result), 3) as processing_time from (
    select 
    a.machine_id,
    sum(
    case
        when a.activity_type = 'start'
        then a.timestamp * -1
        else a.timestamp
    end
    ) as result
    from Activity a
    group by a.machine_id, a.process_id
) a
group by a.machine_id

