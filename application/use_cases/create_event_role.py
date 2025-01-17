from domain.entities.role import Role
from infrastructure.repositories.sqlalchemy_role_repository import SqlAchemyRoleRepository


def create_role(name:str, repository:SqlAchemyRoleRepository):
    role = Role(name=name)
    return repository.create_role(role)
