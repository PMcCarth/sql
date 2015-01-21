#using executemany()

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    #insert multiple records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 270000),
            ('Houston', 'TX', 210000),
            ('Phoenix', 'AZ', 150000)
            ]

    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

    #Here we used paramaterized statements to avoid SQL injection
