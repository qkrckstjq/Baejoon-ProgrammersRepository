-- 코드를 입력하세요
SELECT mcdp_cd 진료과코드, count(*) 5월예약건수 from appointment
where month(apnt_ymd) = 5 and year(apnt_ymd) = 2022
group by mcdp_cd
order by count(*), mcdp_cd 
