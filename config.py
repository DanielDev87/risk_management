from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DATABASE_URL: str = "postgresql://postgres:Carpeta24*@localhost:5432/riskmaltern"  # ejemplo

    class Config:
        env_file = ".env"

settings = Settings()