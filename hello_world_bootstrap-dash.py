import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

extenal_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets = extenal_stylesheets)

# Create dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Create figure from the data frame
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Define layout
app.layout = dbc.Container(children=[
    # Row 1
    dbc.Row([
        dbc.Col([
            html.H1(children='Hello Dash'),
        ]),
    ]),
    # Row 2
    dbc.Row([
        dbc.Col([
            html.Div(children='''
                Dash: A web application framework for your data.
            '''),
        ]),
    ]),
    # Row 3
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='example-graph',
                figure=fig
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
