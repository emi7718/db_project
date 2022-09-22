import sqlite3

conn = sqlite3.connect('customer.db')


cursor = conn.cursor()

cursor.execute('''INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com'
)''')
print('command executed')
conn.commit()
conn.close()
