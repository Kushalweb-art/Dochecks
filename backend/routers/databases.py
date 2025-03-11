from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

router = APIRouter()

@router.post("/test_connection/")
def test_connection(database_url: str):
    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            return {"message": "Connection successful"}
    except OperationalError:
        raise HTTPException(status_code=400, detail="Database connection failed")
