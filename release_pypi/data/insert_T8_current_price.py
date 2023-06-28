import sqlite3

def create_price_table():
    conn = sqlite3.connect('dairy.db')
    c = conn.cursor()
    
    # 创建新表
    c.execute("""
        CREATE TABLE T8_Check_Current_Price (
            Product_ID text PRIMARY KEY,
            Current_Price real
        )
    """)
    
    # 关闭数据库连接
    conn.close()

# 创建新表
create_price_table()
