from dash.dependencies import Input, Output
from src.components.bar_graph import update_bargraph
from src.components.map import update_map
from src.components.histogram import update_histogram
from src.components.camembert import update_pie_chart

def register_callbacks(app):
    @app.callback(
        Output('temperature-bargraph', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_bargraph_wrapper(selected_departement):
        return update_bargraph(selected_departement)

    @app.callback(
        Output('temperature-map', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_map_wrapper(selected_date):
        return update_map(selected_date)

    @app.callback(
        Output('temperature-histogram', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_histogram_wrapper(selected_departement):
        return update_histogram(selected_departement)
    @app.callback(
        Output('temperature-piechart', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_pie_chart_wrapper(selected_date):
        return update_pie_chart(selected_date)
