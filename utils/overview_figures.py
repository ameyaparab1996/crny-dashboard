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

status_df = pd.read_csv("data/status.csv")
status_df['formatted_percentage'] = status_df['percentage'].apply(lambda x: f'{round(x, 2)}%')

# PLOT BAR CHART:
status_bar_fig = px.bar(
    status_df,
    x='status',
    y='percentage',
    color='status',
    text='formatted_percentage',
    color_discrete_sequence= [colors.to_hex(plt.cm.get_cmap('plasma')(i)) for i in np.linspace(0.2, 0.8, len(status_df['status'].unique()))],
    width=600,
    height=500
)

status_bar_fig.update_layout(
    plot_bgcolor=BG_TRANSPARENT,
    paper_bgcolor=BG_TRANSPARENT,
    bargap=0.2,
    showlegend=False,
    # hoverlabel=HOVERLABEL_TEMPLATE,
    margin=WITH_PADDING,
    coloraxis_showscale=False,
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        color=FONT_COLOR,
        visible=False,
        title=None
    ),
    xaxis=dict(
        categoryorder='total descending',
        showgrid=False,
        zeroline=False,
        title=dict(
            text='<i>Status of the Applicants</i>',
            font=dict(size=11),
            standoff=40
        )
    )
)

status_bar_fig.update_traces(
    #text=status_df['formatted_percentage'],
    textposition='outside',
    #marker_color=prevalence_by_disorder['Color'],
    width=0.5,
    marker=dict(line=dict(width=0)),
    # customdata=prevalance_by_disorder['EstimatedPeopleAffected'],
    # hovertemplate='%{y}%<br>Estimated Affected People: %{customdata} millions<extra></extra>'
    hovertemplate=None,
    hoverinfo='none'
)
