-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD from APPOINTMENT a
left join PATIENT p
on a.PT_NO = p.PT_NO
left join DOCTOR d
on a.MDDR_ID = d.DR_ID
where DATE(a.APNT_YMD) = '2022-04-13' and a.APNT_CNCL_YN = 'N'
order by a.APNT_YMD asc