SELECT s.fullname, g.name as group, gr.grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN grades gr ON s.id = gr.student_id
Join subjects sb ON gr.subject_id = sb.id
WHERE s.group_id = 1
AND sb.id = 1;