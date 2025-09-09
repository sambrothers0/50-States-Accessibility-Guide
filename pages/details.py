from dash import html, register_page, dcc, Input, Output, callback
import requests

register_page(__name__, path="/page2", name="Page 2")

layout = html.Div([
    html.H2("Page 2", className="page-title"),
    html.P("Click to fetch a random cat fact from a public API!",className="page-subtitle"),
    html.Button("Get Cat Fact", id="button-cat", n_clicks=0),
    dcc.Loading(html.Div(id="cat-fact"))
], className="page2-wrapper")


@callback(
    Output("cat-fact", "children"),
    Input("button-cat", "n_clicks")
)

def fetch_cat_fact(n):
    try:
        r = requests.get("https://catfact.ninja/fact", timeout=5)
        r.raise_for_status()
        fact = r.json().get("fact", "No fact found.")
        return html.Div(fact)
    except requests.RequestException as e:
        return html.Div(f"Error fetching cat fact from API: {e}")
