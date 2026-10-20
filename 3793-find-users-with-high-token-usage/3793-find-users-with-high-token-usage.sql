# Write your MySQL query statement below
select p.user_id, count(*) as prompt_count, round(avg(p.tokens), 2) as avg_tokens from prompts p
group by p.user_id
having count(*) >= 3 and avg(p.tokens) < max(p.tokens)
order by avg_tokens desc, p.user_id asc