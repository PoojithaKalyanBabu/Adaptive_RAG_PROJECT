def analyze_query(query):
    words = len(query.split())

    if words < 6:
        return {"top_k": 2, "style": "concise"}
    else:
        return {"top_k": 5, "style": "detailed"}
