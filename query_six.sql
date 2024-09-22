SELECT s.fullname, g.name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE s.group_id = 1;