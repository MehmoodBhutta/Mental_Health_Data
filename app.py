from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly  # Import the plotly module
import json

app = Flask(__name__)

# Load and preprocess the data
df = pd.read_csv("survey.csv")
binary_cols = ['self_employed', 'treatment']
df[binary_cols] = df[binary_cols].applymap(lambda x: 1 if x == 'Yes' else 0)

@app.route("/")
def index():
    # Data for the chart
    country_data = df['Country'].value_counts().reset_index()
    country_data.columns = ['Country', 'Count']

    # Create a bar chart using Plotly
    fig = px.bar(country_data, x="Country", y="Count", title="Survey Respondents by Country")
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", graph_json=graph_json)

if __name__ == "__main__":
    app.run(debug=True)
