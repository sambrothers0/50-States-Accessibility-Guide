<<<<<<< HEAD
=======
from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/webscrape2", name="Web Scrape 2")

# web scrape packages
import requests
from bs4 import BeautifulSoup

# US states list for dropdown
us_states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
    'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
    'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
    'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
    'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
    'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
    'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

layout = html.Div(
    children=[
        # Heading with a dynamic ID
        html.H2(
            "See Disability Support Resources in Virginia",
            id="heading"
        ),
        # Paragraph with a dynamic ID
        html.P(
            "Right now, this page is displaying resources in Virginia.",
            id="paragraph"
        ),
        html.P(
            "Please select your state below:"
        ),
        # Dropdown input section
        html.Div(
            children=[
                dcc.Dropdown(
                    id="state-dropdown",
                    options=[{'label': state, 'value': state} for state in us_states],
                    value='Virginia',  # Default value
                    clearable=False
                ),
            ]
        ),
        # Placeholder for links
        dcc.Loading(
            id="loading-spinner",
            type="circle",
            children=[
                html.Div(
                    id="links-list",
                    children=[
                        html.P("Links for your state would appear here.")
                    ]
                )
            ]
        ),
        html.P(
            "See services in all states: "
        ),
        html.A("https://www.disabilityresources.org/state-services")
    ]
)

# Define the callback to update the content
@callback(
    # Output to update the children of the heading and paragraph
    Output("heading", "children"),
    Output("paragraph", "children"),
    Output("links-list", "children"),
    # Input from the dropdown's value
    Input("state-dropdown", "value")
)

def update_state(state_choice):
    # Trigger web scrape, update state choice
    if not state_choice:
        return (
            "See Disability Support Resource Centers in Virginia",
            "Right now, this page is displaying resources in Virginia.",
            html.P("Links for your state would appear here.")
        )

    # Convert state name to lowercase for URL and replace spaces with hyphens
    state_url_name = state_choice.lower().replace(" ", "-")

    # URL of the page to scrape
    url = f'https://www.disabilityresources.org/{state_url_name}.html'

    # Perform web scrape
    try:
        req = requests.get(url, timeout=5)
        soup = BeautifulSoup(req.text, 'lxml')
        
        # Find the specific div containing the links
        resource_links = soup.find('div', {'id': 'message-text-9bc4e092-e962-40aa-af8d-4b783e05154a'}).find_all('a')
        
        links_list = []
        for link in resource_links:
            link_url = link.get('href')
            link_text = link.get_text(strip=True)
            if link_url and link_text:
                links_list.append(
                    html.Div([
                        html.A(link_text, href=link_url, target="_blank")
                    ])
                )
        
        # If no links are found, provide a message
        if not links_list:
            links_list.append(html.P("No specific resources found for this state."))

    except requests.exceptions.RequestException:
        links_list = [html.P("Error fetching resources. Please try again later.")]
        
    # Update the heading and paragraph
    heading_text = f"See Disability Support Resource Centers in {state_choice}"
    paragraph_text = f"Right now, this page is displaying resources in {state_choice}."
    
    return heading_text, paragraph_text, links_list
>>>>>>> 65f1826713b8454a7c7b7e0a7d2dd0fc5746f5a1
