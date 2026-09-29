from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.social_media import SocialMediaPost
from app.services.ingestion_service import IngestionService


router = APIRouter(
    prefix="/api/v1/ingestion",
    tags=["Ingestion"]
)


@router.post("/posts")
def ingest_post(
    post: SocialMediaPost,
    db: Session = Depends(get_db)
):

    result = IngestionService.ingest_post(
        post=post,
        db=db
    )

    return result