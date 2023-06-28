import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file) # create a database connection to a SQLite database
        print(f'successful connection with {db_file}')
    except Error as e:
        print(e)
    return conn

# Function to execute an sql query
def execute_query(conn, create_table_sql):
    try:
        c = conn.cursor() # create a cursor object by calling the cursor method
        c.execute(create_table_sql) # pass the CREATE TABLE statement to the execute() method
    except Error as e:
        print(e)

# Function to insert data into a table
def insert_data(conn, table, values):
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {table} VALUES {values}')
    conn.commit()

def main():
    database = "dairy.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:

        # create tables
        # T1_Family_Consumption table
        create_T1_table = """CREATE TABLE IF NOT EXISTS T1_Family_Consumption (
                                        Transaction_ID text PRIMARY KEY,
                                        Family_ID text NOT NULL,
                                        Product_ID text NOT NULL,
                                        Date text NOT NULL,
                                        Price_at_Purchase real NOT NULL,
                                        Quantity integer NOT NULL,
                                        Is_Holiday boolean,
                                        Is_Extreme_Weather boolean,
                                        Is_Discounted boolean
                                    );"""
        execute_query(conn, create_T1_table)

        # T2_Dairy_Products table
        create_T2_table = """CREATE TABLE IF NOT EXISTS T2_Dairy_Products (
                                        Product_ID text PRIMARY KEY,
                                        Date text NOT NULL,
                                        Price real NOT NULL,
                                        Inventory integer NOT NULL,
                                        Sales integer NOT NULL
                                    );"""
        execute_query(conn, create_T2_table)

        # T3_Suppliers table
        create_T3_table = """CREATE TABLE IF NOT EXISTS T3_Suppliers (
                                        Supplier_ID text PRIMARY KEY,
                                        Product_ID text NOT NULL,
                                        Supply_Price real NOT NULL,
                                        Flexibility integer NOT NULL
                                    );"""
        execute_query(conn, create_T3_table)

        # T4_Discounts table
        create_T4_table = """CREATE TABLE IF NOT EXISTS T4_Discounts (
                                        Discount_ID text PRIMARY KEY,
                                        Product_ID text NOT NULL,
                                        Start_Date text NOT NULL,
                                        End_Date text NOT NULL,
                                        Discount_Rate real NOT NULL
                                    );"""
        execute_query(conn, create_T4_table)

        # T5_Holidays table
        create_T5_table = """CREATE TABLE IF NOT EXISTS T5_Holidays (
                                        Date text PRIMARY KEY,
                                        Is_Holiday boolean
                                    );"""
        execute_query(conn, create_T5_table)

        # T6_Extreme_Weather table
        create_T6_table = """CREATE TABLE IF NOT EXISTS T6_Extreme_Weather (
                                        Date text PRIMARY KEY,
                                        Is_Extreme boolean
                                    );"""
        execute_query(conn, create_T6_table)

        # Insert some example data
        insert_data(conn, 'T1_Family_Consumption', '("tra001", "fam001", "pro001", "2023-06-28", 10.5, 2, True, False, True)')
        insert_data(conn, 'T2_Dairy_Products', '("pro001", "2023-06-28", 10.5, 100, 10)')
        insert_data(conn, 'T3_Suppliers', '("sup001", "pro001", 9.5, 5)')
        insert_data(conn, 'T4_Discounts', '("dis001", "pro001", "2023-06-28", "2023-07-05", 0.1)')
        insert_data(conn, 'T5_Holidays', '("2023-06-28", True)')
        insert_data(conn, 'T6_Extreme_Weather', '("2023-06-28", False)')

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
