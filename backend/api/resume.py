import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.pdf_service import extract_text_from_pdf
from backend.services.resume_parser import parse_resume
router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def test_resume():
    return{
        "message": "Resume API working"
    }
@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail = "Only Pdf files are allowed"
        )

    os.makedirs("uploads", exist_ok=True)

    contents = await file.read()

    with open(f"uploads/{file.filename}","wb") as f:

        f.write(contents)

    pdf_path = f"uploads/{file.filename}"
    text = extract_text_from_pdf(pdf_path)
    parsed_resume = parse_resume(text)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "parsed_resume": parsed_resume,
        "preview": text[:500]
    }