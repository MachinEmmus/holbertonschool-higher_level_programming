#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    import MySQLdb
    
    city = ""
    user = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]
    val = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, passwd=paswd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM `cities` JOIN `states` ON state_id = states.id WHERE states.name = \"{}\" ORDER BY cities.id ASC".format(val))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            city += col + ", "
    print(city[:len(city) - 2])
    cur.close()
    db.close()

