from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(prefix="/articles", tags=["Articles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/')
def create_article(title: str, content: str, author_id: int, db: Session = Depends(get_db)):
    article = models.Article(title=title, content=content, author_id=author_id)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

@router.get('/')
def get_articles(db: Session = Depends(get_db)):
    return db.query(models.Article).all()