import scipy.stats
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'


def create_distribution(mean, standard_dev):
    """Creates and returns a distribution plot,
    given a mean and a standard deviation"""
    x = np.arange(mean - 5*standard_dev, mean+5*standard_dev)
    pdf = scipy.stats.norm.pdf(x, loc=mean, scale=standard_dev)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=pdf))
    return fig
    
    
if __name__ == '__main__':
    fig = create_distribution(5, 5)
    fig.show()
