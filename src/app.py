import duckdb

con = duckdb.connect("local.db")

result = con.execute("SELECT 42 as answer").fetchall()

print(result)
