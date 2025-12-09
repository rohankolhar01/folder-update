from fastapi import FastAPI
from routers import users, articles, auth, comments
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Database initialization
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce CMS Backend")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "E-commerce CMS Backend Running!"}