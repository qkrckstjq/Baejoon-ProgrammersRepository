/* Write your PL/SQL query statement below */
select l.ip, count(*) as invalid_count from logs l
where 
REGEXP_COUNT(l.ip, '\.') != 3 or
REGEXP_LIKE(REGEXP_SUBSTR(l.ip, '[^.]+', 1, 1), '^0[0-9]+') or REGEXP_SUBSTR(l.ip, '[^.]+', 1, 1) not between 0 and 255 or
REGEXP_LIKE(REGEXP_SUBSTR(l.ip, '[^.]+', 1, 2), '^0[0-9]+') or REGEXP_SUBSTR(l.ip, '[^.]+', 1, 2) not between 0 and 255 or
REGEXP_LIKE(REGEXP_SUBSTR(l.ip, '[^.]+', 1, 3), '^0[0-9]+') or REGEXP_SUBSTR(l.ip, '[^.]+', 1, 3) not between 0 and 255 or
REGEXP_LIKE(REGEXP_SUBSTR(l.ip, '[^.]+', 1, 4), '^0[0-9]+') or REGEXP_SUBSTR(l.ip, '[^.]+', 1, 4) not between 0 and 255
group by l.ip
order by invalid_count desc, l.ip desc
