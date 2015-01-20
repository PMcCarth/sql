import sqlite3

#Create database if none exists #
conn = sqlite3.connect("cars.db")

# Create a cursor to execute commands #
c = conn.cursor()

c.execute("""CREATE TABLE inventory (Make TEXT, Model TEXT, Quantity INT)
        """)

conn.close()
