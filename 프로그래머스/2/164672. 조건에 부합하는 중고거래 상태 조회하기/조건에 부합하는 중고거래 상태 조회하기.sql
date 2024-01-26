-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, 
(
    case
    when u.status = 'done' then '거래완료' 
    when u.status = 'reserved' then '예약중'
    else '판매중'
    end
) status
from USED_GOODS_BOARD u
where created_date = '2022-10-05'
order by board_id desc