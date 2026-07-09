from fastapi import APIRouter, UploadFile, File

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
    return {
        "filename": file.filename
    }