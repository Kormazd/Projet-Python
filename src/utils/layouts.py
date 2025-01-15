from dash import dcc, html
from src.components.bar_graph import temperature_df as bargraph_df
from src.components.map import temperature_df as map_df
from src.components.histogram import temperature_df as histogram_df

TITLE_STYLE = {
    "fontSize": "1.4em",
    "fontWeight": "bold",
    "color": "#333",
    "margin": 0
}

NEOMORPHISM_BOX_STYLE = {
    "backgroundColor": "#ffffff",
    "borderRadius": "12px",
    "boxShadow": "7px 7px 14px #c5c5c5, -7px -7px 14px #ffffff",
    "padding": "20px",
    "display": "flex",
    "flexDirection": "column"
}

def centralized_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Dashboard Météo", style=TITLE_STYLE)
                ],
                style={
                    **NEOMORPHISM_BOX_STYLE,
                    "width": "250px",
                    "margin": "0 auto 20px",
                    "justifyContent": "center",
                    "alignItems": "center"
                }
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H3("Sélection Département", style={
                                        "fontSize": "1.1em",
                                        "fontWeight": "bold",
                                        "color": "#333",
                                        "marginBottom": "10px"
                                    }),
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
                                ],
                                style={
                                    "flex": "0.3",
                                    "marginRight": "10px",
                                    **NEOMORPHISM_BOX_STYLE
                                }
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
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
                                                style={"width": "100%", "height": "100%"}
                                            ),
                                        ],
                                        style={
                                            "flex": "1",
                                            "marginRight": "10px",
                                            **NEOMORPHISM_BOX_STYLE
                                        }
                                    ),
                                    html.Div(
                                        [
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
                                                style={"width": "100%", "height": "100%"}
                                            ),
                                        ],
                                        style={
                                            "flex": "1",
                                            "marginLeft": "10px",
                                            **NEOMORPHISM_BOX_STYLE
                                        }
                                    ),
                                ],
                                style={
                                    "display": "flex",
                                    "flex": "0.7",
                                    "gap": "10px"
                                }
                            ),
                        ],
                        style={
                            "display": "flex",
                            "flex": "1",
                            "gap": "10px",
                            "marginBottom": "20px"
                        }
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H3("Sélection Date", style={
                                        "fontSize": "1.1em",
                                        "fontWeight": "bold",
                                        "color": "#333",
                                        "marginBottom": "10px"
                                    }),
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
                                ],
                                style={
                                    "flex": "0.3",
                                    "marginRight": "10px",
                                    **NEOMORPHISM_BOX_STYLE
                                }
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
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
                                                style={"width": "100%", "height": "100%"}
                                            ),
                                        ],
                                        style={
                                            "flex": "1",
                                            "marginRight": "10px",
                                            **NEOMORPHISM_BOX_STYLE
                                        }
                                    ),
                                    html.Div(
                                        [
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
                                                style={"width": "100%", "height": "100%"}
                                            ),
                                        ],
                                        style={
                                            "flex": "1",
                                            "marginLeft": "10px",
                                            **NEOMORPHISM_BOX_STYLE
                                        }
                                    ),
                                ],
                                style={
                                    "display": "flex",
                                    "flex": "0.7",
                                    "gap": "10px"
                                }
                            ),
                        ],
                        style={
                            "display": "flex",
                            "flex": "1",
                            "gap": "10px"
                        }
                    ),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "flex": "1"
                }
            ),
        ],
        style={
            # On utilise minHeight pour autoriser la page à grandir
            "minHeight": "100vh",  
            "width": "98vw",
            "margin": "auto",
            "display": "flex",
            "flexDirection": "column",
            "fontFamily": "Arial, sans-serif",
            # Autorise le défilement vertical si le contenu dépasse la fenêtre
            "overflowY": "auto"
        }
    )
