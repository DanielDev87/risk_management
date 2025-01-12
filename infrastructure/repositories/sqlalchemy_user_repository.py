from sqlalchemy.orm import Session
from domain.entities.user import User

class SqlAchemyUserRepository:
    def __init__(self, db:Session):
        self.db = db

    def create_user(self, user:User):
        db_user = User(username=user.username, password=user.password, role_id=user.role_id)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_user(self, username:str):
        return self.db.query(User).filter(User.username == username).first()
   