from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"  # ejemplo

    class Config:
        env_file = ".env"

settings = Settings()