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
    scope= "usa",
    labels = {"Points": "Disability Friendly Rank"},
    color_continuous_scale= "Cividis",
    range_color= (0, 225)
)

fig.update_Layout(
    title_text="Disability Friendliness by State",
    geo=dict(showlakes=True, Lakecolor="grey"),
    margin={"r":0,"t":40, "l":0, "b":0}
)




layout = html.Div([
    #top row
    html.Div("Ranking of how Disability Friendly each State is", className="block block-top"),
    dcc.Graph(figure=fig),
    html.Div("Footer", className= "block block-footer")
])