from fastapi import FastAPI
from routers import users, articles, comments, search, analytics

app = FastAPI(title="CMS Backend")

app.include_router(users.router)
app.include_router(articles.router)
app.include_router(comments.router)
app.include_router(search.router)
app.include_router(analytics.router)

@app.get('/')
def read_root():
    return {"message": "CMS Backend Running"}