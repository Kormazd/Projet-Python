from dash.dependencies import Input, Output
from src.components.histogram import update_histogram
from src.components.map import update_map
from src.utils.layouts import histogram_layout, map_layout

# Configuration des callbacks
def register_callbacks(app):
    # Callback pour changer d'onglets
    @app.callback(
        Output('page-content', 'children'),
        [Input('navigation-tabs', 'value')]
    )
    def display_page(tab_value):
        if tab_value == "histogram":
            return histogram_layout()
        elif tab_value == "map":
            return map_layout()

    # Callback histogramme
    @app.callback(
        Output('temperature-histogram', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_histogram_wrapper(selected_departement):
        return update_histogram(selected_departement)

    # Callback carte
    @app.callback(
        Output('temperature-map', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_map_wrapper(selected_date):
        return update_map(selected_date)
