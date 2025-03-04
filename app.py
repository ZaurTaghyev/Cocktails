from libs import *

app = FastAPI()

index = faiss.read_index("cocktails_faiss.index")
texts = np.load("cocktails_texts.npy", allow_pickle=True)

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

@app.get("/search/")
def search_cocktail(query: str, top_k: int = 3):
    query_emb = model.encode(query, convert_to_numpy=True).reshape(1, -1)
    
    distances, indices = index.search(query_emb, top_k)
    
    results = [{"name": texts[i][0], "description": texts[i][1]} for i in indices[0]]
    
    return {"query": query, "results": results}
