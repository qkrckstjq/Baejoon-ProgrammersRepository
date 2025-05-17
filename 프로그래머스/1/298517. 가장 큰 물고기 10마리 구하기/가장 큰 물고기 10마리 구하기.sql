select fi.ID, fi.LENGTH from FISH_INFO fi
where fi.LENGTH != 'NULL'
order by -fi.LENGTH, fi.id
limit 10

