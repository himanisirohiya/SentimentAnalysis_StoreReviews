import json
import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html
from dash import dcc
# Load reviews data from JSON
with open('reviews_with_sentiment.json', 'r') as json_file:
    all_reviews = json.load(json_file)

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1('Sentiment Analysis Dashboard'),

    # Add your visualizations here using Plotly
    # Example:
    dcc.Graph(id='sentiment-histogram'),

    # Add other components as needed
])

# Define callback to update the histogram
@app.callback(
    Output('sentiment-histogram', 'figure'),
    Input('sentiment-histogram', 'id')
)
def update_histogram(_):
    # Extract sentiment scores
    sentiment_scores = [review['sentiment_score'] for review in all_reviews]

    # Create a histogram using Plotly
    fig = px.histogram(sentiment_scores, nbins=30, title='Sentiment Histogram')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
