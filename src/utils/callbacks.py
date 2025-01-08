from dash.dependencies import Input, Output
from src.components.barres_graphe import update_histogram
from src.components.map import update_map
from src.components.battle import update_battle

def register_callbacks(app):
    @app.callback(
        Output('temperature-histogram', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_histogram_wrapper(selected_departement):
        return update_histogram(selected_departement)

    @app.callback(
        Output('temperature-map', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_map_wrapper(selected_date):
        return update_map(selected_date)

    @app.callback(
        Output('battle-results', 'children'),
        [Input('dept1-dropdown', 'value'),
         Input('dept2-dropdown', 'value'),
         Input('year-selector', 'value')]
    )
    def update_battle_wrapper(dept1, dept2, years):
        return update_battle(dept1, dept2, years)
