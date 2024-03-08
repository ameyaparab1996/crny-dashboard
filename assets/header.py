import dash
from dash import dcc, html, Output, Input, State, clientside_callback, ClientsideFunction
import dash_mantine_components as dmc
from dash_iconify import DashIconify

GITHUB = 'https://github.com/ameyaparab1996/crny-dashboard'
CONTACT_ICON_WIDTH = 30


def modal_data_source():

    return dmc.Modal(
            id='modal-data-source',
            size='55%',
            styles={
                'modal': {
                    'background-color': '#f2f2f2',
                }
            },
            children=[
                dcc.Markdown(
                    [
                        """
                        
                        # About the Dataset
                        
                        CRNY launched the “Portrait of New York State Artists” survey in March 2022 to build a portrait of the needs, circumstances, and experiences of artists across New York State. CRNY will use data from this survey to conduct advocacy and narrative change work, and to assess whether the funding provided through the programs helps meet the needs of individual artists in any substantive or transformational ways.

                        Upon submission of an application to the Guaranteed Income for Artists or Artist Employment Program, artists were invited to answer additional questions, all optional, about their artistic practice, financial circumstances, well-being, pandemic experience, and attitudes about policy and advocacy matters.
                        
                        The first is data from the application that potential program enrollees completed to apply for the CRNY Guaranteed Income (GI) for Artists program. It includes information for all individuals who applied, regardless of whether they were ultimately accepted into the program. The second data source is the Portrait of Artists survey which CRNY administered with the goal of understanding the needs, circumstances, and experiences of artists in New York.
                        
                        """
                    ],
                )
            ]
        )


header = html.Div(
    dmc.Grid(
        [
            modal_data_source(),
            dmc.Col(
                [
                    dmc.Group(
                        [
                            dmc.ActionIcon(
                                [
                                    DashIconify(icon='bx:data', color='#C8C8C8', width=25)
                                ],
                                variant='transparent',
                                id='about-data-source'
                            ),
                            dmc.Anchor(
                                [
                                    DashIconify(icon='uil:github', color='#8d8d8d', width=CONTACT_ICON_WIDTH),
                                ],
                                href=GITHUB
                            )
                        ],
                        spacing='xl',
                        position='right'
                    )
                ],
                offsetMd=1,
                md=10,
            )
        ],
        mt='md',
        mb=35
    )
)


clientside_callback(
    ClientsideFunction(namespace='clientside', function_name='toggle_modal_data_source'),
    Output('modal-data-source', 'opened'),
    Input('about-data-source', 'n_clicks'),
    State('modal-data-source', 'opened')
)


