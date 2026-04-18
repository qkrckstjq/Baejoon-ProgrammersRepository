select 
    id,
    case 
        when nt = 1 then 'CRITICAL'
        when nt = 2 then 'HIGH'
        when nt = 3 then 'MEDIUM'
        when nt = 4 then 'LOW'
    end as COLONY_NAME
from (
    select 
        id,
        ntile(4) over (order by SIZE_OF_COLONY desc) as nt
    from ECOLI_DATA
) t
order by id;