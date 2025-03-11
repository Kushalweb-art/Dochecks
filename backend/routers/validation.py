from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.soda_utils import run_soda_scan
from backend.models import ValidationResult
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/validate/{table_name}")
def validate_data(table_name: str, db: Session = Depends(get_db)):
    database_url = os.getenv("DATABASE_URL")
    results = run_soda_scan(database_url, table_name)

    # Save results to DB
    for result in results:
        db_result = ValidationResult(
            table_name=result["table"],
            column_name=result["column"],
            check_name=result["check_name"],
            status=result["status"],
        )
        db.add(db_result)
    db.commit()

    return {"results": results}
