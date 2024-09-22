select distinct s.fullname as student, sub.name as subject
from subjects sub
join grades gr on sub.id = gr.subject_id 
join students s on gr.student_id = s.id
where student_id = 12;