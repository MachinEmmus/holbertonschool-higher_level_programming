#!/usr/bin/python3


if __name__ == "__main__":

    import sys
    import MySQLdb

    user = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user, passwd=paswd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
