from dash import dcc, html
from src.components.bar_graph import temperature_df as bargraph_df
from src.components.map import temperature_df as map_df

TITLE_STYLE = {
    "fontSize": "1.4em",
    "fontWeight": "bold",
    "color": "#333",
    "margin": 0
}

NEOMORPHISM_BOX_STYLE = {
    "backgroundColor": "#ffffff",
    "borderRadius": "12px",
    "boxShadow": "0 5px 15px rgba(0, 0, 0, 0.2)",  # Ombres plus uniformes
    "padding": "20px"
}

def centralized_layout():
    return html.Div(
        style={
            # Conteneur principal en flex colonne
            "display": "flex",
            "flexDirection": "column",
            "height": "100vh",
            "width": "98vw",
            "margin": "auto",
            "padding": "20px 0",  # Espaces en haut et en bas
            "backgroundColor": "#fff",  # Fond neutre
            "fontFamily": "Arial, sans-serif",
        },
        children=[
            # 1) Barre de titre (en haut)
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

            # 2) Conteneur principal (2 lignes flexibles)
            html.Div(
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "flex": "1",
                    "gap": "10px"
                },
                children=[
                    # -----------------------------
                    # LIGNE 1 : Dépt. + Bargraph + Histogram
                    # -----------------------------
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "row",
                            "flex": "1",
                            "gap": "10px"  # Espaces entre les boîtes
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
                                            for dept in sorted(
                                                bargraph_df["Département"].unique()
                                            )
                                        ],
                                        value=sorted(
                                            bargraph_df["Département"].unique()
                                        )[0],
                                        placeholder="Sélectionnez un département",
                                        style={
                                            "width": "200px",
                                            "margin": "0 auto"
                                        }
                                    ),
                                ]
                            ),

                            # Bargraph
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
                                        style={
                                            "width": "100%",
                                            "flex": "1"
                                        }
                                    ),
                                ]
                            ),

                            # Histogram
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
                                        style={
                                            "width": "100%",
                                            "flex": "1"
                                        }
                                    ),
                                ]
                            ),
                        ]
                    ),

                    # -----------------------------
                    # LIGNE 2 : Date + Carte + Camembert
                    # -----------------------------
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
                                        style={
                                            "marginBottom": "20px",
                                            "width": "200px"
                                        }
                                    ),
                                ]
                            ),

                            # Carte
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
                                        style={
                                            "width": "100%",
                                            "flex": "1"
                                        }
                                    ),
                                ]
                            ),

                            # Camembert
                            html.Div(
                                style={
                                    **NEOMORPHISM_BOX_STYLE,
                                    "flex": "1",
                                    "display": "flex",
                                    "flexDirection": "column"
                                },
                                children=[
                                    html.H3(
                                        "Répartition (Camembert)",
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
                                        style={
                                            "width": "100%",
                                            "flex": "1"
                                        }
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
