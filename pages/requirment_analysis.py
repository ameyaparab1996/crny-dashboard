import dash
import pandas as pd
import numpy as np
from dash import html, dcc, callback, Input, Output, State, ctx, no_update
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import dash_extensions as de
import plotly.express as px
from utils.ga_jobs_violin import jobs_violin_fig
from utils.gdp_bubble import create_bubble
from utils.overview_accordion import impacts_accordion
from utils.utils_config import FIG_CONFIG_WITHOUT_DOWNLOAD, FIG_CONFIG_WITH_DOWNLOAD, BG_TRANSPARENT, MAIN_TITLE_COLOR, \
    add_loading_overlay

dash.register_page(
    __name__,
    path='/requirement-analysis',
    order=2,
    title='CRNY Dashboard',
    description="""
    Artists face financial instability, limited access to resources, and inadequate support networks, highlighting the need for greater financial security, affordable healthcare, and robust community support.
    """,
    image='miniature.png'
)

wellbeing_df = pd.read_csv("data/wellbeing.csv")
causes_pie_df = pd.read_csv("data/causes.csv")
age_income_df = pd.read_csv("data/age_income.csv")
age_income_df['Financial Stability'] = age_income_df['financial_stability'].str[0:]
age_income_df['financial_capacity_num'] = (age_income_df['financial_capacity'].str[0].astype(int)) * 10
age_income_df['Financial Capacity'] = age_income_df['financial_capacity'].str[3:-1]
age_income_df.rename(columns={'age':'Age','income':'Income','finance_400_emergency':'Can pay for financial emergency','household_income_2021':'Household Income'},inplace=True)

