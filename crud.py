import psycopg2
from psycopg2 import sql


# Database constants
DATABASE = 'a3_p1'
USER = 'postgres'
PASSWORD = '1699'
HOST = 'localhost'
PORT = '5432'

# connect and check if connected
def connect():
    try:
        connection = psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )
        print("Connected to database")
        return connection
    except Exception as e:
        print(e)
        return None

# Method to get all student data and print it
def get_all_students():
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Connection failed")

# Method to add student to the database    
def add_student(first_name, last_name, email, enrollment_date):
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
            conn.commit()
            print(f"Student added: {first_name} {last_name}")
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Connection failed")

# Method to update student email via their ID
def update_student_email(student_id, email):
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))
            conn.commit()
            print(f"Email updated for student {student_id}")
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Connection failed")

# Method to delete student via their ID
def delete_student(student_id):
    conn = connect()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            conn.commit()
            print(f"Student {student_id} deleted")
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Connection failed")
