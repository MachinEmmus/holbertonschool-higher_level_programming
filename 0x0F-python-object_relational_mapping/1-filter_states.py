#!/usr/bin/python3
""" Scripts that list all register that start with 'n'"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db_name,
        port=3306,)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                 LIKE 'n%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
