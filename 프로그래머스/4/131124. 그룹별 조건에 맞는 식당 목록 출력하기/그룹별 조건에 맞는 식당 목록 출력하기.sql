# -- 코드를 입력하세요
SELECT mp.MEMBER_NAME, rr.REVIEW_TEXT, rr.REVIEW_DATE from REST_REVIEW rr
inner join (
    select MEMBER_ID, count(*) as total from REST_REVIEW
    group by MEMBER_ID
    order by total desc
    limit 1
) t
on rr.MEMBER_ID = t.MEMBER_ID
left join MEMBER_PROFILE mp
on rr.MEMBER_ID = mp.MEMBER_ID
order by rr.REVIEW_DATE ASC, rr.REVIEW_TEXT asc

# select count(*) as total from REST_REVIEW
# group by MEMBER_ID
# having MAX(total)