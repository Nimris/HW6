SELECT g.name AS group_name, AVG(gr.grade) AS avg_grade, gr.subject_id AS subject_id
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.name = 'Math'
GROUP BY g.name, gr.subject_id;
