#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def listStatesN(username, password, database):
    """ function lists all states with a name starting
        with N (upper N) from the database hbtn_0e_0_usa """

    """connection to mysqlserver"""
    dbconnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

    cur = dbconnect.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY state.id ASC"

    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    dbconnect.close()


if __name__ == "__main__":
    '''username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[2]'''
    argv = sys.argv[1:]
    username, password, database = argv
    """runs the script"""
    listStatesN(username, password, database)
