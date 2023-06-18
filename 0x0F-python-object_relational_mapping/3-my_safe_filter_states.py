#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


def filterStates(username, password, database, name_search):
    """
    function that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
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
    query = "SELECT * FROM states WHERE BINARY name = %s\
            ORDER BY states.id ASC"

    cur.execute(query, (name_search,))

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
    searchh = sys.argv[4]

    filterStates(userr, pwdd, dbb, searchh)
