from sqlalchemy import Column, Integer, String, DateTime
from .db import Base
from datetime import datetime

class ValidationResult(Base):
    __tablename__ = "validation_results"

    id = Column(Integer, primary_key=True, index=True)
    table_name = Column(String, index=True)
    column_name = Column(String, index=True, nullable=True)
    check_name = Column(String)
    status = Column(String)  # 'Pass' or 'Fail'
    created_at = Column(DateTime, default=datetime.utcnow)
