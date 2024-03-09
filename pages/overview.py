import dash
import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.express as px
from matplotlib import colors
from dash import Dash, html, dcc, callback, Input, Output, State, ctx, no_update, clientside_callback, ClientsideFunction
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import dash_extensions as de

from utils.overview_figures import status_bar_fig
#from utils.overview_accordion import disorders_accordion
from utils.utils_config import FIG_CONFIG_WITHOUT_DOWNLOAD, FIG_CONFIG_WITH_DOWNLOAD, BG_TRANSPARENT, MAIN_TITLE_COLOR, \
    add_loading_overlay

status_df = pd.read_csv("data/status.csv")

dash.register_page(
    __name__,
    path='/',
    order=0,
    title='CRNY Dashboard',
    description="""
    Dive into the vibrant world of artists with this dynamic dashboard, where every click unveils a new chapter in their story. Explore a rich tapestry of figures and statistics, painting a vivid picture of their unique journeys and challenges. Engage with interactive features to delve deeper into the support they need, while narratives provide a captivating glimpse into their diverse challenges. Navigate through the pages to explore the colorful landscape of the artist community.
    """,
    #image='miniature.png'
)


def estimate_case(estimate, status):
    return [
        dmc.Tooltip(
            label=f'Artists with {status} grants',
            children=[
                dmc.Group(
                    [
                        DashIconify(icon='fluent:people-team-16-regular', height=35,
                                    color=MAIN_TITLE_COLOR),
                        dmc.Title(f'{estimate}', order=2, color=MAIN_TITLE_COLOR)
                    ],
                    position='center',
                    mb='lg',
                    id='group-estimate',
                ),
            ],
            withArrow=True,
            transition='fade'
        ),
    ]


layout = dmc.NotificationsProvider(
    [
        dmc.Grid(
            [
          
                dmc.Col(
                    [   
                        
                        dmc.Container(
                            [
                                dmc.Title(
                                    'Creatives Rebuild New York',
                                    color=MAIN_TITLE_COLOR,
                                    align='center',
                                    order=1
                                ),
                                html.H3(
                                "Unveiling the Artists' Story",
                                style={"textAlign": "center"},
                                ),
                                html.Br(),
                                dmc.Text(
                                    "An artist, culture bearer, or culture maker (referred to as 'artist' henceforth) embodies a creative spirit, regularly immersing themselves in artistic or cultural practices.",
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                                dmc.Grid([
                                    dmc.Col([
                                    html.Br(),
                                    html.H5(
                                            "Artists Aware of Guranteed Income",
                                            style={"textAlign": "center", "color":"#f48849"},
                                            ),
                                    html.H1(
                                            "24.66%",
                                            style={"textAlign": "center", "color": "#a82296"},
                                            )],
                                        lg=4),
                                    dmc.Col([
                                        dmc.Title(
                                            '12898',
                                            color=MAIN_TITLE_COLOR,
                                            align='center',
                                            order=1
                                        ),
                                        html.H4(
                                            "Total Applicants",
                                            style={"textAlign": "center"},
                                            )],
                                        lg=4),
                                    dmc.Col([
                                        html.Br(),
                                        html.H5(
                                                "Artists Experiencing Barriers",
                                                style={"textAlign": "center", "color":"#f48849"},
                                                ),
                                        html.H1(
                                            "3/4 th",
                                            style={"textAlign": "center", "color": "#a82296"},
                                            )],
                                        lg=4)
                                    ]),
                            
                                dmc.Text(
                                    "Dive into the vibrant world of artists with this dynamic dashboard, where every click unveils a new chapter in their story. Explore a rich tapestry of figures and statistics, painting a vivid picture of their unique journeys and challenges. Engage with interactive features to delve deeper into the support they need, while narratives provide a captivating glimpse into their diverse challenges. Navigate through the pages to explore the colorful landscape of the artist community.",
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                                #disorders_accordion
                            ],
                            px=0
                        )
                    ],
                    offsetLg=-1,
                    md=4.5
                ),
                dmc.Col(
                    [
                        dmc.Stack(
                            [
                                dmc.Container(id='estimate-container', px=0, children=[html.Div(id='group-estimate')]),
                                dcc.Graph(figure=status_bar_fig, config=FIG_CONFIG_WITH_DOWNLOAD,
                                          id='status-fig', clear_on_unhover=True),
                                dcc.Tooltip(
                                    id='tooltip-status-fig',
                                    direction='bottom',
                                    background_color='rgba(11, 6, 81, 0.8)',
                                    border_color='rgba(11, 6, 81, 0.8)',
                                    style={
                                        'border-radius': '4px',
                                        'color': 'white',
                                        'font-family': 'Helvetica, Arial, sans-serif'
                                    }
                                )
                            ],
                            id='right-container',
                            align='center'
                        )
                    ],
                    offsetLg=1.5,
                    md=2.5
                )
            ],
            justify='center',
            id='overview-container',
            className='animate__animated animate__fadeIn animate__slow'
        ),
        dmc.Container(id='notifications-container')
    ]
)


@callback(
    Output('tooltip-status-fig', 'show'),
    Output('tooltip-status-fig', 'bbox'),
    Output('tooltip-status-fig', 'children'),
    Output('estimate-container', 'children'),
    Input('status-fig', 'hoverData'),
    State('estimate-container', 'children')
)
def update_status_tooltip(hover_data, current_estimated_container):

    if hover_data:
        bbox = hover_data['points'][0]["bbox"]
        label = hover_data['points'][0]['label']

        children = dmc.Container(
            [
                dmc.Text(f'{label} (%)', italic=True, size='xs', color='white', mb=5),
                #dcc.Graph(figure=graph_functions[label](), config=FIG_CONFIG_WITHOUT_DOWNLOAD)
            ],
            px=0
        )

        status_estimated_case = estimate_case(
            status_df.query('status == @label')['frequency'].iloc[0], label
        )

        return True, bbox, children, status_estimated_case

    if not current_estimated_container[0]['props']['children']:
        status_estimated_case = estimate_case(
            estimate=status_df[status_df['status'] == 'Completed']['frequency'].iloc[0],
            status='Completed'
        )
    else:
        status_estimated_case = current_estimated_container

    return False, no_update, no_update, status_estimated_case


@callback(
    Output('notifications-container', 'children'),
    Input('notifications-container', 'id'),
)
def show_notifications(_):
    return [
        dmc.Notification(
            id='notif',
            title='Quick Navigation Tip',
            action='show',
            message=dmc.Container(
                [
                    "Use your keyboard's ", dmc.Kbd('←'), " and ", dmc.Kbd('→'), " to navigate"
                ],
                px=0
            ),
            autoClose=10000,
            radius='xl',
            icon=DashIconify(icon='material-symbols:privacy-tip-outline-rounded'),
        )
    ]


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='update_estimate_animation'),
    Output('group-estimate', 'className'),
    Input('status-fig', 'hoverData'),
)

