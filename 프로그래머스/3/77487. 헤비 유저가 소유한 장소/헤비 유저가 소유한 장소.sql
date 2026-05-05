-- 코드를 입력하세요
select p.ID, p.NAME, p.HOST_ID from PLACES p
left join (SELECT * from PLACES
group by HOST_ID
having count(*) >= 2) p2
on p.HOST_ID = p2.HOST_ID
where p2.HOST_ID is not NULL
order by p.ID
