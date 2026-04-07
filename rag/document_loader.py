from sklearn.feature_extraction.text import TfidfVectorizer


def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = text.split("\n\n")
    vectorizer = TfidfVectorizer()
    embeddings = vectorizer.fit_transform(chunks)

    return {
        "chunks": chunks,
        "embeddings": embeddings,
        "vectorizer": vectorizer
    }
