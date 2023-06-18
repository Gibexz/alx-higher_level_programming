#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":


    def listStates(username, password, database_name):
        """ function lists all states with a name starting
            with N (upper N) from the database hbtn_0e_0_usa """

        """connection to mysqlserver"""
        dbconnect = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database_name,
                charset="utf8"
            )

        cur = dbconnect.cursor()

        query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY states.id ASC;"

        cur.execute(query)

        states = cur.fetchall()

        for state in states:
            print(state)

        cur.close()
        dbconnect.close()

    '''if __name__ == "__main__":'''
    argv = sys.argv[1:]
    username, password, datab = argv
    listStates(username, password, datab)
