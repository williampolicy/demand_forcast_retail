import pandas as pd
import numpy as np
from random import randint

# 读取CSV文件
dates_df = pd.read_csv('special_dates.csv', parse_dates=['start_date', 'end_date'])

# 初始化空的日期序列
discount_days = pd.DatetimeIndex([])
holidays = pd.DatetimeIndex([])
extreme_weather_days = pd.DatetimeIndex([])

# 为每一行的日期范围生成日期序列
for idx, row in dates_df.iterrows():
    date_range = pd.date_range(start=row['start_date'], end=row['end_date'])
    if row['type'] == 'discount':
        discount_days = discount_days.union(date_range)
    elif row['type'] == 'holiday':
        holidays = holidays.union(date_range)
    elif row['type'] == 'extreme_weather':
        extreme_weather_days = extreme_weather_days.union(date_range)
