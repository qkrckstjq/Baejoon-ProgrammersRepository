select count(*) as FISH_COUTN, MAX(fi.LENGTH) as MAX_LENGTH, FISH_TYPE from FISH_INFO fi
group by FISH_TYPE
having AVG(
        case 
            when fi.LENGTH is NULL
            then 10
            when fi.LENGTH is not NULL
            then fi.LENGTH
        end
    )
 >= 33
 order by FISH_TYPE asc