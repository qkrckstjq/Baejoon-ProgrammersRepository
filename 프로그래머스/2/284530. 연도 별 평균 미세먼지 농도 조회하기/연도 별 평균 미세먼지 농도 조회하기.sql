-- 코드를 작성해주세요

select YEAR(a.YM) as YEAR, ROUND(AVG(a.PM_VAL1), 2) as "PM10", ROUND(AVG(a.PM_VAL2), 2) as "PM2.5" from AIR_POLLUTION a
where a.LOCATION2 = "수원"
group by YEAR(a.YM)
order by YEAR(a.YM) asc