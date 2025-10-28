from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import numpy as np

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Quadratic Bifurcation', style={'textAlign':'center'}),
    dcc.Slider(-2, 2, 0.1,
               value=-2,
               id='my-slider'
    ),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('my-slider', 'value')
)
def update_graph(value):
    # Create x values
    x = np.linspace(-3, 3, 100)

    y = x**2 + value

    # Create the plot
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

    fig.update_layout(
        title='Quadratic Function',
        xaxis_title='x',
    yaxis_title='y'
)

    return fig

if __name__ == '__main__':
    app.run(debug=True)
