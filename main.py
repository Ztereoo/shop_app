from contextlib import asynccontextmanager

import uvicorn

from core.config import settings
from fastapi import FastAPI,Path
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(router_v1, prefix= settings.api_v1_prefix)

@app.get('/')
def hello_index():
    return {
        'data': 'some information'
    }





@app.get('/name/')
def greet(name: str = "Poppy"):
    name = name.upper()
    return {'message': f"Hello {name}"}




@app.post('/calc')
def calculate(a:int,b:int):
    return {
        'a':a,
        'b':b,
        'result':a+b,
    }

if __name__ == '__main__':
    uvicorn.run(app)
