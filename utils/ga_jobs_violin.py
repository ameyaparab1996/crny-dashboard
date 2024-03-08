import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib as plt
import plotly.express as px
from matplotlib import colors
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

job_violin_df = pd.read_csv("data/jobs.csv")

jobs_violin_fig = go.Figure()


jobs_violin_fig.add_trace(go.Violin(x=job_violin_df['earning_mode'][job_violin_df['debt'] == 'Yes'],
                            y=job_violin_df['income'][job_violin_df['debt'] == 'Yes'],
                            name='Yes',
                            box_visible=True,
                            legendgroup='Yes',
                            scalegroup='Yes',
                            side='negative',
                            line_color=[colors.to_hex(plt.cm.get_cmap('plasma')(i)) for i in np.linspace(0.1, 0.8, len(job_violin_df['debt'].unique()))][0],
                            jitter=0.2,
                            opacity=0.6,
                            hoverinfo='x+name', hoverinfosrc=None, hoverlabel=None, hoveron=None, hovertemplate=None, hovertemplatesrc=None, hovertext=None, hovertextsrc=None))
jobs_violin_fig.add_trace(go.Violin(x=job_violin_df['earning_mode'][job_violin_df['debt'] == 'No'],
                            y=job_violin_df['income'][job_violin_df['debt'] == 'No'],
                            name='No',
                            box_visible=True,
                            legendgroup='No',
                            scalegroup='No',
                            side='positive',
                            line_color=[colors.to_hex(plt.cm.get_cmap('plasma')(i)) for i in np.linspace(0.1, 0.8, len(job_violin_df['debt'].unique()))][-1],
                            jitter=0.2,
                            opacity=0.6,
                            hoverinfo='x+name', hoverinfosrc=None, hoverlabel=None, hoveron=None, hovertemplate=None, hovertemplatesrc=None, hovertext=None, hovertextsrc=None))
jobs_violin_fig.update_layout(
    #title_text="Income Distribution Across Employment Types",
    legend=dict(
        title='Currently in Debt'
    ),
    xaxis_title="<i>Mode of Earning</i>",
    yaxis_title="<i>Household Income</i>",
    violingap=0.2,
    violingroupgap=0.1,
    violinmode='overlay',
    #width=750,
    height=600,
    autosize=True,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor= 'rgba(0, 0, 0, 0)',
    xaxis=dict(tickangle=-90),
    yaxis=dict(showline=True, linecolor='black', showgrid=True, gridcolor='gray',griddash='dash')
)