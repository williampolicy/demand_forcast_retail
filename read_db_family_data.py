import sqlite3
import pandas as pd

# 创建一个数据库连接
conn = sqlite3.connect('family_data.db')

# 从 family_type 表中查询所有数据
family_type_df = pd.read_sql_query("SELECT * FROM family_type", conn)
print('Family type data:')
print(family_type_df)

# 从 consumption_data 表中查询所有数据
consumption_data_df = pd.read_sql_query("SELECT * FROM consumption_data", conn)
print('\nConsumption data:')
print(consumption_data_df)


# 从 family_preference 表中查询所有数据
family_preference_df = pd.read_sql_query("SELECT * FROM family_preference", conn)
print('Family preference data:')
print(family_preference_df)


import matplotlib.pyplot as plt


# 从数据库中读取family_preference表的数据
family_preference = pd.read_sql_query("SELECT * from family_preference", conn)

# 移除id列，因为我们不需要它进行可视化
family_preference = family_preference.drop(['id'], axis=1)

# 将family_type设置为索引，这样我们可以更方便地绘制条形图
family_preference.set_index('family_type', inplace=True)

# 创建堆叠条形图
family_preference.T.plot(kind='bar', stacked=True)

# 添加标题和标签
plt.title('Family Preference for Products')
plt.xlabel('Product')
plt.ylabel('Preference')

# 显示图表
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # 创建子图

family_types = ['A', 'B', 'C']  # 定义家庭类型
for i, family_type in enumerate(family_types):
    family_preference.loc[family_type].plot(kind='bar', ax=axs[i])
    axs[i].set_title(f'Family Type {family_type} Preference for Products')
    axs[i].set_xlabel('Product')
    axs[i].set_ylabel('Preference')

plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()
# 这将生成一个包含3个子图的图，每个子图对应一个家庭类型。在每个子图中，产品的偏好度是纵坐标，各种产品是横坐标。



# 显示图表
plt.show()



# 关闭连接
conn.close()


