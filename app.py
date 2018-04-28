from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3 as lite
import sys
 
@app.route("/")
def view_all_books():
	
	con = lite.connect("hotspot.db")
	cur = con.cursor()
	cur.execute("select * from Participant")
	rows = cur.fetchall()

	return render_template("index.html", **locals())

@app.route("/addbook", methods=["GET", "POST"])
def add_book():

	if request.method == "GET":
		return render_template("addbook.html", **locals())

	else:
		title = request.form["title"]
		author = request.form["author"]

		con = lite.connect("books.db")
		with con:
			cur = con.cursor()
			cur.execute("insert into Books (title, author) values ('{}', '{}')".format(title, author))

		return redirect("/")


@app.route("/book/<int:id>")
def get_book(id):

	return render_template("viewbook.html", **locals())

@app.route("/category")
def get_events_by_category():

	con = lite.connect("hotspot.db")
	cur = con.cursor()
	cur.execute("select max(ct), eid, cid, Category.Name from Category, (select att.ct as ct, Event.Event_id as eid, Event.Cat_id as cid from Event, (select count(*) as ct, Event_id from Attendance group by Event_id) as att where Event.Event_id = att.Event_id) as a where a.cid = Category.Cat_id group by a.cid order by Category.Name") 
	rows = get_best_events_by_category()
	print(rows)
	return render_template("category.html", **locals())

if __name__ == "__main__":
    app.run()
