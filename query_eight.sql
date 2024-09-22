select t.fullname as teacher, avg(gr.grade) as average_grade, sub.name as subject
from teachers t
join subjects sub on t.id = sub.teacher_id
join grades gr on sub.id = gr.subject_id
where t.id = 1
group by t.fullname, sub.name;
