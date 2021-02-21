import cx_Oracle
import traceback
conn=None
try:
    conn=cx_Oracle.connect("mouzikka/music @127.0.0.1/xe")
    print("Connected Successfully to the DB")
    print("Database version:",conn.version)
    print("DB User:",conn.username)
except cx_Oracle.DatabaseError:
    print("DB Error")
    print(traceback.format_exc())
finally:
           if conn is not None:
               conn.close()
               print("Disconnected successfully from the DB")