from dash import dcc, html
from src.components.bar_graph import temperature_df as bargraph_df
from src.components.map import temperature_df as map_df

# Style global pour les titres
TITLE_STYLE = {
    "fontSize": "1.4em",
    "fontWeight": "bold",
    "color": "#333",
    "margin": 0
}

# Style pour les boîtes du dashboard
NEOMORPHISM_BOX_STYLE = {
    "backgroundColor": "#ffffff",
    "borderRadius": "12px",
    "boxShadow": "0 5px 15px rgba(0, 0, 0, 0.2)",
    "padding": "20px"
}

def centralized_layout():
    """
    Définit le layout principal du dashboard.
    Retourne une structure HTML composée d'une barre de titre et deux rangées principales :
    - Ligne 1 : Sélection de département + graphiques bar/histogramme
    - Ligne 2 : Sélection de date + carte + camembert
    """
    return html.Div(
        style={
            "display": "flex",
            "flexDirection": "column",
            "height": "100vh",
            "width": "98vw",
            "margin": "auto",
            "padding": "20px 0",
            "backgroundColor": "#fff",
            "fontFamily": "Arial, sans-serif"
        },
        children=[
            # Barre de titre
            html.Div(
                [
                    html.H2("Dashboard Météo", style=TITLE_STYLE)
                ],
                style={
                    **NEOMORPHISM_BOX_STYLE,
                    "flex": "0",
                    "textAlign": "center",
                    "margin": "0 auto 20px"
                }
            ),

            # Conteneur principal
            html.Div(
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "flex": "1",
                    "gap": "10px"
                },
                children=[
                    # Ligne 1 : Dépt. + Bargraph + Histogram
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "row",
                            "flex": "1",
                            "gap": "10px"
                        },
                        children=[
                            # Boîte sélection département
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "0.3",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Sélection Département",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.Dropdown(
                                        id="departement-dropdown",
                                        options=[
                                            {"label": dept, "value": dept}
                                            for dept in sorted(bargraph_df["Département"].unique())
                                        ],
                                        value=sorted(bargraph_df["Département"].unique())[0],
                                        placeholder="Sélectionnez un département",
                                        style={"width": "200px", "margin": "0 auto"}
                                    ),
                                ]
                            ),

                            # Boîte Bargraph
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "1",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Graphique des Températures",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.Graph(
                                        id="temperature-bargraph",
                                        config={"responsive": True},
                                        style={"width": "100%", "flex": "1"}
                                    ),
                                ]
                            ),

                            # Boîte Histogram
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "1",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Histogramme des Températures",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.Graph(
                                        id="temperature-histogram",
                                        config={"responsive": True},
                                        style={"width": "100%", "flex": "1"}
                                    ),
                                ]
                            ),
                        ]
                    ),

                    # Ligne 2 : Date + Carte + Camembert
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "row",
                            "flex": "1",
                            "gap": "10px"
                        },
                        children=[
                            # Boîte sélection date
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "0.3",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Sélection Date",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.DatePickerSingle(
                                        id="date-picker",
                                        min_date_allowed=map_df["Date"].min().date(),
                                        max_date_allowed=map_df["Date"].max().date(),
                                        initial_visible_month=map_df["Date"].min().date(),
                                        date=map_df["Date"].min().date(),
                                        style={"marginBottom": "20px", "width": "200px"}
                                    ),
                                ]
                            ),

                            # Boîte Carte
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "1",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Carte des Températures",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.Graph(
                                        id="temperature-map",
                                        config={"responsive": True},
                                        style={"width": "100%", "flex": "1"}
                                    ),
                                ]
                            ),

                            # Boîte Camembert
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "1",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Répartition des Températures",
                                        style={
                                            "fontSize": "1.1em",
                                            "fontWeight": "bold",
                                            "color": "#333",
                                            "marginBottom": "10px"
                                        }
                                    ),
                                    dcc.Graph(
                                        id="temperature-pie",
                                        config={"responsive": True},
                                        style={"width": "100%", "flex": "1"}
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
