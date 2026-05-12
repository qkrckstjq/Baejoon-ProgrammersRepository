-- 코드를 입력하세요
SELECT 
    b.AUTHOR_ID, 
    a.AUTHOR_NAME, 
    b.CATEGORY, 
    SUM(b.price * bs.total) as TOTAL_SALES 
FROM (select BOOK_ID, SUM(SALES) as total from BOOK_SALES 
    where YEAR(SALES_DATE) = "2022" and MONTH(SALES_DATE) = "1"
    group by BOOK_ID
) bs
left join BOOK b 
on bs.BOOK_ID = b.BOOK_ID
left join AUTHOR a
on b.AUTHOR_ID = a.AUTHOR_ID
GROUP BY
    b.AUTHOR_ID,
    a.AUTHOR_NAME,
    b.CATEGORY
order by a.AUTHOR_ID asc, b.CATEGORY desc