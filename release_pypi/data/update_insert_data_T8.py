import sqlite3

def add_data_to_T8():
    # 连接到数据库
    conn = sqlite3.connect('dairy.db')
    c = conn.cursor()

    # 插入数据
    data = [('pro001', 10.5), ('pro002', 11.5), ('pro003', 12.5)]
    c.executemany('INSERT INTO T8_Check_Current_Price VALUES (?,?)', data)

    # 提交更改
    conn.commit()

    # 关闭连接
    conn.close()

# 执行函数
add_data_to_T8()
