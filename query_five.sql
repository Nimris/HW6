select t.fullname, s.name
from teachers t
join subjects s on t.id = s.teacher_id
where t.id = 1;
