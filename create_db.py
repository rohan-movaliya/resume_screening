import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get database config from environment
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Connect to the database
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = db.cursor()

# Table creation queries
tables = []

tables.append("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    linkedin_url VARCHAR(255),
    github_url VARCHAR(255),
    website_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

tables.append("""
CREATE TABLE IF NOT EXISTS education (
    education_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    degree VARCHAR(100),
    institution VARCHAR(255),
    field_of_study VARCHAR(100),
    start_year TEXT,
    end_year TEXT,
    grade VARCHAR(20),
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

tables.append("""
CREATE TABLE IF NOT EXISTS experience (
    experience_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    job_title VARCHAR(100),
    company_name VARCHAR(255),
    location VARCHAR(100),
    start_date TEXT,
    end_date TEXT,
    currently_working BOOLEAN,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

tables.append("""
CREATE TABLE IF NOT EXISTS skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    skill_name TEXT,
    proficiency_level VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

tables.append("""
CREATE TABLE IF NOT EXISTS projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    project_title VARCHAR(255),
    description TEXT,
    technologies_used VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

tables.append("""
CREATE TABLE IF NOT EXISTS certifications (
    certification_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(255),
    issuer VARCHAR(255),
    issue_date TEXT,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

# Execute all table creation queries
for query in tables:
    cursor.execute(query)

print("✅ All tables created successfully.")

# Close the connection
cursor.close()
db.close()
