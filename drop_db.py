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

# Disable foreign key checks before dropping
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

# List of table names to drop (in any order since FK checks are off)
tables = [
    "certifications",
    "projects",
    "skills",
    "experience",
    "education",
    "users"
]

# Drop each table
for table in tables:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")
        print(f"✅ Dropped table: {table}")
    except Exception as e:
        print(f"❌ Failed to drop table {table}: {e}")

# Re-enable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

# Close connection
cursor.close()
db.close()

print("✅ All specified tables dropped successfully.")
