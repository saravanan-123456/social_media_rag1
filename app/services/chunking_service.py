from sqlalchemy.orm import Session

from app.models import SocialMediaPost as SocialMediaPostModel
from app.preprocessing.processor import preprocess_post
from app.chunking.chunker import chunk_text


class ChunkingService:

    @staticmethod
    def chunk_post(
        post_id: str,
        db: Session,
        chunk_size: int = 100,
        chunk_overlap: int = 20
    ) -> dict:

        # 1. Get post from database
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

        # 2. Preprocess the post
        processed_post = preprocess_post(post)

        # 3. Get cleaned text
        text = processed_post["text"]

        # 4. Create chunks
        chunks = chunk_text(
            text=text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        # 5. Build response
        return {
            "post_id": processed_post["post_id"],
            "platform": processed_post["platform"],
            "chunks": chunks,
            "chunk_count": len(chunks)
        }