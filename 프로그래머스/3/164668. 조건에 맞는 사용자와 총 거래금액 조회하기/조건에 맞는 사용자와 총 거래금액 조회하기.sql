# -- 코드를 입력하세요
select * from 
(SELECT ub.WRITER_ID as USER_ID, uu.NICKNAME, sum(ub.PRICE) as TOTAL_SALES from USED_GOODS_BOARD ub
 left join USED_GOODS_USER uu
 on ub.WRITER_ID = uu.USER_ID
where ub.STATUS = "DONE"
group by ub.WRITER_ID) t
where t.TOTAL_SALES >= 700000
order by t.TOTAL_SALES asc