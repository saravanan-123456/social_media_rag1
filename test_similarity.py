from app.embeddings.embedding_model import EmbeddingModel
from sklearn.metrics.pairwise import cosine_similarity


embedding_model = EmbeddingModel()

texts = [
    "I love running shoes.",
    "Running footwear is great.",
    "The stock market crashed today."
]

embeddings = embedding_model.generate_embeddings(texts)

similarity_matrix = cosine_similarity(embeddings)

for i in range(len(texts)):
    for j in range(len(texts)):
        print(
            f"Similarity between Text {i + 1} "
            f"and Text {j + 1}: "
            f"{similarity_matrix[i][j]:.4f}"
        )