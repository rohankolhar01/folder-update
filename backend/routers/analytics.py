from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get('/')
def get_analytics():
    return {"visits": 1000, "active_users": 150}