-- 코드를 입력하세요
SELECT count(*) as USERS from USER_INFO ui
where ui.JOINED like '2021%'
and ui.age between 20 and 29
