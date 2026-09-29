from fastapi import FastAPI

from app.api.routes.ingestion import router as ingestion_router
from app.api.routes.preprocessing import (
    router as preprocessing_router,
)
from app.api.routes.chunking import router as chunking_router
from app.api.routes.embeddings import router as embeddings_router
from app.api.routes.vector_db import router as vector_db_router
from app.database import Base, engine
from app.models import SocialMediaPost


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Social Media Analytics RAG API",
    description="FastAPI backend for social media analytics and RAG",
    version="1.0.0"
)


app.include_router(ingestion_router)

app.include_router(preprocessing_router)

app.include_router(chunking_router)

app.include_router(embeddings_router)

app.include_router(vector_db_router)


@app.get("/")
def root():
    return {
        "message": "Social Media Analytics RAG API is running"
    }