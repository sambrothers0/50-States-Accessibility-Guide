import dash
from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/page3", name="Electricity")

#find and read in the data
Data_Path = Path(__file__).resolve().parent.parent / "data" / "electricity_prices.csv"
df = pd.read_csv(Data_Path)

df["year"] = pd.to_numeric(df["year"]).astype(int)
df["prices"] = pd.to_numeric(df["price"])

layout = html.Div(
    style = {"backgroundColor": "#293831", "color":"white", "padding":"10px"},
    children = [
    html.H1("Electricity Prices by US State", style = {"color":"#cdd6d3", "textAlign":"center"}),
    dcc.Slider(
        id="year-slider",
        min = int(df["year"].min()),
        max = int(df["year"].max()),
        value = int(df["year"].min()),
        marks = {str(y): str(y) for y in sorted(df["year"].unique())},
        step=None,
        tooltip= {"placement": "bottom", "always_visible": True},
    ),
    
    return heading_text, paragraph_text, links_list

    html.Br(),
    dcc.Graph(id="chloropleth-map")

],
)

@callback(
    Output("chloropleth-map", "figure"),
    Input("year-slider", "value")
)

def update_map(selected_year):
    d = df[df["year"] == selected_year]
    fig = px.choropleth(
        d,
        locations="state",
        locationmode="USA-states",
        color="prices",
        scope="usa",
        color_continuous_scale="Reds",
        labels = {"Price": "Price (cents/kWh)"},
        title = f"Residential Electricity Prices -> {selected_year}"
    )
    fig.update_layout(geo=dict(bgcolor="#B9975B"), #bg color around the map
                      paper_bgcolor="#32453C", # full figure bg color
                      font_color="white", #font color
                      margin= dict(l=10, r=10, t=50, b=10)) #margins around map
    return fig