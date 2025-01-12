from pydantic_settings import BaseSettings

class Settings(BaseSettings):
<<<<<<< HEAD
    DATABASE_URL: str = "postgresql://postgres:@localhost:5432/riskmaltern"  # ejemplo
=======
    DATABASE_URL: str = "postgresql://postgres:123456789@localhost:5432/riskmanegement"  # ejemplo
>>>>>>> 840fcb4799451c6aa5899b844483fd2d7018cb7e

    class Config:
        env_file = ".env"

settings = Settings()