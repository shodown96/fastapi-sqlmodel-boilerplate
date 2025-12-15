from contextlib import asynccontextmanager

import uvicorn
from api import api_router
from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

@app.get("/")
async def get_base_endpoint():
    return {"message": "Welcome to FastAPI Boilerplate"}


app.include_router(api_router)

# For debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
