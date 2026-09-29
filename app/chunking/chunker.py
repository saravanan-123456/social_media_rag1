def chunk_text(
    text: str,
    chunk_size: int = 100,
    chunk_overlap: int = 20
) -> list[str]:

    if not text.strip():
        return []

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    words = text.split()

    chunks = []
    current_chunk = []

    current_length = 0

    for word in words:

        word_length = len(word)

        additional_length = (
            word_length
            if not current_chunk
            else word_length + 1
        )

        if current_length + additional_length <= chunk_size:
            current_chunk.append(word)
            current_length += additional_length

        else:
            chunks.append(" ".join(current_chunk))

            overlap_words = []
            overlap_length = 0

            for previous_word in reversed(current_chunk):

                additional = (
                    len(previous_word)
                    if not overlap_words
                    else len(previous_word) + 1
                )

                if overlap_length + additional <= chunk_overlap:
                    overlap_words.insert(0, previous_word)
                    overlap_length += additional
                else:
                    break

            current_chunk = overlap_words + [word]

            current_length = len(
                " ".join(current_chunk)
            )

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks