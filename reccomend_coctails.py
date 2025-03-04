from libs import *

index = faiss.read_index("cocktails_faiss.index")
texts = np.load("cocktails_texts.npy", allow_pickle=True)

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container([
        html.H2("Cocktail Name Prediction", className='form-title'),

        html.Div([
            html.Label("Enter your cocktail wish:", className="form-label"),
            dcc.Input(id="input-wish", type="text", placeholder="Enter your cocktail wish", className="form-input"),
        ], className="input-column"),

        dbc.Row([
            dbc.Col(dbc.Button("Predict", id="predict-button", color="primary"), width={"size": 6, "offset": 3}),
            dbc.Col(html.Div(id="prediction-output", className="my-predict-button"), width=12),
        ], className="my-predict-button"),
    ], className='my-form-container')
])

@app.callback(
    Output("prediction-output", "children"),
    [Input("predict-button", "n_clicks")],
    [State("input-wish", "value")],
    prevent_initial_call=True
)
def make_prediction(n_clicks, wish):
    if not wish or not wish.strip():
        return "Please enter a valid cocktail wish!"

    try:
        response = requests.get("http://127.0.0.1:5000/search/", params={"query": wish, "top_k": 3})
        response.raise_for_status()  # Raise an error for bad HTTP responses
        data = response.json()

        if data.get("results"):
            return "\n".join(f"{result['name']} - {result['description']}" for result in data["results"])
        return "No results found!"

    except requests.exceptions.RequestException as e:
        return f"Error with the API request: {e}"

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

