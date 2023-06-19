#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filterCities(username, password, database, name_search):
    """
    function that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = "SELECT cities.name FROM cities INNER JOIN states ON\
            cities.state_id = states.id WHERE BINARY states.name = %s\
            ORDER BY cities.id ASC"

    cur.execute(query.format(name_search), (name_search,))

    cities = cur.fetchall()

    for city in cities:
        print(city[0], city[1], city[2])

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

    filterCities(userr, pwdd, dbb, searchh)
