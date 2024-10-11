from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import PORT,SERVER_URL,ENV
from apps.calculator.route import router as calculate_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    
app=FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(calculate_router,prefix='/calculate',tags=['calculate'])

if  __name__=='__main__':
    uvicorn.run('main:app',host=SERVER_URL,port=int(PORT),reload=(ENV=='dev'))