#Listing 3_2 : books view
import sqlite3

def books(request):
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    qry = "SELECT * FROM Books"
    cur.execute(qry)
    books=cur.fetchall()
    return HttpResponse(str(books))
