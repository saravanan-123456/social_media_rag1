from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.embedding_service import EmbeddingService


router = APIRouter(
    prefix="/api/v1/embeddings",
    tags=["Embeddings"]
)


@router.post("/posts/{post_id}")
def generate_embeddings(
    post_id: str,
    db: Session = Depends(get_db)
):
    try:
        result = EmbeddingService.generate_post_embeddings(
            post_id=post_id,
            db=db
        )

        return {
            "status": "embedded",
            "data": result
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )