# Write your MySQL query statement below

select a.student_id, a.subject,
(select score from Scores where student_id = a.student_id and subject = a.subject and exam_date = a.min_date) as first_score,
(select score from Scores where student_id = a.student_id and subject = a.subject and exam_date = a.max_date) as latest_score
from (
    select s.student_id, s.subject, MIN(s.exam_date) as min_date, MAX(s.exam_date) as max_date from Scores s
    group by s.student_id, s.subject
    having count(*) >= 2
) a
where (select score from Scores where student_id = a.student_id and subject = a.subject and exam_date = a.min_date) < 
(select score from Scores where student_id = a.student_id and subject = a.subject and exam_date = a.max_date)
order by a.student_id, a.subject
