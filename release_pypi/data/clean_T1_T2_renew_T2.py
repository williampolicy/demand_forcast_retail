import sqlite3

# 连接到你的数据库
conn = sqlite3.connect('dairy.db')
c = conn.cursor()

# 删除T1_Family_Consumption表中的所有行
c.execute("DELETE FROM T1_Family_Consumption")
conn.commit()

# 删除T2_Dairy_Product表中的所有行
c.execute("DELETE FROM T2_Dairy_Products")
conn.commit()

# 删除T2_Dairy_Products表中的Sales字段
# SQLite不直接支持删除字段，所以我们需要创建一个新表，复制过去所有我们想保留的字段，然后删除旧表，最后将新表重命名回原名
c.execute("""
CREATE TABLE T2_Dairy_Products_New (
    Product_ID text,
    Date text,
    Price real,
    Inventory integer
)
""")
conn.commit()

# 复制原表的数据
c.execute("""
INSERT INTO T2_Dairy_Products_New (Product_ID, Date, Price, Inventory)
SELECT Product_ID, Date, Price, Inventory FROM T2_Dairy_Products
""")
conn.commit()

# 删除原表
c.execute("DROP TABLE T2_Dairy_Products")
conn.commit()

# 重命名新表
c.execute("ALTER TABLE T2_Dairy_Products_New RENAME TO T2_Dairy_Products")
conn.commit()

# 最后，别忘了关闭数据库连接
conn.close()
