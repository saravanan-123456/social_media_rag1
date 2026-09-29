from sqlalchemy.orm import Session

from app.models import SocialMediaPost as SocialMediaPostModel
from app.preprocessing.processor import preprocess_post


class PreprocessingService:

    @staticmethod
    def preprocess_post(
        post_id: str,
        db: Session
    ) -> dict:

        post = (
            db.query(SocialMediaPostModel)
            .filter(
                SocialMediaPostModel.post_id == post_id
            )
            .first()
        )

        if not post:
            raise ValueError(
                f"Post {post_id} not found"
            )

        processed_post = preprocess_post(post)

        return processed_post