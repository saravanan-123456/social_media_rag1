from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(model_name)

    def generate_embedding(
        self,
        text: str
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()