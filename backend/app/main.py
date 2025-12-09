from fastapi import FastAPI
from .routers import users, articles, comments, search, analytics
from .core.database import init_db

app = FastAPI(title='Ecommerce CMS Platform')

@app.on_event('startup')
async def startup():
    await init_db()

# Register routers
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(comments.router)
app.include_router(search.router)
app.include_router(analytics.router)

@app.get('/')
def root():
    return {'message': 'Welcome to the FastAPI Ecommerce CMS Platform'}