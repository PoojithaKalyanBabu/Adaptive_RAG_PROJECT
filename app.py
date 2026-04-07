import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

from rag.document_loader import load_documents
from rag.adaptive_logic import analyze_query
from rag.retriever import retrieve_documents
from rag.prompt_builder import build_prompt

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

# Load documents once
documents = load_documents("data/knowledge.txt")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        query = request.json.get("query")

        strategy = analyze_query(query)
        context_docs = retrieve_documents(query, documents, strategy)
        prompt = build_prompt(query, context_docs, strategy)

        response = model.generate_content(prompt)

        return jsonify({
            "answer": response.text
        })

    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
