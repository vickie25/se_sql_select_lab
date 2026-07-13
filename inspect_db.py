import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

queries = {
    "values": lambda: pd.read_sql(
        "SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails", conn
    ).sum().values,
    "tolist": lambda: pd.read_sql(
        "SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails", conn
    ).sum().tolist(),
    "reset_index_values": lambda: pd.read_sql(
        "SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails", conn
    ).sum().reset_index(drop=True).values,
    "sql_sum_values": lambda: pd.read_sql(
        "SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price FROM orderDetails", conn
    ).values[0],
    "col0": lambda: pd.read_sql(
        'SELECT ROUND(priceEach * quantityOrdered) AS "0" FROM orderDetails', conn
    ).sum(),
}

for name, fn in queries.items():
    result = fn()
    print(name, type(result), result)
    try:
        print("  [0] =>", result[0])
    except Exception as e:
        print("  [0] err:", e)

conn.close()
