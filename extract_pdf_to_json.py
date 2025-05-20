from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from own_prompt import prompt

load_dotenv()

def extract_pdf_to_json(pdf_path, output_json_path):
    # Load the resume PDF
    loader = PyPDFLoader(pdf_path)
    pdf_document = loader.load()

    # Extract the text content from the PDF
    context = "\n".join([doc.page_content for doc in pdf_document])

    # Initialize the AI model
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # Format the prompt
    formatted_prompt = prompt.replace("{context}", context)
    
    # Get response from the AI model
    response = llm.invoke(formatted_prompt)
    final_responsee = response.content
    output = final_responsee.replace("```json", "").replace("```", "").strip()

    # Save the output to a JSON file
    with open(output_json_path, mode="w") as file:
        file.write(output)

