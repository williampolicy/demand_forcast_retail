import sqlite3
import pandas as pd

# 创建数据库连接，如果数据库不存在，这个命令会创建一个新的数据库
conn = sqlite3.connect('family_activity.db')

# 读取CSV文件到一个DataFrame
df = pd.read_csv('activity_level.csv')

# 将DataFrame导入到SQLite数据库中，我们命名新的表为"ActivityLevels"
df.to_sql('ActivityLevels', conn, if_exists='replace', index=False)

# 关闭数据库连接
conn.close()
