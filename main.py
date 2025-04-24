from fastapi import FastAPI, UploadFile, File
from extract import extract_lab_data
from llm import explain_results

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    extracted_data = extract_lab_data(contents)
    explanation = explain_results(extracted_data)
    return {"data": extracted_data, "explanation": explanation}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for stricter config
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

