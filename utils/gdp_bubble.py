import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib as plt
import plotly.express as px
from matplotlib import colors

from utils.utils_config import BG_TRANSPARENT, HOVERLABEL_TEMPLATE


def create_bubble(df, switcher):

    step_x = 1
    step_y = 1

    max_x_range = [df['Age'].min() - step_x, df['Age'].max() + step_x]
    max_y_range = [df['Income'].min() - step_y, df['Income'].max() + step_y]

    if switcher:
        color_col = 'Can pay for financial emergency'
        color_sequence = [colors.to_hex(plt.cm.get_cmap('plasma')(i)) for i in np.linspace(0.1, 0.8, len(df['Can pay for financial emergency'].unique()))]
        #custom_data = ['financial_capacity']
        #hover_template = "<b>%{customdata[0]}</b><br>GDP: %{x}<br>Fi: %{y:.2f}%<extra></extra>"
    else:
        color_col = 'Financial Stability'
        color_sequence = [colors.to_hex(plt.cm.get_cmap('plasma')(i)) for i in np.linspace(0, 0.8, len(df['Financial Stability'].unique()))]
        #custom_data = ['Continent', 'financial_capacity']
        #hover_template = "<b>%{customdata[1]}</b><br>GDP: %{x}<br>Prevalence: %{y:.2f}%"

    fig = px.scatter(
        df,
        x='Age',
        y='Income',
        #animation_frame='Year',
        #animation_group='Entity',
        size='financial_capacity_num',
        opacity=0.5,
        color=color_col,
        color_discrete_sequence=color_sequence,
        hover_name = 'Financial Capacity',
        hover_data={'Age': True, 'Household Income': True, 'Financial Stability': True, 'financial_capacity_num': False},
        #custom_data=custom_data
    )

    fig.update_layout(
        paper_bgcolor=BG_TRANSPARENT,
        plot_bgcolor=BG_TRANSPARENT,
        xaxis_range=max_x_range,
        yaxis_range=max_y_range,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor='#7159a3',
            linewidth=3,
            showspikes=False,
            title='<i>Age</i>'
        ),
        yaxis=dict(
            showgrid=False,
            linecolor='#7159a3',
            linewidth=3,
            title='<i>Household Income</i>',
            ticksuffix="  ",
            zeroline=False
        ),
        #hovermode='x unified',
        #hoverlabel=HOVERLABEL_TEMPLATE,
        
    )

    fig.update_traces(
        #hovertemplate=hover_template
    )

    return fig

