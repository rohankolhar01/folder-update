from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(prefix="/search", tags=["Search"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
def search_articles(query: str, db: Session = Depends(get_db)):
    return db.query(models.Article).filter(models.Article.title.like(f"%{query}%")).all()