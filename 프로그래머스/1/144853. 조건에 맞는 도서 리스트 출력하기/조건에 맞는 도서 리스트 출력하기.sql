-- 코드를 입력하세요
SELECT BOOK_ID, cast(PUBLISHED_DATE as char) as PUBLISHED_DATE from BOOK
where year(PUBLISHED_DATE) = '2021' and CATEGORY = '인문'
order by PUBLISHED_DATE