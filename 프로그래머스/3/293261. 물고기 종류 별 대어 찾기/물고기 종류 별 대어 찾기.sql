-- 코드를 작성해주세요
select
fi.ID,
fn.FISH_NAME,
fi.LENGTH
from FISH_INFO fi
left join FISH_NAME_INFO fn
on fi.FISH_TYPE = fn.FISH_TYPE
where (fi.FISH_TYPE, fi.LENGTH) in
(select FISH_TYPE, MAX(LENGTH) from FISH_INFO
 group by FISH_TYPE)
