import pandas as pd
import numpy as np
from random import randint

# 创建日期范围
date_range = pd.date_range(start='1/1/2022', end='12/31/2023')

# 假设的销售量
sales = [randint(0, 12) for _ in range(len(date_range))] 

# # 折扣活动的日期
# discount_days = pd.date_range(start='6/1/2022', end='6/10/2022').union(pd.date_range(start='11/20/2022', end='11/30/2022'))

# # 节假日
# holidays = pd.date_range(start='12/25/2022', end='12/25/2022').union(pd.date_range(start='7/4/2023', end='7/4/2023'))

# # 极端天气日期
# extreme_weather_days = pd.date_range(start='2/10/2022', end='2/15/2022').union(pd.date_range(start='12/10/2022', end='12/15/2022'))


# 读取CSV文件
dates_df = pd.read_csv('special_dates.csv', parse_dates=['start_date', 'end_date'])

# 初始化空的日期序列
discount_days = pd.DatetimeIndex([])
holidays = pd.DatetimeIndex([])
extreme_weather_days = pd.DatetimeIndex([])

# 为每一行的日期范围生成日期序列
for idx, row in dates_df.iterrows():
    #你可以使用pandas的date_range函数来为这些日期范围生成连续的日期序列
    special_range = pd.date_range(start=row['start_date'], end=row['end_date'])
    if row['type'] == 'discount':
        discount_days = discount_days.union(special_range )
    elif row['type'] == 'holiday':
        holidays = holidays.union(special_range)
    elif row['type'] == 'extreme_weather':
        extreme_weather_days = extreme_weather_days.union(special_range)

print('\n----discount_days:')
print(discount_days)

print('\n----holidays:')
print(holidays)

print('\n----extreme_weather_days:')
print(extreme_weather_days)

# print('----date_range:\n')
# print(date_range)

# print('----sales:\n')
# print(sales)



# 在折扣期间增加销售量至2.5-3倍
# 在节假日期间增加销售量
# 极端天气期间销售量会有所下降，但在天气预报后的几天内会提前消费，因此销售量提前增加
# for i in range(len(date_range)):
#     if date_range[i] in discount_days:
#         sales[i] *= randint(25, 30)/10  # Increase by 2.5 to 3 times
#     if date_range[i] in holidays:
#         sales[i] += randint(10, 20)  # Increase on holidays
#     if date_range[i] in extreme_weather_days:
#         sales[i] -= randint(10, 20)  # Decrease during extreme weather
#         if i > 0:  # Increase in the few days before extreme weather
#             sales[i-1] += randint(10, 20)
#             if i > 1:
#                 sales[i-2] += randint(10, 20)


# Handling sales due to holidays, discounts, and extreme weather
for i in range(len(date_range)):
    if date_range[i] in holidays:
        sales[i] += randint(10, 20)  # Increase on holidays
    if date_range[i] in discount_days:
        sales[i] *= randint(25, 30)/10  # Increase by 2.5 to 3 times
    if date_range[i] in extreme_weather_days:
        # Calculate the decrease in sales
        decrease = randint(10, 20)  
        # Increase in the few days before extreme weather
        if i > 0 and sales[i-1] + decrease <= 100:  # Make sure sales don't exceed max value
            sales[i-1] += decrease
            if i > 1 and sales[i-2] + decrease <= 100:  # For two days before, do the same
                sales[i-2] += decrease
                decrease *= 2  # Double the decrease because we added sales for two days
        elif i > 0:  # If only one day before, add the decrease to that day's sales
            sales[i-1] += decrease
        
        # Decrease in sales during extreme weather
        if sales[i] - decrease >= 0:  # Make sure sales don't go below zero
            sales[i] -= decrease
        else:
            sales[i] = 0  # If sales would go below zero, set them to zero




# for i in range(len(date_range)):
#     if date_range[i] in discount_days:
#         sales[i] *= randint(25, 30)/10  # Increase by 2.5 to 3 times
#     if date_range[i] in holidays:
#         sales[i] += randint(10, 20)  # Increase on holidays
#     if date_range[i] in extreme_weather_days:
#         decrease = randint(10, 20)  # Calculate the decrease in sales
#         if sales[i] - decrease > 0:  # Make sure sales don't go below zero
#             sales[i] -= decrease
#         else:
#             sales[i] = 0  # If sales would go below zero, set them to zero
#         if i > 0:  # Increase in the few days before extreme weather
#             sales[i-1] += randint(10, 20)
#             if i > 1:
#                 sales[i-2] += randint(10, 20)



# 创建DataFrame
data = pd.DataFrame({
    'date': date_range,
    'sales': sales
})



# 创建一个存放日期和销售额的字典
extreme_weather_sales = {}
for i in range(len(date_range)):
    # 如果是极端天气的一天或其前后两天
    if date_range[i] in extreme_weather_days or (i > 0 and date_range[i-1] in extreme_weather_days) or (i < len(date_range) - 1 and date_range[i+1] in extreme_weather_days):
        extreme_weather_sales[date_range[i]] = sales[i]
# 打印极端天气期间以及前后各一天的销售情况
for date, sale in extreme_weather_sales.items():
    print(f"Date: {date}, Sales: {sale}")


# 保存为csv文件
data.to_csv('sales_data.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('sales_data.csv')

# 转换日期
data['date'] = pd.to_datetime(data['date'])

# 绘制销售量时间序列图
plt.figure(figsize=(10,6))
plt.plot(data['date'], data['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Time Series')
plt.show()
