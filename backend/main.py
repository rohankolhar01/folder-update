from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, articles, comments, search, analytics
from database import engine, Base

app = FastAPI(title="CMS Backend API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(articles.router)
app.include_router(comments.router)
app.include_router(search.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Welcome to the CMS API built with FastAPI and MySQL"}