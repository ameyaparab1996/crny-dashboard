import dash
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import plotly.graph_objects as go
from dash import html, dcc, callback, Input, Output, State, clientside_callback, no_update, Patch, ctx, \
    ClientsideFunction
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
from utils.ga_utils import create_county_title
from utils.ga_community_bar import community_bar_fig
from utils.ga_discipline_bar import discipline_bar_fig
from utils.ga_choropleth import create_choropleth_fig
from utils.utils_config import FIG_CONFIG_WITH_DOWNLOAD, FIG_CONFIG_WITHOUT_DOWNLOAD, BG_TRANSPARENT, MAIN_TITLE_COLOR, HIDE, \
    STORAGE_SESSION, add_loading_overlay

pd.set_option('display.float_format', '{}'.format)
county_status_df = pd.read_csv('data/counties.csv')
ethnicity_df = pd.read_csv('data/ethnicities.csv')
ethnicity_df.rename(columns={"immigrant": "Immigrant"},inplace=True)
ethnicity_df['percentage'] = ethnicity_df['percentage'].apply(lambda x: f'{round(x, 2)}%')
ethnicity_list = ethnicity_df["ethnicity"].unique()

CHOROPLETH_INTERVAL = 50
SLIDER_YEAR_INCREMENT = 10
is_first_session = True

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

dash.register_page(
    __name__,
    path='/location-analysis',
    order=1,
    title='CRNY Dashboard',
    description="""
    Discover in-depth analysis of mental health prevalence based on location, age, and gender. This interactive page 
    allows exploration of mental health trends across countries, continents, and demographic groups.
    """,
    image='miniature.png'
)

