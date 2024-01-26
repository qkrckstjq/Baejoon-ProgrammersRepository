-- 코드를 입력하세요
SELECT book_id, author_name, substring(published_date,1,10) published_date from BOOK b
inner join AUTHOR a
on b.author_id = a.author_id
where b.category = '경제'
order by published_date