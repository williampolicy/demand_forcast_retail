from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = 'A'  # Default selection
    if request.method == 'POST':
        selected_option = request.form.get('dropdown')

    # Create data
    data = {
        'A': [1, 2, 3, 4, 5, 6],
        'B': [6, 5, 4, 3, 2, 1],
        'C': [2, 3, 5, 6, 2, 1],
    }

    # Create a bar chart
    categories = ['A', 'B', 'C', 'D', 'E', 'F']
    values = data.get(selected_option)
    bar = go.Bar(x=categories, y=values)

    # Convert the figures to JSON
    bar_json = json.dumps(bar, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the template
    return render_template('index.html', plot=bar_json)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template
# import plotly
# import plotly.graph_objs as go
# import json

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Create a bar chart
#     categories = ['A', 'B', 'C', 'D', 'E', 'F']
#     values = [1, 2, 3, 4, 5, 6]
#     bar = go.Bar(x=categories, y=values)

#     # Convert the figures to JSON
#     bar_json = json.dumps(bar, cls=plotly.utils.PlotlyJSONEncoder)

#     # Render the template
#     return render_template('index.html', plot=bar_json)

# if __name__ == '__main__':
#     app.run(debug=True)
