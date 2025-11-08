import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr

#  Load dataset 
data = pd.read_csv("dataset")  # dataset info

#  Load embedding model 
model = SentenceTransformer("all-MiniLM-L6-v2")

#  Encode all Titles 
case_embeddings = model.encode(data["Title"].tolist(), convert_to_tensor=False)

#  Search function 
def search_cases(query, threshold=0.55):
    if not query.strip():
        return pd.DataFrame([{"Message": "❌ Empty query. Please type something."}])

    # Encode query
    query_embedding = model.encode([query], convert_to_tensor=False)
    similarity = cosine_similarity(query_embedding, case_embeddings).flatten()

    # Filter by threshold
    matches = [
        (i, score) for i, score in enumerate(similarity) if score >= threshold
    ]

    if not matches:
        return pd.DataFrame([{"Message": "❌ No relevant Incident found."}])

    # Sort by similarity (descending)
    matches = sorted(matches, key=lambda x: x[1], reverse=True)
    indices, scores = zip(*matches)

    results = data.iloc[list(indices)].copy()
    results["similarity"] = scores

    return results[["IncidentId", "Title", "InternalTitle", "similarity"]]

# ---- Gradio wrapper ----
def case_search(query, threshold):
    return search_cases(query, threshold=threshold)

# ---- Gradio UI ----
iface = gr.Interface(
    fn=case_search,
    inputs=[
        gr.Textbox(label="Search Query"),
        gr.Slider(0.3, 0.9, value=0.55, step=0.05, label="Similarity Threshold")
    ],
    outputs=gr.Dataframe(),
    title="Incident Search System by Marcos Riquetta",
    description="Search for incidents by Title. Adjust the similarity threshold for stricter or looser matching."
)