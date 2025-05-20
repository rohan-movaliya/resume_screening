import os
from extract_pdf_to_json import extract_pdf_to_json
from store_json_to_database import store_json_to_database

RESUME_FOLDER = "Resume Dataset"
TEMP_JSON_PATH = "temp_data.json"

for filename in os.listdir(RESUME_FOLDER):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(RESUME_FOLDER, filename)
        print(f"📄 Processing: {filename}")

        try:
            # 1. Extract PDF to JSON
            extract_pdf_to_json(pdf_path, TEMP_JSON_PATH)

            # 2. Store JSON into database
            store_json_to_database(TEMP_JSON_PATH)

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
    print("\n")
print("✅ All resumes processed.")
