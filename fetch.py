from psycopg2 import DatabaseError

from connect import create_connection

def insert_data(conn, file_path):
    with conn.cursor() as c:
        try:
            with open(file_path, 'r') as file:
                sql_query = file.read()
                
            c.execute(sql_query)
            
            if sql_query.strip().upper().startswith("SELECT"):
                results = c.fetchall()
                
            for row in results:
                print(row)
                
        except DatabaseError as e:
            print(e)
            
if __name__ == '__main__':
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn, 'query_one.sql')
            else:
                print("Error! Cannot create the database connection.")
    except RuntimeError as err:
        print(f"Runtime error: {err}")
