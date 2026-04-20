-- 코드를 작성해주세요

select he.DEPT_ID,
(
    select DEPT_NAME_EN from HR_DEPARTMENT
    where he.DEPT_ID = DEPT_ID
) as DEPT_NAME_EN,
(
    select ROUND(AVG(he.SAL), 0) from HR_DEPARTMENT
    where he.DEPT_ID = DEPT_ID
) as AVG_SAL

from HR_EMPLOYEES he 
left join HR_DEPARTMENT hd
on hd.DEPT_ID = he.EMP_NO
group by he.DEPT_ID
order by AVG_SAL desc