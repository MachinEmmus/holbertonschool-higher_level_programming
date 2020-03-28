
if __name__ == "__main__":

    import sys
    import MySQLdb

    user = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]
    v = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, passwd=paswd, db=db_name)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE `name` = \"{}\" ORDER BY id ASC".format(v))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
