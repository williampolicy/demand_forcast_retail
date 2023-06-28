#!/usr/bin/env python3
import sqlite3

# Connect to the database
conn = sqlite3.connect('dairy.db')
c = conn.cursor()

# List of tables you want to see
tables_to_show = ['T1_Family_Consumption', 'T2_Dairy_Products', 'T7_Orders']

for table_name in tables_to_show:
    print(table_name)

    # Get table structure
    # c.execute(f'PRAGMA table_info({table_name});')
    # rows = c.fetchall()
    # print("Table structure:")
    # for row in rows:
    #     print(row)

    # Get table contents
    c.execute(f'SELECT * FROM {table_name};')
    rows = c.fetchall()
    print("Table contents:")
    for row in rows:
        print(row)
        
    print("\n---------------------------\n")

conn.close()
