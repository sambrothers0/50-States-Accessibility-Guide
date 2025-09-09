#app.py
import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
import dash_bootstrap_components as dbc

#initialize the app
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, title="Multi Page App")

server = app.server #for deployment

app.layout = html.Div([
    html.H1("50 States Accessibility Guide", className="app-title"),
    html.Div([
        html.Img(src="/assets/img/Disability_Symbols_Blog.webp", className="landing-image"),
    ], className="image-banner"),
    html.H2("A guide to help you find accessible places in the US", className="landing-header"),
    html.H3("The problem our website seeks to address is the gap in availability of travel information on accessibility."
            " Our goal is to fill this gap with an informative and visually compelling webpage that provides rich"
            " accessibility data from live APIs. We've chosen to focus on all US states to be as comprehensive as"
            " possible, while still keeping our topic narrow and focused.", className="landing-subtitle"),
    html.H2("Take a look around", className="landing-header"),
    html.H3("Our website includes several features which make it easier for users to view and understand accessibility data. "
            " There is an interactive map that displays accessibility ratings for each state, allowing users to quickly identify"
            " areas with high or low accessibility. The info page features more comprehensive disability data, which can't be"
            " succinctly viewed from just the map. We have also included a collection of disability advocacy groups for getting directly involved with the"
            " disabled community. This project provides a helpful place for people who are concerned with accessibility"
            " to find travel information across the states, whether or not you are American.", className="landing-subtitle"),
    dbc.Navbar(
        dbc.Container([
            dbc.Nav(
                [
                    dbc.NavLink("Map", href="/", active="exact"),
                    dbc.NavLink("Info", href="/info", active="exact"),
                    dbc.NavLink("Involvement", href="/involvement", active="exact")
                ],
                className="custom-navbar"
            ),
        ]),
        color="light",
        dark=False,
        className="mb-4"
    ),
    page_container
])

if __name__ == "__main__":
    app.run(debug=True)