select 
a.user_id,
a.reaction as dominant_reaction,
round(a.reaction_cnt / t.total_cnt, 2) as reaction_ratio 
from (
    -- 1. 유저별, 리액션별 카운트를 구하는 서브쿼리 (콘텐츠 5개 이상 참여한 유저만 필터링)
    select r.user_id, r.reaction, count(*) as reaction_cnt from reactions r
    where r.user_id in
        (
            select r.user_id from reactions r
            group by r.user_id
            having count(distinct r.content_id) >= 5
        )
    group by r.user_id, r.reaction
) a
join (
    -- 2. 유저별 전체 반응 수와 최대 반응 카운트를 구하는 서브쿼리
    select user_id, sum(reaction_cnt) as total_cnt, max(reaction_cnt) as max_cnt
    from (
        select r.user_id, r.reaction, count(*) as reaction_cnt from reactions r
        where r.user_id in
            (
                select r.user_id from reactions r
                group by r.user_id
                having count(distinct r.content_id) >= 5
            )
        group by r.user_id, r.reaction
    ) sub
    group by user_id
    having max(reaction_cnt) / sum(reaction_cnt) >= 0.6
) t on a.user_id = t.user_id and a.reaction_cnt = t.max_cnt
order by reaction_ratio desc, a.user_id asc;