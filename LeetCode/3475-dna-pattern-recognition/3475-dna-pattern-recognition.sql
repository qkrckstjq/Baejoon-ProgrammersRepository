# Write your MySQL query statement below
select
*,
case
    when REGEXP_LIKE(s.dna_sequence, '^ATG')
    then 1
    else 0
end as has_start,
case
    when REGEXP_LIKE(s.dna_sequence, '(TAA|TAG|TGA)$')
    then 1
    else 0
end as has_stop,
case
    when REGEXP_LIKE(s.dna_sequence, 'ATAT')
    then 1
    else 0
end as has_atat,
case
    when REGEXP_LIKE(s.dna_sequence, 'G{3}')
    then 1
    else 0
end as has_ggg
from
Samples s
order by s.sample_id
