import os
from fastapi import APIRouter, UploadFile, File, HTTPException

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
            details = "Only Pdf files are allowed"
        )

    os.makedirs("uploads", exist_ok=True)

    contents = await file.read()

    with open(f"uploads/{file.filename}","wb") as f:
        f.write(contents)
    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }