from dash.dependencies import Input, Output
from src.components.bar_graph import update_bargraph
from src.components.map import update_map
from src.components.histogram import update_histogram
from src.components.camembert import update_camembert

def register_callbacks(app):
    """
    Enregistre tous les callbacks nécessaires pour le dashboard.
    Chaque callback connecte un input utilisateur à un graphique.
    """
    @app.callback(
        Output('temperature-bargraph', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_bargraph_wrapper(selected_departement):
        # Met à jour le graphique des températures moyennes par département
        return update_bargraph(selected_departement)

    @app.callback(
        Output('temperature-map', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_map_wrapper(selected_date):
        # Met à jour la carte des températures pour la date sélectionnée
        return update_map(selected_date)

    @app.callback(
        Output('temperature-histogram', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_histogram_wrapper(selected_departement):
        # Met à jour l'histogramme des températures par département
        return update_histogram(selected_departement)

    @app.callback(
        Output('temperature-pie', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_camembert_wrapper(selected_date):
        # Met à jour le graphique en camembert pour la date sélectionnée
        return update_camembert(selected_date)
