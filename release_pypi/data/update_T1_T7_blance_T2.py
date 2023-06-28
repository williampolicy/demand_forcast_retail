#!/usr/bin/env python3
import sqlite3

# 连接数据库
def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return conn, c

# 关闭数据库连接
def close_db(conn):
    conn.close()

def show_table(c, table_name):
    # 查询表内容
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()

    # 打印表内容
    print(f"Contents of {table_name}:")
    for row in rows:
        print(row)

# T7驱动库存增加的函数
def restock(c, product_id, restock_quantity, supplier_id, date):
    # 显示插入前的数据
    show_table(c, 'T2_Dairy_Products')

    # 查询当前价格
    c.execute("SELECT Current_Price FROM T8_Check_Current_Price WHERE Product_ID = ?", (product_id,))
    result = c.fetchone()
    if result is None:
        print(f"No record found in T8_Check_Current_Price with Product_ID: {product_id}")
        return
    current_price = result[0]

    # 查询当前库存
    c.execute("SELECT Inventory FROM T2_Dairy_Products WHERE Product_ID = ? AND Date = ?", (product_id, date,))
    result = c.fetchone()

    if result is not None:
        # 更新库存和采购记录
        current_inventory = result[0]
        new_inventory = current_inventory + restock_quantity
        c.execute("UPDATE T2_Dairy_Products SET Inventory = ? WHERE Product_ID = ? AND Date = ?", (new_inventory, product_id, date,))
        c.execute("UPDATE T7_Orders SET Order_Quantity = Order_Quantity + ? WHERE Product_ID = ? AND Date = ? AND Supplier_ID = ?", (restock_quantity, product_id, date, supplier_id,))
    else:
        # 检查在这个日期是否已经存在了对应产品的记录
        c.execute("SELECT * FROM T2_Dairy_Products WHERE Product_ID = ? AND Date = ?", (product_id, date,))
        if c.fetchone() is not None:
            # 如果存在，那么更新这个记录
            c.execute("UPDATE T2_Dairy_Products SET Inventory = Inventory + ? WHERE Product_ID = ? AND Date = ?", (restock_quantity, product_id, date,))
        else:
            # 如果不存在，那么插入新的记录
            c.execute("INSERT INTO T2_Dairy_Products (Product_ID, Date, Price, Inventory) VALUES (?, ?, ?, ?)", (product_id, date, current_price, restock_quantity))
            c.execute("UPDATE T7_Orders SET Order_Quantity = Order_Quantity + ? WHERE Product_ID = ? AND Date = ? AND Supplier_ID = ?", (restock_quantity, product_id, date, supplier_id,))


# T1驱动库存减小的函数
def consume(c, family_id, product_id, consume_quantity, date):
    # 显示插入前的数据
    show_table(c, 'T2_Dairy_Products')

    # 查询产品的当前价格和库存
    c.execute("SELECT Price, Inventory FROM T2_Dairy_Products WHERE Product_ID = ? AND Date = ?", (product_id, date,))
    result = c.fetchone()

    if result is not None:
        # 更新库存和消费记录
        current_price, current_inventory = result
        new_inventory = current_inventory - consume_quantity
        c.execute("UPDATE T2_Dairy_Products SET Inventory = ? WHERE Product_ID = ? AND Date = ?", (new_inventory, product_id, date,))
        c.execute("UPDATE T1_Family_Consumption SET Quantity = Quantity + ? WHERE Family_ID = ? AND Product_ID = ? AND Date = ?", (consume_quantity, family_id, product_id, date,))
    else:
        # 检查在这个日期是否已经存在了对应产品的记录
        c.execute("SELECT * FROM T2_Dairy_Products WHERE Product_ID = ? AND Date = ?", (product_id, date,))
        if c.fetchone() is not None:
            # 如果存在，那么更新这个记录
            c.execute("UPDATE T2_Dairy_Products SET Inventory = Inventory - ? WHERE Product_ID = ? AND Date = ?", (consume_quantity, product_id, date,))
        else:
            # 如果不存在，那么插入新的记录
            c.execute("INSERT INTO T2_Dairy_Products (Product_ID, Date, Price, Inventory) VALUES (?, ?, ?, ?)", (product_id, date, current_price, new_inventory))
            c.execute("INSERT INTO T1_Family_Consumption (Family_ID, Product_ID, Date, Quantity, Price_at_Purchase) VALUES (?, ?, ?, ?, ?)", (family_id, product_id, date, consume_quantity, current_price))


def initialize_consumption(c):
    c.execute("SELECT COUNT(*) FROM T1_Family_Consumption")
    count = c.fetchone()[0]

    if count == 0:
        # Create a new Transaction_ID
        new_id = 'tra001'

        # Insert a new consumption record with the new Transaction_ID
        c.execute("INSERT INTO T1_Family_Consumption (Transaction_ID, Family_ID, Product_ID, Date, Price_at_Purchase, Quantity) VALUES (?, ?, ?, ?, ?, ?)", 
            (new_id, 'fam001', 'pro001', '2023-01-01', 10.0, 0))

def initialize_products(c):
    c.execute("SELECT COUNT(*) FROM T2_Dairy_Products")
    count = c.fetchone()[0]

    if count == 0:
        # 为每个产品插入一个初始记录
        c.execute("INSERT INTO T2_Dairy_Products (Product_ID, Date, Price, Inventory) VALUES (?, ?, ?, ?)", ('pro001', '2023-01-01', 10.0, 10))
        #c.execute("INSERT INTO T2_Dairy_Products (Product_ID, Date, Price, Inventory) VALUES (?, ?, ?, ?)", ('pro002', '2023-01-01', 12.0, 12))
        #c.execute("INSERT INTO T2_Dairy_Products (Product_ID, Date, Price, Inventory) VALUES (?, ?, ?, ?)", ('pro003', '2023-01-01', 15.0, 15))

# 主函数
def main():
    # 连接数据库
    conn, c = connect_db('dairy.db')
    # 初始化产品
    initialize_products(c)
    initialize_consumption(c)

    # 操作流程
    consume(c, 'fam001', 'pro001', 1, '2023-01-01')
    #consume(c, 'fam002', 'pro002', 3, '2023-01-01')
    #consume(c, 'fam003', 'pro003', 3, '2023-01-01')
    

    restock(c, 'pro001', 8, 'sup001', '2023-01-01')
    #restock(c, 'pro002', 24, 'sup002', '2023-01-02')
    #restock(c, 'pro003', 24, 'sup003', '2023-01-02')

    # 提交数据库操作
    conn.commit()

    # 关闭数据库连接
    close_db(conn)




# 执行主函数
if __name__ == '__main__':

    main()
