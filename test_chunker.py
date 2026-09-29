from app.chunking.chunker import chunk_text


text = (
    "Our new running shoes are finally here! "
    "They are lightweight and comfortable for "
    "long-distance running. Check them out today!"
)

chunks = chunk_text(
    text=text,
    chunk_size=50,
    chunk_overlap=10
)

for index, chunk in enumerate(chunks, start=1):
    print(f"Chunk {index}:")
    print(chunk)
    print()