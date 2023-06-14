import pandas as pd
import numpy as np
from datetime import datetime

# 生成日期范围
dates = pd.date_range(start='2022-01-01', end='2023-12-31')

# 建立数据框，随机生成活动水平
df = pd.DataFrame({
    'Day': dates,
    'Activity_Level_A': np.random.uniform(0.2, 1.0, len(dates)),
    'Activity_Level_B': np.random.uniform(0.2, 1.0, len(dates)),
    'Activity_Level_C': np.random.uniform(0.2, 1.0, len(dates)),
})

# 从特殊日期文件中读取数据
special_dates = pd.read_csv('../special_dates.csv')
special_dates['start_date'] = pd.to_datetime(special_dates['start_date'])
special_dates['end_date'] = pd.to_datetime(special_dates['end_date'])

# 遍历特殊日期，增加活动水平
for _, row in special_dates.iterrows():
    df.loc[(df['Day'] >= row['start_date']) & (df['Day'] <= row['end_date']), ['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C']] *= np.random.uniform(2.0, 3.0)

# # 画图
# df.set_index('Day')[['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C']].plot()

import matplotlib.pyplot as plt

# 其他代码...

df.set_index('Day')[['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C']].plot()

plt.title("Activity Levels Over Time")
plt.xlabel("Date")
plt.ylabel("Activity Level")
plt.show()


# 计算总需求
df['Total_Activity'] = df['Activity_Level_A'] + df['Activity_Level_B'] + df['Activity_Level_C']

# 使用matplotlib绘制图像
import matplotlib.pyplot as plt

df.set_index('Day')[['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C', 'Total_Activity']].plot()

plt.title("Activity Levels Over Time")
plt.xlabel("Date")
plt.ylabel("Activity Level")
plt.show()

# 或者使用plotly绘制图像
import plotly.express as px

fig = px.line(df.melt(id_vars='Day', value_vars=['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C', 'Total_Activity']), x='Day', y='value', color='variable')

fig.show()





