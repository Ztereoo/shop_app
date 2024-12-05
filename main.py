from typing import Annotated
import uvicorn
from fastapi import FastAPI,Path
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

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
