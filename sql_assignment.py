#import sql and easygui

import sqlite3
import easygui
import random
 #Script 1 - add 100 rand ints to a db called 'newnum.db'

#connect to the db

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    #create the table, drop it first if it exists
    c.execute("DROP TABLE if exists integer")
    c.execute("CREATE TABLE integer(num int)")

    #populate the table with 100 random integers from 1 - 100
    #must do it in a loop, otherwise we just insert 1 number
    #must use parameterized statements!!!
    for i in range(100):
        c.execute("INSERT INTO integer VALUES(?)",(random.randint(1,100),))


#script 2, allow user to choose which aggregation they want to perform

#we create a dictionary of choices and commands to pull from
choice = {
          "AVG": "SELECT avg(num) FROM integer",
          "MAX": "SELECT max(num) FROM integer",
          "MIN": "SELECT min(num) FROM integer",
          "SUM": "SELECT sum(num) FROM integer"
          }

#prompt the user


init_prompt = easygui.ynbox("Would you like to aggregate the data?", "")

if init_prompt is True:
    aggregation = easygui.buttonbox("Please choose your aggregation", "", ("AVG", "MAX", "MIN", "SUM"))
    c.execute(choice[aggregation])
    result = easygui.msgbox(c.fetchone(), 'Result')



else:
    confirm_close = easygui.ynbox("Are you sure you want to quit?", "")
    if confirm_close is True:
        exit()



