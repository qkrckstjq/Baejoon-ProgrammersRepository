-- 코드를 작성해주세요

select he.EMP_NO, he.EMP_NAME,
(case
    when AVG(hg.SCORE) >= 96
    then 'S'
    when AVG(hg.SCORE) >= 90
    then 'A'
    when AVG(hg.SCORE) >= 80
    then 'B'
    else 'C'
end) GRADE,
(case
    when AVG(hg.SCORE) >= 96
    then he.SAL * (20 / 100)
    when AVG(hg.SCORE) >= 90
    then he.SAL * (15 / 100)
    when AVG(hg.SCORE) >= 80
    then he.SAL * (10 / 100)
    else 0
end) BONUS
from HR_EMPLOYEES he
join HR_GRADE hg
on he.EMP_NO = hg.EMP_NO
group by EMP_NO
order by EMP_NO