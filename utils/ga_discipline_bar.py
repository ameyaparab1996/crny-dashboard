import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px
from matplotlib import colors
#from utils.process_data import all_disorders_dataframes
from utils.utils_config import BG_TRANSPARENT

WITH_PADDING = dict(pad=15, t=0, b=0, l=0, r=0)
HOVERLABEL_TEMPLATE = dict(
    bgcolor='rgba(11, 6, 81, 0.8)',
    bordercolor='rgba(11, 6, 81, 0.8)',
    font=dict(
        color='white'
    )
)
FONT_COLOR = '#5D5D5D'

disciplinecount_df = pd.read_csv("data/disciplines.csv")
disciplinecount_df.rename(columns={"count":"Number of Artists"},inplace=True)

# PLOT BAR CHART:
discipline_bar_fig = px.bar(
            disciplinecount_df,
            y="approach",
            x="Number of Artists",
            color="Public Value of Art",
            color_discrete_sequence=["#bd2e95","#a37cf0","#682bd7"],
            animation_frame="discipline",
            hover_name='approach',
            hover_data={'Public Value of Art' : True, 'approach': False, 'discipline': False, 'Number of Artists': True},
            range_x=[0, 5000],
        )

discipline_bar_fig.update_layout(
    plot_bgcolor=BG_TRANSPARENT,
    paper_bgcolor=BG_TRANSPARENT,
    yaxis_title="<i>Approach of Art Practice</i>",
    xaxis_title="<i>Number of Artists</i>",
    #title_text="Discipline and Approach of Artists",
    title_x=0.5,
    title_font_size=24,
    autosize=True,
    #yaxis=dict(tickangle=-90),
    xaxis=dict(showline=True, linecolor='black', showgrid=True, gridcolor='gray',griddash='dash'),
    updatemenus=[
        {
            "direction": "left",
            "pad": {"l": 20, "t": 40},
            "showactive": False,
            #"type": "buttons",
            "x": -0.3,
            "xanchor": "left",
            "y": -0.1,
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
                "prefix": "Discipline: ",
                "visible": True,
                "xanchor": "right"
            },
            "pad": {"b": 10, "t": 50},
            "len": 1.5,
            "x": -0.3,
            "y": -0.1
        }
    ]
)