from sqlalchemy.orm import Session

from app.models import SocialMediaPost as SocialMediaPostModel
from app.schemas.social_media import SocialMediaPost


class IngestionService:

    @staticmethod
    def ingest_post(
        post: SocialMediaPost,
        db: Session
    ):

        db_post = SocialMediaPostModel(
            post_id=post.post_id,
            platform=post.platform,
            user_id=post.user_id,
            caption=post.caption,
            likes=post.likes,
            comments=post.comments,
            shares=post.shares,
            reach=post.reach,
            timestamp=post.timestamp
        )

        db.add(db_post)

        db.commit()

        db.refresh(db_post)

        return {
            "id": db_post.id,
            "post_id": db_post.post_id,
            "platform": db_post.platform,
            "status": "ingested"
        }