# import pandas as pd
# import numpy as np

# # 创建一个日期序列
# dates = pd.date_range(start='2022-01-01', end='2022-12-01', freq='MS')

# # 为每个日期生成销售数据和需求数据
# sales_data = np.random.randint(80, 120, len(dates))
# demand_data = np.random.randint(100, 140, len(dates))

# # 计算库存数据
# inventory_data = demand_data - sales_data

# # 将数据合并为一个 DataFrame
# data = pd.DataFrame({
#     'Date': dates,
#     'Sales': sales_data,
#     'Demand': demand_data,
#     'Inventory': inventory_data
# })


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个日期序列
dates = pd.date_range(start='2022-01-01', end='2022-12-01', freq='MS')

# 为每个日期生成销售数据和需求数据
sales_data = np.random.randint(80, 120, len(dates))
demand_data = np.random.randint(100, 140, len(dates))

# 计算库存数据
inventory_data = demand_data - sales_data

# 将数据合并为一个 DataFrame
data = pd.DataFrame({
    'Date': dates,
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
plt.title('Sales, Demand, and Inventory over Time')
plt.legend()
plt.grid(True)
plt.show()

