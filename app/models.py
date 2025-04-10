from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Secret(Base):
    __tablename__ = "secrets"

    id = Column(Integer, primary_key=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    secret = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    ttl_seconds = Column(Integer)
    ip_address = Column(String)