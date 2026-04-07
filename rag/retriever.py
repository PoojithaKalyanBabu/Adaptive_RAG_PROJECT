from sklearn.metrics.pairwise import cosine_similarity


def retrieve_documents(query, documents, strategy):
    query_vec = documents["vectorizer"].transform([query])
    scores = cosine_similarity(query_vec, documents["embeddings"]).flatten()

    top_k = strategy["top_k"]
    top_indices = scores.argsort()[-top_k:][::-1]

    return [documents["chunks"][i] for i in top_indices]
