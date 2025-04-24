import fitz
import re

def extract_lab_data(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Example pattern extraction (customize this as needed)
    results = {}
    patterns = {
        "Hemoglobin": r"Hemoglobin\s+([\d.]+)",
        "TSH": r"TSH\s+([\d.]+)",
        "WBC": r"WBC\s+([\d.]+)",
        "RBC": r"RBC\s+([\d.]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            results[key] = match.group(1)

    return results
