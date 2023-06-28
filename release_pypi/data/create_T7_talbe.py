import sqlite3

# Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('dairy.db')

# Create a cursor object
c = conn.cursor()

# Delete the table if it already exists
c.execute('DROP TABLE IF EXISTS T7_Orders')

# Create the table
c.execute('''
    CREATE TABLE T7_Orders (
        Order_ID text PRIMARY KEY,
        Product_ID text NOT NULL,
        Date text NOT NULL,
        Order_Quantity integer NOT NULL,
        Supplier_ID text NOT NULL,
        FOREIGN KEY(Product_ID) REFERENCES T2_Dairy_Products(Product_ID),
        FOREIGN KEY(Supplier_ID) REFERENCES T3_Suppliers(Supplier_ID)
    )
''')

# Insert some example data
c.executemany('''
    INSERT INTO T7_Orders (Order_ID, Product_ID, Date, Order_Quantity, Supplier_ID) VALUES (?, ?, ?, ?, ?)
''', [
    ('ord001', 'pro001', '2023-01-01', 48, 'sup001'),
    ('ord002', 'pro002', '2023-01-01', 48, 'sup002'),
    ('ord003', 'pro003', '2023-01-01', 48, 'sup003')
])

# Commit the transaction and close the connection
conn.commit()
conn.close()
