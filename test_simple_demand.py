import pandas as pd
import numpy as np

# 假设的数据
data = {
    'family_type': ['A', 'B', 'C'],
    'sensitivity': [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
    'num_families': [100, 200, 150],
    'activity_level': [1.0, 1.2, 0.9],
    'weight': [1.0, 1.1, 0.95]
}

df = pd.DataFrame(data)

# 初始化一个全年的需求矩阵
total_demand = np.zeros((365, 3))

# 对于每一种类型的家庭
for _, row in df.iterrows():
    # 计算这种类型家庭的每日需求
    daily_demand = np.array(row['sensitivity']) * row['activity_level'] * row['weight']
    # 乘以家庭数量并加到总需求中
    total_demand += daily_demand * row['num_families']

# total_demand现在是一个365x3的矩阵，表示全年每一天的需求谱
print(total_demand)


# 将total_demand转换为DataFrame
demand_df = pd.DataFrame(total_demand, columns=['Product_1', 'Product_2', 'Product_3'])

# 添加一列为'Day'，表示这一年中的第几天
demand_df['Day'] = range(1, 366)

# 打印结果
print(demand_df)

# 可视化
import matplotlib.pyplot as plt

# 绘制三种产品的需求随时间变化的图像
plt.figure(figsize=(12, 6))
plt.plot(demand_df['Day'], demand_df['Product_1'], label='Product 1')
plt.plot(demand_df['Day'], demand_df['Product_2'], label='Product 2')
plt.plot(demand_df['Day'], demand_df['Product_3'], label='Product 3')
plt.xlabel('Day of the year')
plt.ylabel('Demand')
plt.title('Demand for each product throughout the year')
plt.legend()
plt.show()


