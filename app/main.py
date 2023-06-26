import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = Dash(__name__)

df = pd.read_csv("app/alpha_vantage_news.csv")

app.layout = html.Div(
    [
        html.H1("My Dash App", style={"textAlign": "center"}),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Dropdown(
                                id="ticker-dropdown",
                                options=[
                                    {"label": i, "value": i}
                                    for i in df["ticker"].unique()
                                ],
                                value="Select a ticker",
                            )
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Tabs(
                                    id="tabs",
                                    value="tab-1",
                                    children=[
                                        dcc.Tab(label="Relevance Score", value="tab-1"),
                                        dcc.Tab(label="Sentiment Score", value="tab-2"),
                                    ],
                                ),
                                html.Div(id="tabs-content"),
                            ]
                        )
                    ]
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value"), Input("ticker-dropdown", "value")],
)
def render_content(tab, selected_ticker):
    if selected_ticker is not None:
        filtered_df = df[df["ticker"] == selected_ticker]

        if tab == "tab-1":
            figure = {
                "data": [
                    {
                        "x": filtered_df["time_published"],
                        "y": filtered_df["relevance_score"],
                        "type": "bar",
                    }
                ],
                "layout": {"title": f"Relevance Score Over Time for {selected_ticker}"},
            }
            return dcc.Graph(figure=figure)

        elif tab == "tab-2":
            figure = {
                "data": [
                    {
                        "x": filtered_df["time_published"],
                        "y": filtered_df["ticker_sentiment_score"],
                        "type": "bar",
                    }
                ],
                "layout": {"title": f"Sentiment Score Over Time for {selected_ticker}"},
            }
            return dcc.Graph(figure=figure)


if __name__ == "__main__":
    app.run_server(debug=True)
