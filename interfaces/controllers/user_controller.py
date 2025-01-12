from infrastructure.database.db_config import SessionLocal
from infrastructure.repositories.sqlalchemy_user_repository import SqlAchemyUserRepository
from application.use_cases.create_event_user import create_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Funcion para la ruta /users
@router.post("/users/")
def create_new_user(username:str, password:str, role_id:int, db:Session = Depends(get_db)):
    repository = SqlAchemyUserRepository(db)
    user = create_user(username, password, role_id, repository)
    return user