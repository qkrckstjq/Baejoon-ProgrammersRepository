-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, SUBSTRING(HIRE_YMD,1,10) as HIRE_YMD  from DOCTOR d
where d.MCDP_CD = 'CS' or d.MCDP_CD = 'GS'
order by d.HIRE_YMD desc, d.DR_NAME 