layout = html.Div(
    [
        dmc.Grid(
            [
                dmc.Col(
                    [
                        html.Br(),
                        html.Img(src='assets/location.png', style={'width': 150, 'height': 'auto'})
                    ],

                    offsetLg=2,
                    lg=2
                ),
                dmc.Col(
                    [

                            dmc.Title(
                                    'Where are these Artists from?',
                                    color=MAIN_TITLE_COLOR,
                                    align='left',
                                    order=1
                             ),
                            dmc.Text(
                            "Artists in New York State are dispersed across a wide spectrum of locations, reflecting the rich diversity of the state's geography. From the bustling urban landscapes of New York City to the tranquil rural areas of upstate New York, and the vibrant suburbs in between, artists contribute to the cultural fabric of communities across the state. This geographical diversity not only influences the artistic expressions and experiences of these individuals but also underscores the importance of understanding and supporting artists in their local contexts.",
                            align='justify',
                            color='#4B4B4B',
                            mt='md'
                            )
    
                        
                    ],

                    #offsetLg=,
                    lg=7
                )
               
            ],
        ),

        dmc.Grid(
            [
                dmc.Col(
                    [
                        dmc.Container(
                            [
                                dcc.Graph(figure=community_bar_fig,
                                          id='community-fig'),
                            ],
                            mt='lg',
                            px=0
                        )
                    ],
                    offsetLg=1,
                    lg=3,
                    #span=1
                ),
                dmc.Col(
                    [
                        html.Br(),
                        dcc.Graph(figure=create_choropleth_fig(),id='choropleth-fig')
                    ],
                    #lg=5,
                    lg=8,
                    offsetLg=-0.5,
                    #span=2
                )
            ],
            #columns=4,
            #mt=35,
            #mb=100,
            gutter="xl"
        ),
        html.Br(),
        html.Br(),
        dmc.Grid(
            [
                dmc.Col(
                    [

                                dmc.Title(
                                    'How does diversity shape Artistic communities?',
                                    color=MAIN_TITLE_COLOR,
                                    align='left',
                                    order=1
                                ),

                        dmc.Text(
                            "The gender identity of artists encompasses a spectrum of diverse expressions, reflecting the multifaceted nature of human experience. In the context of artistic communities, gender identities often intersect, meaning that individuals may identify with multiple gender identities simultaneously or transition between different identities fluidly. This intersectionality adds complexity to the understanding of gender and highlights the need for inclusive spaces that embrace diverse gender expressions. It also underscores the importance of recognizing and respecting each individual's unique journey of self-discovery and self-expression within the artistic realm.",
                            align='justify',
                            color='#4B4B4B',
                            mt='md'
                        )
                    ],

                    offsetLg=1,
                    lg=10
                )
            ],
        ),
        html.Br(),
        html.H3("Gender Identity Diversity & Intersection Among Artists",
                style={"textAlign": "center"}),
        dmc.Grid(
            [

                    html.Img(src='assets/upset_plot.png', style={'width': '80%', 'height': 'auto'})
            ],
            justify ='center',
            #columns=4,
            #mt=35,
            #mb=100,
            #gutter="xl"
        ),
        html.Br(),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        
                            html.H3(
                                "Cultural Diversity & Immigration in the Artistic Community",
                                style={"textAlign": "center"},
                            ),
                            dmc.Grid([
                                dmc.Col([
                                    dmc.Text(
                                        "Choose a scale:",
                                        align='center',
                                        color='#4B4B4B',
                                        mt='md'
                                    ),
                                    dcc.RadioItems(
                                        id="bar-polar-app-x-radio-items",
                                        options=["Absolute", "Logarithmic"],
                                        value="Logarithmic",
                                    ),
                                ],lg=3),
                                dmc.Col([
                                    dmc.Text(
                                        "Choose the Ethnicity:",
                                        align='center',
                                        color='#4B4B4B',
                                        mt='md'
                                    ),
                                    dcc.Dropdown(
                                        id="bar-polar-app-x-dropdown",
                                        value=ethnicity_list[:3],
                                        options=ethnicity_list,
                                        multi=True,
                                    ),
                                ],lg=8),]),
                            dcc.Graph(id="bar-polar-app-x-graph"),
                    ],
                    offsetLg=1,
                    lg=6
                ),
                dmc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H2(
                                "Melting Pot of Cultures",
                                style={"textAlign": "center"},
                                ),
                        dmc.Text(
                            'The ethnic identities of artists reflect a rich tapestry of cultural heritage and ancestral backgrounds, contributing to the diversity and vibrancy of artistic expression. In the artistic landscape, ethnic identities intersect with experiences of immigration and migration, highlighting the global nature of artistic communities. Many artists navigate the complexities of immigration, either as immigrants themselves or as descendants of immigrant families, bringing unique cultural perspectives and narratives to their work.',
                            align='justify',
                            color='#4B4B4B',
                            mt='md'
                        ),
                        dmc.Text(
                            'The immigration status of artists can shape their ability to access resources, opportunities, and recognition within the arts, emphasizing the need for inclusive policies and supportive environments for immigrant artists. Recognizing and celebrating the diversity of ethnic identities and immigration experiences enriches the artistic tapestry and fosters greater understanding and appreciation within the creative community.',
                            align='justify',
                            color='#4B4B4B',
                            mt='md'
                        )
                    ],
                    offsetLg=0.2,
                    lg=4,

                )
            ],
            #mt=35,
            #mb=100,
            gutter="xl"
        ),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        dmc.Title(
                                'How Do Artists Approach Their Practice?',
                                color=MAIN_TITLE_COLOR,
                                align='left',
                                order=1
                        ),
                        dmc.Text(
                            "Artists across diverse disciplines approach their art practice with unique perspectives and methodologies, each reflecting their individual creative process and artistic vision. From painters to sculptors, musicians to writers, and performers to filmmakers, artists draw inspiration from various sources, including personal experiences, cultural influences, and societal issues. Additionally, collaboration, interdisciplinary exchange, and community engagement are increasingly integral to contemporary art practices, fostering creativity, dialogue, and social impact. Support to these Artists can facilitate collaboration, community engagement, and public outreach initiatives, fostering connections between artists, audiences, and diverse communities",
                            align='justify',
                            color='#4B4B4B',
                            mt='md'
                        ),
                        html.H3(
                                "Artists' Practice, Public Impact & Disciplines",
                                style={"textAlign": "center"},
                            ),
                        dcc.Graph(figure=discipline_bar_fig,id='discipline-fig')
                    ],
                    lg=10,
                    offsetLg=0,
                    #span=3
                )
            ],
            justify ='center',
            #columns=4,
            #mt=35,
            #mb=100,
            gutter="xl"
        ),
        html.Br(),
        html.Br(),
    ],
    id='location-analysis-container',
    className='animate__animated animate__fadeIn animate__slow'
)

@callback(
    Output("bar-polar-app-x-graph", "figure"),
    Input("bar-polar-app-x-dropdown", "value"),
    Input("bar-polar-app-x-radio-items", "value"),
)
def update_graph(ethnicity, radius_scale):
    filtered_df = ethnicity_df[ethnicity_df["ethnicity"].isin(ethnicity)]
    
    log_r = True if radius_scale == "Logarithmic" else False

    fig = px.bar_polar(
        filtered_df,
        r=filtered_df["frequency"],
        theta=filtered_df["ethnicity"],
        color=filtered_df["Immigrant"],
        template="plotly_white",
        color_discrete_sequence=["#bd2e95","#a37cf0","#682bd7"],
        log_r=log_r,
        hover_name='ethnicity',
        hover_data={'ethnicity' : False, 'Immigrant': True, 'frequency': True, 'percentage': True}
    )
    
    fig.update_layout(
        plot_bgcolor=BG_TRANSPARENT,
        paper_bgcolor=BG_TRANSPARENT,
        autosize=True,
    )
    return fig