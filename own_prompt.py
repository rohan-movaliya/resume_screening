prompt = """
You are a resume parser. Extract structured data in JSON format from the given resume using the exact schema below.

**Important Instructions:**
- All fields in the JSON must follow the schema strictly.
- In the `skills` field, combine all technical and soft skills into **one plain text string**, separated by commas, on a **single line**.
- Do not return the skills as an array or object.
- If any field is missing in the resume, leave it blank (or use null for dates/numbers).
- Do not change the structure or field names of the schema.

Schema:
{
  "user": {
    "full_name": "",
    "email": "",
    "phone": "",
    "address": "",
    "linkedin_url": "",
    "github_url": "",
    "website_url": "",
  },
  "education": [
    {
      "degree": "",
      "institution": "",
      "field_of_study": "",
      "start_year": 0,
      "end_year": 0,
      "grade": "",
      "description": ""
    }
  ],
  "experience": [
    {
      "job_title": "",
      "company_name": "",
      "location": "",
      "start_date": "",
      "end_date": "",
      "currently_working": false,
      "description": ""
    }
  ],
  "skills": {
      "skill_name": "",
      "proficiency_level": ""
  },
  "projects": [
    {
      "project_title": "",
      "description": "",
      "technologies_used": "",
    }
  ],
  "certifications": [
    {
      "title": "",
      "issuer": "",
      "issue_date": "",
      "description": "",
    }
  ]
}

Resume:
{context}
"""