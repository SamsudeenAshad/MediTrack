from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_vitals():
    return {"message": "Vitals endpoint - coming soon"}
