select 
    uu.USER_ID,
    uu.NICKNAME,
    CONCAT(uu.CITY, ' ', uu.STREET_ADDRESS1, ' ', uu.STREET_ADDRESS2) as 전체주소,
    CONCAT(SUBSTR(uu.TLNO, 1, 3), '-', SUBSTR(uu.TLNO, 4, 4), '-', SUBSTR(uu.TLNO, 8, 4)) as 전화번호
from USED_GOODS_USER uu
where (
    select count(*) 
    from USED_GOODS_BOARD ub
    where ub.WRITER_ID = uu.USER_ID
) >= 3
order by uu.USER_ID desc;