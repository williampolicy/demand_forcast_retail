import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 创建数据库连接
conn = sqlite3.connect('family_activity.db')

# 读取数据库中的表到DataFrame
df = pd.read_sql('SELECT * FROM ActivityLevels', conn)


# 打印列名
print(df.columns)

# 打印数据
print(df)


# 关闭数据库连接
conn.close()



# 以可视化形式展示活动水平
df.plot(kind='line', subplots=True)
plt.show()


# 找到12月份的数据并修改活动水平
# df.loc[(df['Day'] >= 335) & (df['Day'] <= 365), ['A_activity', 'B_activity', 'C_activity']] *= 2
df.loc[(df['Day'] >= 335) & (df['Day'] <= 365), ['Activity_Level_A', 'Activity_Level_B', 'Activity_Level_C']] *= 2


# 创建数据库连接
conn = sqlite3.connect('family_activity.db')

# 将修改后的DataFrame存回数据库，替换原表
df.to_sql('ActivityLevels', conn, if_exists='replace', index=False)

# 关闭数据库连接
conn.close()




# 创建数据库连接
conn = sqlite3.connect('family_activity.db')

# 读取数据库中的表到DataFrame
df = pd.read_sql('SELECT * FROM ActivityLevels', conn)

# 关闭数据库连接
conn.close()

# 打印修改后的数据
print(df)

# 以可视化形式展示修改后的活动水平
df.plot(kind='line', subplots=True)
plt.show()



