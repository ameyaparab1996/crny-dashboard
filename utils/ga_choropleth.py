import plotly.express as px
import pandas as pd
from utils.utils_config import BG_TRANSPARENT
from urllib.request import urlopen
import json

# FIGURE:
def create_choropleth_fig():
    #with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    #    counties = json.load(response)
        
    with open('data/counties_data.json', 'r') as f:
        counties = json.load(f)
    county_status_df = pd.read_csv('data/counties.csv')
    fig = px.choropleth(
        county_status_df,
        geojson=counties,
        locations='fips',
        color='Number of Artists',
        scope='usa',
        color_continuous_scale="Agsunset",
        range_color=[min(county_status_df['Number of Artists']), max(county_status_df['Number of Artists'])],
        #title='Distribution of Artists by County',
        labels={'color': 'Population'},
        hover_name='county',
        hover_data={'fips': False, 'county': False, 'Number of Artists': True},
        #height='auto',
        #width=800,
        animation_frame='community'
    )
    fig.update_layout(#title_text="Distribution of Artists by County", 
                       title_x=0.5, title_font_size=24)
    fig.update_geos(fitbounds="locations")
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 3000, "redraw": True}, "mode": "immediate", "transition": {"duration": 2000}}],
                        "label": "Play",
                        "method": "animate",
                    },
                    {
                        "args": [[None], {"frame": {"duration": 3000, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate",
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 40},
                "showactive": False,
                "type": "buttons",
                "x": 0.2,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top",
            }
        ],
        sliders=[
            {
                "active": 0,
                "yanchor": "top",
                "xanchor": "left",
                "currentvalue": {
                    "font": {"size": 16},
                    "prefix": "Community: ",
                    "visible": True,
                    "xanchor": "right"
                },
                #"transition": {"duration": 3000},  # Adjust the animation duration here (in milliseconds)
                "pad": {"b": 10, "t": 50},
                "len": 1,
                "x": 0,
                "y": 0,
                "steps": []
            }
        ],
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        autosize=True
    )

    return fig
