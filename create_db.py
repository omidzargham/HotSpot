import sqlite3 as lite
import sys

con = lite.connect("hotspot.db")

with con:
	cur = con.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS Participant (Participant_id INTEGER PRIMARY KEY, Name TEXT, Age INTEGER, Gender TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Destination (Dest_id INTEGER PRIMARY KEY, Dest_name TEXT, State TEXT, City TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Event (Event_id INTEGER PRIMARY KEY, Event_name TEXT, Dest_id INTEGER, Start_time DATETIME, End_time DATETIME, Description TEXT, Cat_id INTEGER, Cost FLOAT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Attendance (Att_id INTEGER PRIMARY KEY, Participant_id INTEGER, Event_id INTEGER)")
	cur.execute("CREATE TABLE IF NOT EXISTS Category (Cat_id INTEGER PRIMARY KEY, Name TEXT)")

	
	
	cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (null, 'Andrea', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (null, 'Cindy', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (null, 'Ben', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (null, 'Omid', 21, 'Male')")
	'''
	cur.execute("INSERT INTO Books (title, author) VALUES ('Info Org', 'Bob')")
	cur.execute("INSERT INTO Books (title, author) VALUES ('Info Law', 'Deidre')")
	cur.execute("INSERT INTO Books (title, author) VALUES ('Math', 'Julie')")
	'''