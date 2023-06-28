import sqlite3

# Connect to the database
conn = sqlite3.connect('dairy.db')
c = conn.cursor()

# Insert new data into T1_Family_Consumption
c.execute("DELETE FROM T1_Family_Consumption;")
data = [('tra001', 'fam001', 'pro001', '2023-12-25', 10.5, 2, True, False, True),
        ('tra002', 'fam002', 'pro002', '2023-04-17', 11.5, 3, True, False, False),
        ('tra003', 'fam003', 'pro003', '2023-11-23', 12.5, 1, True, True, False)]
c.executemany("INSERT INTO T1_Family_Consumption VALUES (?,?,?,?,?,?,?,?,?);", data)

# Insert new data into T2_Dairy_Products
c.execute("DELETE FROM T2_Dairy_Products;")
data = [('pro001', '2023-12-25', 10.5, 100, 10),
        ('pro002', '2023-04-17', 11.5, 200, 20),
        ('pro003', '2023-11-23', 12.5, 300, 30)]
c.executemany("INSERT INTO T2_Dairy_Products VALUES (?,?,?,?,?);", data)

# Insert new data into T3_Suppliers
c.execute("DELETE FROM T3_Suppliers;")
data = [('sup001', 'pro001', 9.5, 5),
        ('sup002', 'pro002', 10.5, 6),
        ('sup003', 'pro003', 11.5, 7)]
c.executemany("INSERT INTO T3_Suppliers VALUES (?,?,?,?);", data)

# Insert new data into T4_Discounts
c.execute("DELETE FROM T4_Discounts;")
data = [('dis001', 'pro001', '2023-12-18', '2023-12-31', 0.1),
        ('dis002', 'pro002', '2023-04-10', '2023-04-24', 0.15),
        ('dis003', 'pro003', '2023-11-16', '2023-11-30', 0.2)]
c.executemany("INSERT INTO T4_Discounts VALUES (?,?,?,?,?);", data)

# Insert new data into T5_Holidays
c.execute("DELETE FROM T5_Holidays;")
data = [('2023-12-25', True),
        ('2023-04-17', True),
        ('2023-11-23', True)]
c.executemany("INSERT INTO T5_Holidays VALUES (?,?);", data)

# Insert new data into T6_Extreme_Weather
c.execute("DELETE FROM T6_Extreme_Weather;")
data = [('2023-02-20', True)]
c.executemany("INSERT INTO T6_Extreme_Weather VALUES (?,?);", data)

conn.commit()
conn.close()
