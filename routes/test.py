from fastapi import APIRouter


router = APIRouter()

@router.post("/{body}")
async def root(body: str):
    data = eval(body)
    return data
