select u.name as results from (
    select u.name, count(*) as cnt from MovieRating mr
    left join Users u
    on mr.user_id = u.user_id
    group by mr.user_id
    order by cnt desc, u.name
    limit 1
) u

union all

select * from (
    select m.title as results from Movies m
    left join (
        select mr.movie_id, avg(mr.rating) as average_rating from MovieRating mr
        where DATE_FORMAT(mr.created_at, "%Y-%m") = '2020-02'
        group by movie_id
    ) te
    on m.movie_id = te.movie_id
    order by te.average_rating desc, m.title
    limit 1
) e



