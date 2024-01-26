-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID,r.CONTENTS,
SUBSTRING(r.created_date,1,10) as CREATED_DATE from USED_GOODS_BOARD b
inner join USED_GOODS_REPLY r
on b.BOARD_ID = r.BOARD_ID
where b.created_date between '2022-10-01' and '2022-10-31'
order by r.created_date, b.title