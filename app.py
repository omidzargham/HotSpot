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

# @app.route("/addbook", methods=["GET", "POST"])
# def add_book():

# 	if request.method == "GET":
# 		return render_template("addbook.html", **locals())

# 	else:
# 		title = request.form["title"]
# 		author = request.form["author"]

# 		con = lite.connect("books.db")
# 		with con:
# 			cur = con.cursor()
# 			cur.execute("insert into Books (title, author) values ('{}', '{}')".format(title, author))

# 		return redirect("/")


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

@app.route("/pop-loc", methods=["GET", "POST"])
def get_pop_loc():
	if request.method == "GET":
		return render_template("poploc.html", **locals())

	else:
		state = request.form["state"]
		city = request.form["city"]

		con = lite.connect("hotspot.db")
		cur = con.cursor()
		if (city == ""):
			cur.execute("select Event.Event_name, Event.Description, count(*) as num_participants FROM ((Event LEFT JOIN Attendance ON Event.Event_id = Attendance.Event_id) LEFT JOIN Participant ON Attendance.Participant_id = Participant.Participant_id) LEFT JOIN Destination ON Destination.Dest_id = Event.Dest_id WHERE Destination.State = '{}' AND  Participant.Participant_id IS NOT NULL GROUP BY Event.Event_id ORDER BY num_participants DESC LIMIT 5".format(state))
		else:
			cur.execute("select Event.Event_name, Event.Description, count(*) as num_participants FROM ((Event LEFT JOIN Attendance ON Event.Event_id = Attendance.Event_id) LEFT JOIN Participant ON Attendance.Participant_id = Participant.Participant_id) LEFT JOIN Destination ON Destination.Dest_id = Event.Dest_id WHERE Destination.City = '{}' AND  Participant.Participant_id IS NOT NULL GROUP BY Event.Event_id ORDER BY num_participants DESC LIMIT 5".format(city))
		rows = cur.fetchall()
		return render_template("view-poploc.html", **locals())



if __name__ == "__main__":
    app.run()
