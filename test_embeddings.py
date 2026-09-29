from app.embeddings.embedding_model import EmbeddingModel


embedding_model = EmbeddingModel()

text = "Our running shoes are lightweight and comfortable."

embedding = embedding_model.generate_embedding(text)

print("Embedding type:", type(embedding))
print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])