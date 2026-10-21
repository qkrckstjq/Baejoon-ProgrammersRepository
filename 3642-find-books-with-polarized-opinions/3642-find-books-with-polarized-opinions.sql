# Write your MySQL query statement below
with min_5 as (
    select 
    *,
    count(*) as total_count,
    sum(case when rs.session_rating >= 4 then 1 else 0 end) as high_r,
    sum(case when rs.session_rating <= 2 then 1 else 0 end) as low_r,
    max(rs.session_rating) as max_rating,
    min(rs.session_rating) as min_rating
    from reading_sessions rs
    group by rs.book_id
    having count(*) >= 5
)
select 
m.book_id,
b.title, 
b.author, 
b.genre, 
b.pages, 
(m.max_rating - m.min_rating) as rating_spread,  
round((m.high_r + m.low_r) / m.total_count, 2) as polarization_score
from min_5 m
left join books b
on m.book_id = b.book_id
where m.high_r != 0 and m.low_r != 0 and ((m.high_r + m.low_r) / m.total_count) >= 0.6
order by polarization_score desc, b.title desc