from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.authMiddleware import AuthMiddleware
from contextlib import asynccontextmanager
from pymongo import AsyncMongoClient
from beanie import init_beanie
import schemas.userTypes as user_types
import schemas.dishTypes as dish_types
import schemas.tablesTypes as tables_types
import schemas.eventTypes as event_types
from routers.user_router import router as user_router
from routers.dish_router import router as dish_router
from routers.tables_router import router as table_router




@asynccontextmanager
async def lifespan(app:FastAPI):
    client = AsyncMongoClient("mongodb://localhost:27017")
    
    # Выбираем базу данных
    database = client["waiter_demo"]
    
    # Регистрируем СРАЗУ ВСЕ модели в этой базе данных
    await init_beanie(
        database=database,
        document_models=[
            user_types.UserSchema,
            dish_types.DishSchema,
            dish_types.menu_CategoriesSchema,
            dish_types.dish_ElementSchema,
            tables_types.tablesSchema,
            tables_types.hallSchema,
            event_types.orderSchema



            
        ]
    )
    print("Все коллекции Beanie успешно инициализированы!")
    
    yield
    await client.close()
    


app=FastAPI(title="demo-server",lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Разрешенные адреса (или ["*"] для вообще всех)
    allow_credentials=True,           # Разрешить куки и авторизацию
    allow_methods=["*"],              # Разрешить все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"],              # Разрешить любые заголовки
)
app.add_middleware(AuthMiddleware)
app.include_router(user_router)
app.include_router(dish_router)
app.include_router(table_router)
@app.get("/")
async def mainPage():
    return {"aaa"}

