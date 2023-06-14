import sqlite3

# 创建数据库连接
conn = sqlite3.connect('family_data.db')

# 创建 cursor 对象
cursor = conn.cursor()

# 删除 family_preference 表
cursor.execute("DROP TABLE IF EXISTS family_preference")
# # 提交改动
# conn.commit()
# # 关闭连接
# conn.close()

# 创建 family_preference 表
cursor.execute("""
CREATE TABLE family_preference (
    id INTEGER PRIMARY KEY,
    family_type CHAR(10),
    butter INTEGER,
    ice_cream INTEGER,
    milk INTEGER,
    cream_crease INTEGER,
    pork INTEGER,
    beef INTEGER,
    cheese INTEGER,
    half_and_half INTEGER,
    source_cream INTEGER,
    cotagge_cesse INTEGER,
    eggs INTEGER,
    yogurt INTEGER,
    protein_drink INTEGER,
    cottage_cheese INTEGER
)
""")

# 向 family_preference 表插入数据
cursor.execute("""
INSERT INTO family_preference (family_type, butter, ice_cream, milk, cream_crease, pork, beef, cheese, half_and_half, source_cream, cotagge_cesse, eggs, yogurt, protein_drink, cottage_cheese) VALUES
('A', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
('B', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
('C', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1)
""")

# 提交数据到数据库
conn.commit()

# 关闭连接
conn.close()
