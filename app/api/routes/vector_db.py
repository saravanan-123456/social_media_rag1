from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.vector_db_service import VectorDBService


router = APIRouter(
    prefix="/api/v1/vector-db",
    tags=["Vector Database"]
)


@router.post("/initialize")
def initialize_vector_database():

    return VectorDBService.initialize()


@router.post("/posts/{post_id}")
def store_post_embeddings(
    post_id: str,
    db: Session = Depends(get_db)
):

    result = VectorDBService.store_post_embeddings(
        post_id=post_id,
        db=db
    )

    return result