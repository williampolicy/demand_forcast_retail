import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('sales_data.csv')

# 将date字段转换为日期类型
data['date'] = pd.to_datetime(data['date'])

# 初始化供应量、库存量和缺货标记
data['supply'] = 0
data['inventory'] = 0
data['out_of_stock'] = False

# 每周一上货12个产品
data.loc[data['date'].dt.dayofweek == 0, 'supply'] = 12  # Update supply on Mondays

# 计算库存
for i in range(1, len(data)):  # Start from the second row because the first day's inventory is 0
    data.loc[i, 'inventory'] = data.loc[i-1, 'inventory'] + data.loc[i, 'supply'] - data.loc[i, 'sales']

    # 检查是否缺货
    if data.loc[i, 'inventory'] < 0:
        data.loc[i, 'out_of_stock'] = True
        data.loc[i, 'inventory'] = 0
        if i+7 < len(data):  # Make sure the index doesn't exceed the length of the dataframe
            data.loc[i+7, 'supply'] += 12  # Increase the supply for the next week

# 绘制销售量、供应量和库存量的曲线
plt.figure(figsize=(10,6))
plt.plot(data['date'], data['sales'], label='Sales')
plt.plot(data['date'], data['supply'], label='Supply')
plt.plot(data['date'], data['inventory'], label='Inventory')

plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Sales, Supply, and Inventory over Time')
plt.legend(loc='upper left')  # Add a legend
plt.show()

# 保存到新的csv文件
data.to_csv('sales_supply_inventory_data.csv', index=False)
