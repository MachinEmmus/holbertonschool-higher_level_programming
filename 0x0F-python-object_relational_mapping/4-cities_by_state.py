#!/usr/bin/python3


if __name__ == "__main__":

    import sys
    import MySQLdb

    user = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user, passwd=paswd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM `cities`\
                 JOIN `states` ON state_id = states.id\
                 ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
