def build_prompt(query, docs, strategy):
    context = "\n".join(docs)

    if strategy["style"] == "concise":
        return f"""
Answer briefly.

Context:
{context}

Question:
{query}
"""
    else:
        return f"""
Answer with explanation.

Context:
{context}

Question:
{query}
"""
