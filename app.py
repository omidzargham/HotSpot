from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import sqlite3 as lite
import sys
from datetime import datetime

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/popular-events")
def get_top_events():

	con = lite.connect("hotspot.db")
	cur = con.cursor()
	cur.execute("select Event.Event_name, Event.Description, Event.Start_time, count(*)  as num_participants from attendance join event on attendance.event_id = event.event_id GROUP BY Event.Event_id order by num_participants DESC")
	rows = cur.fetchall()
	realrows = []
	nightrows = []
	for row in rows:
		if row[2] is not None:
			obj = datetime.strptime(row[2], "%Y-%m-%d %H:%M")
			if obj.hour in range(6,18):
				realrows.append(row)
			else:
				nightrows.append(row)

	return render_template("popularevents.html", **locals())

	#GROUP BY Event.Event_id ORDER BY num_participants

@app.route("/category", methods=["GET"])
def get_events_by_category():

	con = lite.connect("hotspot.db")
	cur = con.cursor()
	cur.execute("select max(ct), eid, cid, Category.Name, Event.Event_name from Event, Category, (select att.ct as ct, Event.Event_id as eid, Event.Cat_id as cid from Event, (select count(*) as ct, Event_id from Attendance group by Event_id) as att where Event.Event_id = att.Event_id) as a where a.cid = Category.Cat_id and Event.Cat_id = a.cid and a.eid = Event.Event_id group by a.cid order by Category.Name") 
	rows = cur.fetchall()
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
			cur.execute("select Event.Event_name, Event.Description, Destination.city, Destination.state, count(*)  as num_participants from attendance join event on attendance.event_id = event.event_id join Destination on event.Dest_id = Destination.Dest_id WHERE Destination.State='{}' GROUP BY Event.Event_id order by num_participants DESC LIMIT 5".format(state))
		else:
			cur.execute("select Event.Event_name, Event.Description, Destination.city, Destination.state, count(*)  as num_participants from attendance join event on attendance.event_id = event.event_id join Destination on event.Dest_id = Destination.Dest_id WHERE Destination.City='{}' GROUP BY Event.Event_id order by num_participants DESC LIMIT 5".format(city))
		rows = cur.fetchall()
		return render_template("view-poploc.html", **locals())



if __name__ == "__main__":
    app.run()


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
