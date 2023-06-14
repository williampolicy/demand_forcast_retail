import numpy as np
import pandas as pd
from random import randint



# 假设我们有10天的数据，初始销售量都是50
# sales = [50]*20
date_range = pd.date_range(start='1/1/2023', periods=20)
sales = [50] * len(date_range)


# 第4天和第5天是极端天气的一部分
extreme_weather_days = date_range[7:11]

# 构造极端天气事件
extreme_weather_events = [list(extreme_weather_days)]

# 遍历每一天
for i in range(len(date_range)):
    # 如果是极端天气事件的第一天
    for j, event in enumerate(extreme_weather_events):
        if date_range[i] == event[0]:  # If the current date is the start of an extreme weather event
            # 生成一组降序排列的随机数
            random_increases = sorted(np.random.randint(10, 40, size=len(event)), reverse=True)
            print(f'random_increase:',random_increases)

            # 在前一天和前两天增加销售额
            for k in range(1, min(i, len(event))+1):  # Loop from 1 to the number of days before the event
                increase = random_increases[k-1]  # Get the corresponding increase
                if sales[i-k] + increase <= 100:  # Make sure sales don't exceed max value
                    sales[i-k] += increase
            # 使用升序排列的随机数来逐渐减少销售额
            # random_decreases = sorted(random_increases)
            # print(f'random_decreases:',random_decreases)

            for k in range(len(event)):  # Loop over each day of the event
                decrease = random_increases[k]  # Get the corresponding decrease
                if sales[i+k] - decrease >= 0:  # Make sure sales don't go below zero
                    sales[i+k] -= decrease
                else:
                    sales[i+k] = 0  # If sales would go below zero, set them to zero

# 打印每天的销售量
for i in range(len(date_range)):
    print("Date: {}, Sales: {}".format(date_range[i].date(), sales[i]))



import matplotlib.pyplot as plt

# Convert the dates to strings for better display on the plot
date_range_str = [date.strftime('%m-%d') for date in date_range]




plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(date_range_str, sales, marker='o', linestyle='-')  # Plot the sales data

# Highlight the extreme weather days
for event in extreme_weather_events:
    event_dates_str = [date.strftime('%m-%d') for date in event]
    extreme_weather_sales = [sales[date_range.get_loc(date)] for date in event if date in date_range]
    plt.fill_between(event_dates_str, extreme_weather_sales, color='red', alpha=0.3)

    # plt.fill_between(event_dates_str, sales[date_range.isin(event)], color='red', alpha=0.3)

plt.xlabel('Date')  # Set the x-axis label
plt.ylabel('Sales')  # Set the y-axis label
plt.title('Sales vs Date')  # Set the plot title
plt.grid(True)  # Add a grid
plt.show()  # Display the plot




# # 假设我们有10天的数据，初始销售量都是50
# sales = [50]*10
# date_range = pd.date_range(start='1/1/2023', periods=10)

# # 第4天和第5天是极端天气的一部分
# extreme_weather_days = date_range[3:5]

# # 构造极端天气事件
# extreme_weather_events = [list(extreme_weather_days)]

# # 遍历每一天
# for i in range(len(date_range)):
#     # 如果是极端天气事件的第一天
#     for j, event in enumerate(extreme_weather_events):
#         if date_range[i] == event[0]:  # If the current date is the start of an extreme weather event
#             # 生成一组降序排列的随机数
#             random_increases = sorted(np.random.randint(10, 20, size=len(event)), reverse=True)

#             # 在前一天和前两天增加销售额
#             for k in range(1, min(i, len(event))+1):  # Loop from 1 to the number of days before the event
#                 increase = random_increases[k-1]  # Get the corresponding increase
#                 if sales[i-k] + increase <= 100:  # Make sure sales don't exceed max value
#                     sales[i-k] += increase
#                     if sales[i+k] - increase >= 0:  # Make sure sales don't go below zero
#                         sales[i+k] -= increase
#                     else:
#                         sales[i+k] = 0  # If sales would go below zero, set them to zero

# # 打印每天的销售量
# for i in range(len(date_range)):
#     print("Date: {}, Sales: {}".format(date_range[i].date(), sales[i]))




# # 假设我们有10天的数据，初始销售量都是50
# sales = [50]*10
# date_range = pd.date_range(start='1/1/2023', periods=10)

# # 第4天和第5天是极端天气的一部分
# extreme_weather_days = date_range[3:5]

# # 构造极端天气事件
# extreme_weather_events = [list(extreme_weather_days)]

# # 生成一组随机数，数量与极端天气的事件数相等
# random_increases = np.random.randint(10, 20, size=len(extreme_weather_events))

# # 遍历每一天
# for i in range(len(date_range)):
#     # 如果是极端天气事件的第一天
#     for j, event in enumerate(extreme_weather_events):
#         if date_range[i] == event[0]:  # If the current date is the start of an extreme weather event
#             # 获取对应的增量
#             increase = random_increases[j]

#             # 在前一天和前两天增加销售额
#             if i > 0:  # Make sure sales don't exceed max value
#                 sales[i-1] += increase
#                 if i > 1:  # For two days before, do the same
#                     sales[i-2] += increase
#                     increase *= 2  # Double the decrease because we added sales for two days

#             # 在极端天气事件期间减少销售额
#             for k in range(len(event)):
#                 if sales[i+k] >= increase:  # Make sure sales don't go below zero
#                     sales[i+k] -= increase
#                 else:
#                     sales[i+k] = 0  # If sales would go below zero, set them to zero

# # 打印每天的销售量
# for i in range(len(date_range)):
#     print("Date: {}, Sales: {}".format(date_range[i].date(), sales[i]))
