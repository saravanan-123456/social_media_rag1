from sqlalchemy.orm import Session
from qdrant_client.models import PointStruct
from uuid import uuid5, NAMESPACE_DNS

from app.models import SocialMediaPost as SocialMediaPostModel
from app.preprocessing.processor import preprocess_post
from app.chunking.chunker import chunk_text
from app.embeddings.embedding_model import EmbeddingModel
from app.vector_db.qdrant_client import QdrantVectorDB


class VectorDBService:

    @staticmethod
    def initialize():

        vector_db = QdrantVectorDB()

        vector_db.create_collection()

        return {
            "status": "initialized",
            "collection": vector_db.COLLECTION_NAME
        }

    @staticmethod
    def store_post_embeddings(
        post_id: str,
        db: Session
    ):

        # 1. Get post from PostgreSQL
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

        # 4. Generate embeddings
        embedding_model = EmbeddingModel()

        embeddings = embedding_model.generate_embeddings(
            chunks
        )

        # 5. Connect to Qdrant
        vector_db = QdrantVectorDB()

        vector_db.create_collection()

        client = vector_db.get_client()

        # 6. Create Qdrant points
        points = []

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            point = PointStruct(
                id=str(uuid5(NAMESPACE_DNS,f"social_media_post_{post_id}_chunk_{index + 1}")),
                vector=embedding,
                payload={
                    "post_id": processed_post["post_id"],
                    "platform": processed_post["platform"],
                    "user_id": processed_post["user_id"],
                    "chunk_id": index + 1,
                    "text": chunk,
                    "likes": processed_post["likes"],
                    "comments": processed_post["comments"],
                    "shares": processed_post["shares"],
                    "reach": processed_post["reach"],
                    "timestamp": str(
                        processed_post["timestamp"]
                    )
                }
            )

            points.append(point)

        # 7. Store vectors in Qdrant
        client.upsert(
            collection_name=vector_db.COLLECTION_NAME,
            points=points
        )

        return {
            "status": "stored",
            "post_id": post_id,
            "chunk_count": len(chunks),
            "collection": vector_db.COLLECTION_NAME
        }