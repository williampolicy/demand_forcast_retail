import sqlite3

# Connect to the database
conn = sqlite3.connect('dairy.db')
c = conn.cursor()

# Get the list of all tables
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

for table_name in tables:
    table_name = table_name[0]
    print(table_name)

    # Get table structure
    c.execute(f'PRAGMA table_info({table_name});')
    rows = c.fetchall()
    print("Table structure:")
    for row in rows:
        print(row)

    # Get table contents
    c.execute(f'SELECT * FROM {table_name};')
    rows = c.fetchall()
    print("Table contents:")
    for row in rows:
        print(row)
        
    print("\n---------------------------\n")

conn.close()
