from fastapi import FastAPI
from interfaces.controllers.user_controller import router as user_controller
from infrastructure.database.db_config import Base, engine

#Esta linea crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_controller.router)