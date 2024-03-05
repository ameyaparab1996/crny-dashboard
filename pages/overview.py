import dash
from dash import html, dcc, callback, Input, Output, State, ctx, no_update, clientside_callback, ClientsideFunction
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import dash_extensions as de

from utils.overview_figures import disorder_bar_fig, graph_functions, prevalence_by_disorder
from utils.overview_accordion import disorders_accordion
from utils.utils_config import FIG_CONFIG_WITHOUT_DOWNLOAD, FIG_CONFIG_WITH_DOWNLOAD, BG_TRANSPARENT, MAIN_TITLE_COLOR, \
    add_loading_overlay

dash.register_page(
    __name__,
    path='/',
    order=0,
    title='Mental Health - Overview',
    description="""
    A comprehensive analysis of global mental health, focusing on the prevalence and impact of anxiety, depressive, 
    bipolar, schizophrenia, and eating disorders. Explore data-driven insights into mental health trends and their 
    effects on different demographics.
    """,
    image='miniature.png'
)


def estimate_case(estimate, disorder_name):
    return [
        dmc.Tooltip(
            label=f'Estimated affected people by {disorder_name} disorder in millions',
            children=[
                dmc.Group(
                    [
                        DashIconify(icon='fluent:people-team-16-regular', height=35,
                                    color=MAIN_TITLE_COLOR),
                        dmc.Title(f'{estimate}M', order=2, color=MAIN_TITLE_COLOR)
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
                                    'Exploring the Impact of Demographic, Economic, and Geographic Factors on Mental '
                                    'Health Disorders',
                                    color=MAIN_TITLE_COLOR,
                                    align='justify',
                                    order=1
                                ),
                                dmc.Text(
                                    'This application delves into the world of mental health, analyzing how '
                                    'demographic, economic, and geographic factors influence the prevalence and '
                                    'treatment of mental disorders across various populations and regions. Utilizing '
                                    'data from reputable sources, we aim to uncover disparities and trends in mental'
                                    'health management, shedding light on the challenges and opportunities for'
                                    'improved care.',
                                    color='#4B4B4B',
                                    mt='lg',
                                    mb=40,
                                    align='justify'
                                ),
                                disorders_accordion
                            ],
                            px=0
                        )
                    ],
                    offsetMd=1,
                    md=6
                ),
                dmc.Col(
                    [
                        dmc.Stack(
                            [
                                dmc.Container(id='estimate-container', px=0, children=[html.Div(id='group-estimate')]),
                                dcc.Graph(figure=disorder_bar_fig, config=FIG_CONFIG_WITH_DOWNLOAD,
                                          id='disorder-fig', clear_on_unhover=True),
                                dcc.Tooltip(
                                    id='tooltip-disorder-fig',
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
                    md=5
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
    Output('tooltip-disorder-fig', 'show'),
    Output('tooltip-disorder-fig', 'bbox'),
    Output('tooltip-disorder-fig', 'children'),
    Output('estimate-container', 'children'),
    Input('disorder-fig', 'hoverData'),
    State('estimate-container', 'children')
)
def update_disorder_tooltip(hover_data, current_estimated_container):

    if hover_data:
        bbox = hover_data['points'][0]["bbox"]
        label = hover_data['points'][0]['label']

        children = dmc.Container(
            [
                dmc.Text(f'{label} Disorder Prevalence (%)', italic=True, size='xs', color='white', mb=5),
                dcc.Graph(figure=graph_functions[label](), config=FIG_CONFIG_WITHOUT_DOWNLOAD)
            ],
            px=0
        )

        disorder_estimated_case = estimate_case(
            prevalence_by_disorder.query('Disorder == @label')['EstimatedPeopleAffected'].iloc[0], label
        )

        return True, bbox, children, disorder_estimated_case

    if not current_estimated_container[0]['props']['children']:
        disorder_estimated_case = estimate_case(
            estimate=prevalence_by_disorder.query("Disorder == 'Anxiety'")['EstimatedPeopleAffected'].iloc[0],
            disorder_name='Anxiety'
        )
    else:
        disorder_estimated_case = current_estimated_container

    return False, no_update, no_update, disorder_estimated_case


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
    Input('disorder-fig', 'hoverData'),
)

