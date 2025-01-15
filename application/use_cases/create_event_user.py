from domain.entities.user import User
from infrastructure.repositories.sqlalchemy_user_repository import SqlAchemyUserRepository


def create_user(username:str, password:str, role_id:int, repository:SqlAchemyUserRepository):
    user = User(username=username, password=password, role_id=role_id)    
    return repository.create_user(user)