#Listing 3_5 : book view
def book(request, id):
    conn=sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    qry = "SELECT * FROM Books WHERE id=?"
    cur.execute(qry, (id,))
    book=cur.fetchone()
    return HttpResponse(str(book))
