import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="example",
    host="postgres",
    port="5432",
    sslmode="verify-full"
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

cur.execute("SELECT * FROM test;")

print(cur.fetchall())

conn.commit()
cur.close()
