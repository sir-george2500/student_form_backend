from fastapi import HTTPException

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "sql3.freesqldatabase.com",
    "user": "sql3673373",
    "password": "EsllsED8rR",
    "database": "sql3673373",
    "port": 3306,
}

def create_students_table():
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()

            create_table_query = """
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    middle_name VARCHAR(255),
                    date_of_birth DATE NOT NULL,
                    tech_knowledge ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
                    select_course VARCHAR(255) NOT NULL,
                    preferred_attendance_days ENUM('MWF', 'TTH', 'FS') NOT NULL,
                    email_address VARCHAR(255) NOT NULL,
                    phone_number VARCHAR(20) NOT NULL,
                    home_address VARCHAR(255) NOT NULL
                );
            """

            cursor.execute(create_table_query)
            print("Table 'students' created successfully!")

    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error creating 'students' table")

def insert_student_data(student_form):
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the student with the same first_name and last_name already exists
            check_duplicate_query = """
                SELECT COUNT(*) FROM students
                WHERE email_address = %(email_address)s;
            """
            cursor.execute(check_duplicate_query, student_form.dict())
            duplicate_count = cursor.fetchone()[0]  # Fetch the count

            if duplicate_count > 0:
                raise HTTPException(status_code=400, detail="You have already register")

            # Insert data into 'students' table
            insert_query = """
                INSERT INTO students
                (first_name, last_name, middle_name, date_of_birth, tech_knowledge,
                 select_course, preferred_attendance_days, email_address, phone_number, home_address)
                VALUES
                (%(first_name)s, %(last_name)s, %(middle_name)s, %(date_of_birth)s, %(tech_knowledge)s,
                 %(select_course)s, %(preferred_attendance_days)s, %(email_address)s, %(phone_number)s, %(home_address)s);
            """

            # Data to be inserted
            student_data = student_form.dict()

            cursor.execute(insert_query, student_data)
            connection.commit()
            print("Data inserted into 'students' table successfully!")

    except Error as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error inserting data into 'students' table")

    finally:
        if connection and connection.is_connected():
            connection.close()
