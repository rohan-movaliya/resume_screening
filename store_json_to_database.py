import json
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os

def store_json_to_database(json_file_path: str):
    load_dotenv()

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    # Connect to MySQL
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = db.cursor()

    try:
        # Load JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Insert into users table
        user = data['user']
        cursor.execute('''
            INSERT INTO users (full_name, email, phone, address, linkedin_url, github_url, website_url, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            user['full_name'], user['email'], user['phone'], user['address'],
            user['linkedin_url'], user['github_url'], user['website_url'], datetime.now()
        ))
        user_id = cursor.lastrowid

        # Insert into education table
        for edu in data['education']:
            cursor.execute('''
                INSERT INTO education (user_id, degree, institution, field_of_study, start_year, end_year, grade, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                user_id, edu['degree'], edu['institution'], edu['field_of_study'],
                edu['start_year'], edu['end_year'], edu['grade'], edu['description']
            ))

        # Insert into experience table
        for exp in data['experience']:
            cursor.execute('''
                INSERT INTO experience (user_id, job_title, company_name, location, start_date, end_date, currently_working, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                user_id, exp['job_title'], exp['company_name'], exp['location'],
                exp['start_date'], exp['end_date'], exp['currently_working'], exp['description']
            ))

        # # Insert into skills table
        skills = data['skills']['skill_name']
        cursor.execute('''
            INSERT INTO skills (user_id, skill_name, proficiency_level)VALUES (%s, %s, %s)
        ''', (
            user_id, skills, data['skills']['proficiency_level']
        ))

        # Insert into projects table
        for project in data['projects']:
            cursor.execute('''
                INSERT INTO projects (user_id, project_title, description, technologies_used)
                VALUES (%s, %s, %s, %s)
            ''', (
                user_id, project['project_title'], project['description'], project['technologies_used']
            ))

        # Insert into certifications table
        for cert in data['certifications']:
            cursor.execute('''
                INSERT INTO certifications (user_id, title, issuer, issue_date, description)
                VALUES (%s, %s, %s, %s, %s)
            ''', (
                user_id, cert['title'], cert['issuer'], cert['issue_date'], cert['description']
            ))

        db.commit()
        print("✅ Data successfully inserted into the database.")

    except mysql.connector.Error as err:
        db.rollback()
        print(f"❌ Database error: {err}")

    except Exception as e:
        db.rollback()
        print(f"❌ Unexpected error: {e}")

    finally:
        cursor.close()
        db.close()


