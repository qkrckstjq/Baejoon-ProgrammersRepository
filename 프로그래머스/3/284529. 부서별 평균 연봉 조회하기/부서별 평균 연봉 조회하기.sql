-- 코드를 작성해주세요

select he.DEPT_ID,
(
    hd.DEPT_NAME_EN
) as DEPT_NAME_EN,
(
    ROUND(AVG(he.SAL), 0) 
) as AVG_SAL

from HR_EMPLOYEES he 
left join HR_DEPARTMENT hd
on hd.DEPT_ID = he.DEPT_ID
group by he.DEPT_ID, hd.DEPT_NAME_EN
order by AVG_SAL desc