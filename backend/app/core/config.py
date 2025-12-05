from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()