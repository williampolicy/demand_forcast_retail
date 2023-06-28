import sqlite3

def clear_tables():
    conn = sqlite3.connect('dairy.db')
    c = conn.cursor()

    # 清空 T1_Family_Consumption 表
    c.execute("DELETE FROM T1_Family_Consumption")
    # 清空 T2_Dairy_Products 表
    c.execute("DELETE FROM T2_Dairy_Products")
    # 清空 T7_Orders 表
    c.execute("DELETE FROM T7_Orders")

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

if __name__ == "__main__":
    clear_tables()
    print("Tables have been cleared.")
