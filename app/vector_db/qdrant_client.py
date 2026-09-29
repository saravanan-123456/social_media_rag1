from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


class QdrantVectorDB:

    COLLECTION_NAME = "social_media_posts"

    def __init__(self):
        self.client = QdrantClient(
            path="./qdrant_data"
        )

    def create_collection(self):

        collections = self.client.get_collections()

        collection_names = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME not in collection_names:

            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def get_client(self):
        return self.client