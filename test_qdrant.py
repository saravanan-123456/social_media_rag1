from app.vector_db.qdrant_client import QdrantVectorDB


vector_db = QdrantVectorDB()

client = vector_db.get_client()

result = client.scroll(
    collection_name=vector_db.COLLECTION_NAME,
    limit=10,
    with_vectors=True,
    with_payload=True
)

points, next_page = result

print("Number of points:", len(points))

for point in points:
    print("\nPoint ID:", point.id)
    print("Vector dimensions:", len(point.vector))
    print("Payload:", point.payload)