layout = dmc.NotificationsProvider(
    [   
        
        dmc.Grid(
            [
                
                dmc.Col(
                    [
                        dmc.Container(
                            [
                                dmc.Title(
                                    'Why do Artists need support?',
                                    color=MAIN_TITLE_COLOR,
                                    align='center',
                                    order=1
                                ),
                                dmc.Text(
                                    'Artists face financial instability, limited access to resources, and inadequate support networks, highlighting the need for greater financial security, affordable healthcare, and robust community support.',
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                                impacts_accordion
                            ],
                        )
                    ],
                    offsetLg=-1.1,
                    #md=6,
                    lg=4.2
                ),
                dmc.Col(
                    [
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H3(
                                "Multifactorial Dynamics of Artists' Well-being",
                                style={"textAlign": "center"},
                                ),
                            dmc.Stack([
                                dmc.Container([
                                html.Br(),
                                dcc.Dropdown(
                                        id="image-dropdown", options=wellbeing_df.wellbeing_impact_2020_2022.unique()[0:-1], value="Overall Impact",
                                        style={'width': '300px'}
                                    ),]),
                                dcc.Loading(html.Img(id='image-display', src='',width='120%' ),type="circle"),
                            ])
                    ],
                    lg=5
                )
            ],
            justify='center',
            #columns=6,
            id='overview-container',
        ),
        html.Br(),
        html.Br(),
        dmc.Grid(
            [
       
                dmc.Col(
                    [       
                        
                            dmc.Stack([
                                dmc.Container([
                                    html.H3(
                                            "Engagement in Various Causes",
                                            style={"textAlign": "center"},
                                            ),
                                    dmc.Grid(
                                        [
                                            
                                            dmc.Col([dmc.Text(
                                                        'Artists belong to a group that can influence policy on government: ',
                                                        color='#4B4B4B',
                                                        align='justify'
                                                    )],
                                                    #offsetLg=0.2,
                                                    lg=7),
                                            dmc.Col([dcc.RadioItems(
                                                        id="data",
                                                        options=["Yes", "No"],
                                                        value="Yes",
                                                    ),],
                                                    #offsetLg=0,
                                                    lg=3),
                                        ],
                                        #columns=4,
                                        )
                                ]),
                                dcc.Loading(dcc.Graph(id="graph"), type="circle"),
                            ])
                    ],
                    offset=-0.5,
                    lg=5
                ),
                dmc.Col(
                    [
                        dmc.Container(
                            [
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.H2(
                                "Empowering Advocates",
                                style={"textAlign": "center"},
                                ),
                                html.H4(
                                "Supporting Artists in Influencing Government Policy",
                                style={"textAlign": "center"},
                                ),
                                dmc.Text(
                                    'Artists who belong to groups with the ability to influence government policy serve as powerful advocates for the arts and cultural sectors. Their unique perspectives and connections enable them to effectively communicate the importance of supporting artistic endeavors and creative industries to policymakers. By providing financial support to these artists, we acknowledge their invaluable contributions and empower them to dedicate more time and resources to their advocacy efforts. This support not only strengthens the arts community but also fosters a more vibrant and diverse cultural landscape, enriching society as a whole.',
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                            ],
                        )
                    ],
                    #md=6,
                    #offset=0.5,
                    lg=4.5
                ),
            ],
            justify='center',
            #columns=6,
            id='overview-container',
        ),
        dmc.Grid(
            [
       
                dmc.Col(
                    [       
                            html.H2(
                                "Navigating the Financial Landscape",
                                style={"textAlign": "center"},
                                ),
                            html.H4(
                                "Supporting Artists' Economic Empowerment",
                                style={"textAlign": "center"},
                                ),
                            dmc.Text(
                                    'Artists, with their diverse employment statuses including part-time, full-time, contract, and unemployment, navigate a complex financial landscape. Part-time artists juggle multiple income streams, often leading to fluctuating earnings. Full-time artists pursue stability but contend with the challenge of maintaining consistent income. Contract artists relish flexibility yet grapple with sporadic work opportunities and financial uncertainty. Unemployed artists face significant financial strain, necessitating additional support to meet their basic needs.',
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                            dmc.Text(
                                    "Household income, influenced by employment status and artistic endeavors, profoundly impacts an artist's financial stability and debt management capabilities. Age dynamics further shape financial pressures, as younger artists encounter different challenges compared to their older counterparts. Unexpected financial emergencies, like medical expenses or sudden job loss, pose significant hurdles for artists of all employment statuses, highlighting the imperative of proactive financial planning and robust support networks within the artistic community.",
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                    ],
                    offsetLg=0,
                    lg=4
                ),
                dmc.Col(
                    [
                    
                        dmc.Container(
                            [
                                html.H3(
                                    "Income Distribution Across Employment Types",
                                    style={"textAlign": "center"}
                                ),
                                dcc.Graph(figure=jobs_violin_fig,id='jobs-fig'),
                                
                            ],
                        ),
                       
                    ],
                    #md=6,
                    offsetLg=0.5,
                    lg=5.5
                ),
            ],
            justify='center',
            #columns=6,
            id='overview-container',
        ),
        html.Br(),
        dmc.Grid(
            [
                dmc.Col(
                    [   
                        html.H3(
                            "Interplay of Income, Age, Financial Stability & Financial Capacity",
                            style={"textAlign": "center"},
                        ),
                        dmc.Center(
                            [
                                dmc.Tooltip(
                                    [
                                        dmc.Switch(
                                            onLabel=DashIconify(icon='streamline:bag-dollar', height=15),
                                            offLabel=DashIconify(icon='carbon:piggy-bank', height=15),
                                            size='md',
                                            color='violet',
                                            id='switch-continent-incomes',
                                            persistence=True,
                                            #persistence_type=STORAGE_SESSION,
                                        )
                                    ],
                                    label='Toggle to filter data by Financial Emergency or Financial Stability',
                                    transition='fade',
                                    withArrow=True
                                )
                            ]
                        )
                    ],
                    offsetLg=1,
                    lg=10,
                )
            ]
        ),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        
                        add_loading_overlay(
                            elements=[
                                html.Div(
                                    dcc.Graph(
                                        id='bubble-fig',
                                        figure=create_bubble(
                                            age_income_df,
                                            switcher=False
                                        )
                                    ),
                                    id='bubble-container'
                                )
                            ]
                        ),
                        dmc.Text(
                                    'Providing financial support to artists is crucial for fostering economic stability, enabling them to focus on their craft, pursue opportunities, and contribute to society. This investment in creativity enhances individual well-being and strengthens the cultural landscape, benefiting communities and economies.',
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                    ],
                    offsetLg=1,
                    lg=9.5
                )
            ],
            mt='lg'
        ),
    ]
)


@callback(
    Output('image-display', 'src'),
    [Input('image-dropdown', 'value')]
)
def update_image(value):
    return 'assets/' + value + '.png'

    
@callback(
    Output("graph", "figure"),
    Input("data", "value")
)
def generate_chart(data):
    if data == 'Yes':
      pie_df = causes_pie_df[causes_pie_df['policy_group'] == 'Yes']
    else:
      pie_df = causes_pie_df[causes_pie_df['policy_group'] == 'No']
    fig = px.pie(pie_df,
                 values='count',
                 names='causes_participation',
                 hover_name='causes_participation',
                 hover_data={'causes_participation' : False, 'policy_group': False, 'count': False},
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 width=600,
                 height=400)
                 
    fig.update_layout(
        plot_bgcolor=BG_TRANSPARENT,
        paper_bgcolor=BG_TRANSPARENT
    )
    return fig
    
@callback(
    Output('bubble-container', 'children'),
    Input('switch-continent-incomes', 'checked'),
    prevent_initial_call=True
)
def update_bubble_fig(switcher: bool):
    df = age_income_df

    fig = create_bubble(
        df=df,
        switcher=switcher
    )

    return dcc.Graph(id="bubble-fig", figure=fig)


