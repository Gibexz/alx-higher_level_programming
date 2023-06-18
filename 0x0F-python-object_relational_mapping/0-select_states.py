#!/usr/bin/python3
"""
python script that lists all states in the database
hbtn_0e_0_usa and are sorted by id (state.id)
"""
import MySQLdb
import sys


def statesList(username, password, database_name):
    """Function that prints all the states in the database"""

    """# Connect to the MySQL server """
    dbconnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )

    """create a cursor object to interact with the database"""
    cur = dbconnect.cursor()

    """query to be executed in other to retrieve all states sorted by id"""
    query = "SELECT * FROM states ORDER BY state.id ASC"

    cur.execute(query)

    states = cur.fetchall()

    for i in states:
        print(i)

    cur.close()
    dbconnect.close()

    if __name__ == "__main__":
        argv = sys.argv[1:]
        username, password, database_name = argv

        statesList(username, password, database_name)
