from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/')
def add_comment(content: str, user_id: int, article_id: int, db: Session = Depends(get_db)):
    comment = models.Comment(content=content, user_id=user_id, article_id=article_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment