import numpy as np
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
import itertools

# 创建日期范围
date_range = pd.date_range(start='1/1/2022', end='12/31/2023')

# 假设的销售量
sales = [randint(0, 20) for _ in range(len(date_range))] 

# 读取CSV文件
dates_df = pd.read_csv('special_dates.csv', parse_dates=['start_date', 'end_date'])

# 初始化空的日期序列
discount_days = pd.DatetimeIndex([])
holidays = pd.DatetimeIndex([])
extreme_weather_days = pd.DatetimeIndex([])

# 为每一行的日期范围生成日期序列
for idx, row in dates_df.iterrows():
    special_range = pd.date_range(start=row['start_date'], end=row['end_date'])
    if row['type'] == 'discount':
        discount_days = discount_days.union(special_range)
    elif row['type'] == 'holiday':
        holidays = holidays.union(special_range)
    elif row['type'] == 'extreme_weather':
        extreme_weather_days = extreme_weather_days.union(special_range)

# Handling sales due to holidays, discounts
for i in range(len(date_range)):
    if date_range[i] in holidays:
        sales[i] += randint(20, 40)  # Increase on holidays
    if date_range[i] in discount_days:
        sales[i] *= randint(25, 50)/10  # Increase by 2.5 to 3 times

# Handling sales due to extreme weather
groups = extreme_weather_days.to_series().diff().ne(pd.Timedelta(1, unit='D')).cumsum()
extreme_weather_events = [list(g) for k, g in itertools.groupby(extreme_weather_days, groups.get)]

for i in range(len(date_range)):
    for event in extreme_weather_events:
        if date_range[i] in event:
            random_increases = sorted(np.random.randint(3, 20, size=len(event)), reverse=True)
            for k in range(1, min(i, len(event))+1): 
                increase = random_increases[k-1]
                if sales[i-k] + increase <= 100:  
                    sales[i-k] += increase
            for k in range(len(event)):
                decrease = random_increases[k] 
                if sales[i+k] - decrease >= 0:  
                    sales[i+k] -= decrease
                else:
                    sales[i+k] = 0  

# 创建DataFrame
data = pd.DataFrame({
    'date': date_range,
    'sales': sales
})

# 保存为csv文件
data.to_csv('sales_data.csv', index=False)

# 读取数据
data = pd.read_csv('sales_data.csv')

# 转换日期
data['date'] = pd.to_datetime(data['date'])

# 绘制销售量时间序列图
plt.figure(figsize=(10,6))
plt.plot(data['date'], data['sales'])

# Highlight the extreme weather days
for event in extreme_weather_events:
    event_dates_str = [date.strftime('%Y-%m-%d') for date in event]
    extreme_weather_sales = [sales[date_range.get_loc(date)] for date in event if date in date_range]
    plt.fill_between(event_dates_str, extreme_weather_sales, color='red', alpha=0.3, label='Extreme Weather')

# Highlight the discount days
discount_dates_str = [date.strftime('%Y-%m-%d') for date in discount_days if date in date_range]
discount_sales = [sales[date_range.get_loc(date)] for date in discount_days if date in date_range]
plt.fill_between(discount_dates_str, discount_sales, color='green', alpha=0.3, label='Discount Days')

# Highlight the holidays
holiday_dates_str = [date.strftime('%Y-%m-%d') for date in holidays if date in date_range]
holiday_sales = [sales[date_range.get_loc(date)] for date in holidays if date in date_range]
plt.fill_between(holiday_dates_str, holiday_sales, color='blue', alpha=0.3, label='Holidays')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Time Series')
plt.legend(loc='upper left')  # Add a legend
plt.show()
