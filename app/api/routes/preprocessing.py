from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.preprocessing_service import (
    PreprocessingService,
)


router = APIRouter(
    prefix="/api/v1/preprocessing",
    tags=["Preprocessing"]
)


@router.post("/posts/{post_id}")
def preprocess_post(
    post_id: str,
    db: Session = Depends(get_db)
):

    try:

        result = PreprocessingService.preprocess_post(
            post_id=post_id,
            db=db
        )

        return {
            "status": "processed",
            "data": result
        }

    except ValueError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )