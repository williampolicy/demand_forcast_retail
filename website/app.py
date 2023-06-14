from flask import Flask, render_template, request
import pandas as pd
import sqlite3
import plotly
import plotly.graph_objs as go
import json

# 连接数据库
conn = sqlite3.connect('../family_data.db')

# 从数据库中读取family_preference表的数据
family_preference = pd.read_sql_query("SELECT * from family_preference", conn)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    family_type = request.form.get('family_type', 'A')  # 默认选项为A类家庭

    # 获取对应家庭类型的偏好数据
    preference_data = family_preference.loc[family_preference['family_type'] == family_type]

    # 创建plotly图形对象
    bar = go.Bar(x=list(preference_data.columns[2:]), y=preference_data.values[0, 2:])

    # Convert the figures to JSON
    bar_json = json.dumps(bar, cls=plotly.utils.PlotlyJSONEncoder)

    # 渲染index.html模板并传递图表相关的bar_json
    return render_template('index.html', plot=bar_json)

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request
# import pandas as pd
# import sqlite3
# from bokeh.plotting import figure
# from bokeh.embed import components
# from bokeh.models import FactorRange

# # 连接数据库
# conn = sqlite3.connect('../family_data.db')

# # 从数据库中读取family_preference表的数据
# family_preference = pd.read_sql_query("SELECT * from family_preference", conn)

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():

#     family_type = request.form.get('family_type', 'A')  # 默认选项为A类家庭
#     print(f"Family Type: {family_type}")


#     # 获取对应家庭类型的偏好数据
#     preference_data = family_preference.loc[family_preference['family_type'] == family_type]
#     print(f"Preference Data: {preference_data}")

#     # 创建bokeh图形对象
#     p = figure(x_range=FactorRange(factors=list(preference_data.columns[2:])), height=350, title=f"Family Type {family_type} Product Preferences",
#                toolbar_location=None, tools="")
#     print(f"Bokeh Figure: {p}")
#     p.vbar(x=list(preference_data.columns[2:]), top=preference_data.values[0, 2:], width=0.9)
#     p.xgrid.grid_line_color = None
#     p.y_range.start = 0
#     script, div = components(p)

#     # p = figure(x_range=FactorRange(factors=list(preference_data.columns[2:])), plot_height=350, title=f"Family Type {family_type} Product Preferences",
#     #            toolbar_location=None, tools="")
#     # p.vbar(x=list(preference_data.columns[2:]), top=preference_data.values[0, 2:], width=0.9)
#     # p.xgrid.grid_line_color = None
#     # p.y_range.start = 0
#     # script, div = components(p)

#     # 渲染index.html模板并传递图表相关的script和div
#     return render_template('index.html', script=script, div=div)


# if __name__ == '__main__':
#     app.run(debug=True)


# from bokeh.plotting import figure, show
# from bokeh.io import output_file

# output_file("bars.html")

# p = figure(height = 600, width = 600, 
#            title = 'Example Bar Graph')

# p.vbar(x=['A', 'B', 'C'], top=[1,2,3], color="firebrick", width=0.5)

# show(p)


# from flask import Flask, render_template
# from bokeh.embed import components
# from bokeh.plotting import figure
# from bokeh.models import ColumnDataSource
# import pandas as pd
# import sqlite3

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/family/<string:family_type>')
# def show_family_preference(family_type):
#     conn = sqlite3.connect('../family_data.db')
#     df = pd.read_sql_query("SELECT * from family_preference", conn)
#     df = df[df.family_type == family_type].drop(['id', 'family_type'], axis=1)

#     source = ColumnDataSource(df)

#     p = figure(x_range=df.columns, title=f"Family {family_type} Preferences", toolbar_location=None, tools="")
#     p.vbar(x='index', top='values', width=0.9, source=source)
#     p.xgrid.grid_line_color = None
#     p.y_range.start = 0

#     script, div = components(p)

#     return render_template('family.html', script=script, div=div)

# if __name__ == '__main__':
#     app.run(debug=True)


