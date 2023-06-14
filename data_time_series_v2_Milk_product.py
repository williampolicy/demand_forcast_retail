import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个日期序列
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

# 为每个日期生成销售数据和需求数据
# 商品种类
product_names = ['Milk']

# 定义节日和暴风雪日
holidays = ['2022-11-24', '2022-12-25']  # Thanksgiving and Christmas
blizzard = ['2022-02-10', '2022-02-11', '2022-02-12', '2022-02-13']

for product in product_names:
    sales_data = np.random.uniform(50, 100, len(dates))  # changed to 'np.random.uniform' to generate float64 type data
    demand_data = np.random.uniform(100, 140, len(dates))  # changed to 'np.random.uniform' to generate float64 type data
    inventory_data = demand_data - sales_data
    
    # 在节日和暴风雪日增加需求
    for holiday in holidays:
        demand_data[pd.to_datetime(holiday) == dates] *= 1.3  # increase demand by 30% on holidays

    for day in blizzard:
        demand_data[pd.to_datetime(day) == dates] *= 2  # double the demand during the blizzard

    # 将数据合并为一个 DataFrame
    data = pd.DataFrame({
        'Date': dates,
        'Product': product,
        'Sales': sales_data,
        'Demand': demand_data,
        'Inventory': inventory_data
    })

    # 打印 DataFrame
    print(data)

    # 绘图：销售、需求、库存随时间的变化
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Sales'], label='Sales')
    plt.plot(data['Date'], data['Demand'], label='Demand')
    plt.plot(data['Date'], data['Inventory'], label='Inventory')

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'{product} - Sales, Demand, and Inventory over Time')
    plt.legend()
    plt.grid(True)
    plt.show()
