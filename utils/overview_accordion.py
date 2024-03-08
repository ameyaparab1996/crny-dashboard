import dash_mantine_components as dmc
from dash import html

characters_list = [
    {
        "id": "accumulatedebt",
        "image": "https://img.icons8.com/external-nawicon-mixed-nawicon/64/6a00a8/external-Debt-recession-nawicon-mixed-nawicon-2.png",
        "label": "Accumulated Debt",
        "description": "Financial Strain",
        "content": "Many artists faced accumulating debt as a result of canceled performances, exhibitions, and other income-generating opportunities, highlighting the financial challenges and vulnerabilities within the creative community.",
    },
    {
        "id": "anxiety",
        "image": "https://img.icons8.com/ios/50/8b0aa5/shaking.png",
        "label": "Anxiety",
        "description": "Navigating Uncertainty",
        "content": "The COVID-19 lockdown exacerbated anxiety among artists, who grappled with uncertainty about the future of their careers, financial instability due to canceled gigs and exhibitions, and the isolation from their usual creative communities, intensifying feelings of stress and apprehension.",
    },
    {
        "id": "caregiver",
        "image": "https://img.icons8.com/pastel-glyph/64/a82296/trust--v1.png",
        "label": "Became a Caregiver",
        "description": "Artists as Caregivers",
        "content": "Some artists stepped into caregiving roles, balancing their creative pursuits with the responsibilities of caring for loved ones, showcasing resilience and compassion in the face of adversity.",
    },
    {
        "id": "foodinsecurity",
        "image": "https://img.icons8.com/external-others-pike-picture/50/c13b82/external-Hunger-poverty-others-pike-picture-2.png",
        "label": "Food Insecurity",
        "description": "Starving Creativity",
        "content": "As the pandemic unfolded, artists found themselves facing the harsh reality of food insecurity, with dwindling income streams and limited access to resources, challenging their ability to sustain both their creative passions and basic nutritional needs.",
    },
    {
        "id": "housinginsecurity",
        "image": "https://img.icons8.com/external-tanah-basah-glyph-tanah-basah/48/d5536f/external-homeless-recession-tanah-basah-glyph-tanah-basah.png",
        "label": "Housing Insecurity",
        "description": "Sheltering Struggles",
        "content": "COVID-19 exacerbated housing insecurity for artists, as lost income and instability in the arts sector left many struggling to afford rent and facing the threat of eviction, amplifying the challenges of maintaining stable housing in uncertain times.",
    },
    {
        "id": "loneliness",
        "image":"https://img.icons8.com/external-stick-figures-gan-khoon-lay/51/e66c5c/external-alone-suicide-stick-figures-gan-khoon-lay.png",
        "label": "Loneliness",
        "description": "Echoes of Solitude",
        "content": "Social isolation, canceled events, and the absence of in-person collaboration deepened feelings of loneliness among artists highlighting the emotional toll of navigating creative pursuits in solitary environments.",
    },
    {
        "id": "sickness",
        "image": "https://img.icons8.com/ios-filled/50/f48849/protection-mask.png",
        "label": "Sickness",
        "description": "Health in Crisis",
        "content": "Amid the COVID-19 pandemic, artists confronted sickness and health challenges, grappling with the virus's impact on their physical well-being and creative endeavors, underscoring the vulnerability of artistic communities to the pandemic's health effects."
    },
    {
        "id": "forcedtomove",
        "image": "https://img.icons8.com/ios-filled/50/fca636/leave-house.png",
        "label": "Forced to Move",
        "description": "On the Move",
        "content": "The years 2020 - 2022 intensified financial burdens for artists relocating to new places, amplifying the challenges of securing stable income and resources amidst uncertain transitions."
    }
]


def create_accordion_label(label, image, description):
    return dmc.AccordionControl(
        dmc.Group(
            [
                dmc.Avatar(src=image, radius="xl", size="lg"),
                html.Div(
                    [
                        dmc.Text(label),
                        dmc.Text(description, size="sm", weight=400, color="dimmed"),
                    ]
                ),
            ]
        )
    )


def create_accordion_content(content):
    return dmc.AccordionPanel(dmc.Text(content, size="sm"))


impacts_accordion = dmc.Accordion(
    chevronPosition="right",
    variant="contained",
    children=[
        dmc.AccordionItem(
            [
                create_accordion_label(
                    character["label"], character["image"], character["description"]
                ),
                create_accordion_content(character["content"]),
            ],
            value=character["id"],
        )
        for character in characters_list
    ],
)
