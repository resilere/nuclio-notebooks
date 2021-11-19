import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div(id='tabs-example-content')
])


@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])


if __name__ == '__main__':
    app.run_server()