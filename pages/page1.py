import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
import pandas as pd
import plotly.express as px


dash.register_page(__name__, path="/page1", name="Page 1")

#Load the dataset
file_path = "data/DisabilityRankedStates.csv"
df = pd.read_csv(file_path)


#Chloropleth map
fig = px.choropleth(
    df,
    locations = "State",
    locationmode= "USA-states",
    color = "Points",
    title= f"Disability Friendliness by State",
    scope= "usa",
    labels = {"State": "Disability Friendly Rank"},
    color_continuous_scale= "Cividis",
    range_color= (0, 225)
)




layout = html.Div([
    #top row
    html.Div("Ranking of how disability friendly each state is", className="block"),
    dcc.Graph(figure=fig)
])