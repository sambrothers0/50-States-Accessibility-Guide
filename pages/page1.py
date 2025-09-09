import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
from pathlib import Path
import pandas as pd
import plotly.express as px


dash.register_page(__name__, path="/", name="Map")

#Load the dataset
Data_Path = Path(__file__).resolve().parent.parent / "data" / "DisabilityRankedStates.csv"
df = pd.read_csv(Data_Path)


#Chloropleth map
fig = px.choropleth(
    df,
    locations = "State",
    locationmode= "USA-states",
    color = "Points",
    scope= "usa",
    labels = {"Points": "Disability Friendly Rank"},
    color_continuous_scale= "Cividis",
    range_color= (0, 225)
)

fig.update_layout(
    title_text="Disability Friendliness by State",
    geo=dict(showlakes=True, lakecolor="lightblue"),
    margin={"r":0,"t":40, "l":0, "b":0}
)




layout = html.Div([
    html.Div([
        html.H3("Mapping Accessibility Through Aggregated Scores", className="map-header"),
        html.P("This map displays the disability friendliness of each US state, ranked numerically by points. "
               "The ranking is aggregated from scores on various factors such as housing, healthcare, employment opportunities, "
               "and social inclusion for people with disabilities. States with higher points are considered more "
               "disability-friendly, while those with lower points may have more challenges in providing adequate "
               "support and resources for individuals with disabilities. Data is sourced from AAA State of Play rankings.",
               className="map-subheader")
    ]),
    dcc.Graph(figure=fig)
])