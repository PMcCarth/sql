import csv
import sqlite3

with sqlite3.connect("employees.db") as conn:
    c = conn.cursor()

    #open the csv file and read from it

    employees = csv.reader(open("employees.csv", "rU"))

    #create new table called employees

    c.execute("SELECT firstname, lastname from employees")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
