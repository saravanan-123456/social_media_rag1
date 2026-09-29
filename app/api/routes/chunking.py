from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.chunking_service import ChunkingService


router = APIRouter(
    prefix="/api/v1/chunking",
    tags=["Chunking"]
)


@router.post("/posts/{post_id}")
def chunk_post(
    post_id: str,
    db: Session = Depends(get_db)
):
    try:
        result = ChunkingService.chunk_post(
            post_id=post_id,
            db=db
        )

        return {
            "status": "chunked",
            "data": result
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )