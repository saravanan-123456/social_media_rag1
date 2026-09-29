from sqlalchemy.orm import Session

from app.models import SocialMediaPost as SocialMediaPostModel
from app.preprocessing.processor import preprocess_post
from app.chunking.chunker import chunk_text
from app.embeddings.embedding_model import EmbeddingModel


class EmbeddingService:

    @staticmethod
    def generate_post_embeddings(
        post_id: str,
        db: Session
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

        # 2. Preprocess
        processed_post = preprocess_post(post)

        # 3. Chunk
        chunks = chunk_text(
            text=processed_post["text"],
            chunk_size=100,
            chunk_overlap=20
        )

        # 4. Load embedding model
        embedding_model = EmbeddingModel()

        # 5. Generate embeddings
        embeddings = embedding_model.generate_embeddings(
            chunks
        )

        # 6. Build result
        chunk_data = []

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings),
            start=1
        ):
            chunk_data.append({
                "chunk_id": index,
                "text": chunk,
                "embedding": embedding,
                "embedding_dimension": len(embedding)
            })

        return {
            "post_id": processed_post["post_id"],
            "platform": processed_post["platform"],
            "chunk_count": len(chunks),
            "chunks": chunk_data
        }