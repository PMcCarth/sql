# Here we aim to create an SQLite3 db and table #

# We import the sqlite3 lib #
import sqlite3

# we create a new db it it doesn't already exist #
conn = sqlite3.connect("new.db")

# We create a cursor object to execute commands #
c = conn.cursor()

# Now we create a table #
c.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)
            """)

# Close the DB connection #
conn.close()
