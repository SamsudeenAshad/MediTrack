from fastapi import APIRouter

router = APIRouter()

@router.get("/overview")
async def get_analytics_overview():
    return {"message": "Analytics endpoint - coming soon"}
