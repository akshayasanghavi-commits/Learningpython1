import sqlite3

conn = sqlite3.connect("data/company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS applicants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    experience INTEGER
)
""")

cursor.execute("INSERT INTO applicants (name, email, experience) VALUES ('Akshaya', 'ak@example.com', 3)")
cursor.execute("INSERT INTO applicants (name, email, experience) VALUES ('Rahul', 'rahul@example.com', 5)")

conn.commit()
conn.close()