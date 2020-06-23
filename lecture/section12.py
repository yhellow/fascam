# Section12
# database: mssql, oracle, mysql, mongodb, casasndra, elasticsearch
# SQL: structured query language (from a certain version and above, sqlite is installed automatically)
# table 



# SQL
    # browserportable to use sqlite3 conveniently (robo3t for mongodb)
import sqlite3
    # sqlite3 and sqlite version
print('sqlite3.version: ', sqlite3.version)
print('sqlite3.sqite_version: ', sqlite3.sqlite_version)
print()


import datetime
#  create date
now = datetime.datetime.now()                   # automatic (seconds %.6f)
print('now: ', now)
rightnow = now.strftime('%Y-%m-%d %H:%M:%S')    # year-month-day(month and day: lowercase) / hour:minute:second
print('date and time: ', rightnow)
print()
# --------------------------------------------------------------------



# DB
# DB: create & auto commit (rollback)

