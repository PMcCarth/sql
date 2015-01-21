import sqlite3

#create connection object
conn = sqlite3.connect("new.db")

#create a cursor to execute SQL commands
c = conn.cursor()

#insert data

c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")

#commit changes
conn.commit

#close the connection
conn.close()
