from fastapi import FastAPI
from interfaces.controllers.user_controller import router as user_controller
from interfaces.controllers.role_controller import router as role_controller
from interfaces.controllers.risk_category_controller import router as risk_category_controller
from infrastructure.database.db_config import Base, engine
from contextlib import asynccontextmanager

# Define el manejador de lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):   
    async with engine.begin() as conn:        
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def get_root():
    return {"message": "Hola muchachas"}

app.include_router(user_controller)
app.include_router(role_controller)
app.include_router(risk_category_controller)