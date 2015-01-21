# Here we aim to create an SQLite3 db and table #

# We import the sqlite3 lib #
import sqlite3

# we create a new db it it doesn't already exist #
conn = sqlite3.connect("new.db")

# We create a cursor object to execute commands #
c = conn.cursor()

# Now we insert data #
c.execute("INSERT INTO population VALUES('New York City', 'NY', '8200000')")
c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# Commit the changes #
conn.commit()

# Close the DB connection #
conn.close()
