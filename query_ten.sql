SELECT sub.name AS subject, s.fullname as student, t.fullname as teacher
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
JOIN grades gr ON sub.id = gr.subject_id
JOIN students s ON gr.student_id = s.id
WHERE s.id = 1 AND t.id = 1;