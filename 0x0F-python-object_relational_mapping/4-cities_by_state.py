#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filterStates(username, password, database):
    """
    function that lists all cities from the database hbtn_0e_4_usa
    """
    dbconnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

    cur = dbconnect.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM\
            cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"

    cur.execute(query)

    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    dbconnect.close()


if __name__ == "__main__":
    '''
    argv = sys.argv[1:]
    userr, pwdd, dbb, searchh = argv
    '''
    userr = sys.argv[1]
    pwdd = sys.argv[2]
    dbb = sys.argv[3]

    filterStates(userr, pwdd, dbb)
