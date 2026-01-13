import openai
import numpy as np

def retrieve(query, model, index, texts, k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    return [texts[i] for i in indices[0]]

def generate_answer(context, query):
    prompt = f"""
You are a building compliance expert.

Context from standards:
{context}

Question:
{query}

Answer with clause references.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
