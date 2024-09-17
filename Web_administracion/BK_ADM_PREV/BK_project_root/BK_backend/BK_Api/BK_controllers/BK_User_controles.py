from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter()

@router.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
        return users
