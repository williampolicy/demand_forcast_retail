import sqlite3

# 连接到你的数据库
conn = sqlite3.connect('dairy.db')
c = conn.cursor()

# 表3: T3_Suppliers
c.execute('DELETE FROM T3_Suppliers')

suppliers = [
    ('sup001', 'pro001', 9.5, 5),
    ('sup002', 'pro002', 10.5, 6),
    ('sup003', 'pro003', 11.5, 7)
]

c.executemany('''
    INSERT INTO T3_Suppliers (
        Supplier_ID,
        Product_ID,
        Supply_Price,
        Flexibility)
    VALUES (?, ?, ?, ?)
    ''', suppliers)

# 表4: T4_Discounts
# 清空表4: T4_Discounts
c.execute('DELETE FROM T4_Discounts')

discounts = [
    ('dis001', 'pro001', '2023-12-18', '2023-12-25', 0.9),
    ('dis002', 'pro002', '2023-11-18', '2023-11-25', 0.85),
    ('dis003', 'pro003', '2023-10-18', '2023-10-25', 0.9)
]

c.executemany('''
    INSERT INTO T4_Discounts (
        Discount_ID,
        Product_ID,
        Start_Date,
        End_Date,
        Discount_Rate)
    VALUES (?, ?, ?, ?, ?)
    ''', discounts)

# 表5: T5_Holidays
# 清空表5: T5_Holidays
c.execute('DELETE FROM T5_Holidays')

holidays = [
    ('2023-12-25', 1),
    ('2023-11-25', 1),
    ('2023-10-25', 1)
]

c.executemany('''
    INSERT INTO T5_Holidays (
        Date,
        Is_Holiday)
    VALUES (?, ?)
    ''', holidays)

# 表6: T6_Extreme_Weather
# 清空表6: T6_Extreme_Weather
c.execute('DELETE FROM T6_Extreme_Weather')


extreme_weather = [
    ('2023-02-20', 1)
]

c.executemany('''
    INSERT INTO T6_Extreme_Weather (
        Date,
        Is_Extreme)
    VALUES (?, ?)
    ''', extreme_weather)

# 提交事务并关闭连接
conn.commit()
conn.close()
