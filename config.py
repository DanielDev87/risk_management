from sqlalchemy import create_engine
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:risk@localhost:5432/riskcontrol" # ejemplo

    class Config:
        env_file = ".env"

settings = Settings()

# Configuración del motor SQLAlchemy
engine = create_engine(settings.DATABASE_URL, echo=True)