import logging
from random import randint
from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection

fake = Faker('uk-UA')
subjects = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "Ukrainian"]
groups = ["A", "B", "C"]

def insert_data(conn):
    with conn.cursor() as c:
        try:
            c.executemany("INSERT INTO groups (name) VALUES (%s);", [(group,) for group in groups])
            
            students = [(fake.name(), randint(1, len(groups))) for _ in range(40)]
            c.executemany("INSERT INTO students (fullname, group_id) VALUES (%s, %s);", students)
            
            teachers = [(fake.name(),) for _ in range(4)]
            c.executemany("INSERT INTO teachers (fullname) VALUES (%s);", teachers)

            subjects_data = [(subject, randint(1, 4)) for subject in subjects]
            c.executemany("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);", subjects_data)
            
            grades = [(randint(1, 40), randint(1, len(subjects)), randint(1, 100), fake.date_this_year()) for _ in range(400)]
            c.executemany("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s);", grades)

            conn.commit()
            
        except DatabaseError as e:
            logging.error(f"Database error occurred: {e}")
            conn.rollback()
        finally:
            logging.info("Data insertion completed.")

if __name__ == '__main__':
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn)
            else:
                logging.error("Error! Cannot create the database connection.")
    except RuntimeError as err:
        logging.error(f"Runtime error: {err}")
