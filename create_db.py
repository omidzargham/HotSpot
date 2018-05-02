import sqlite3 as lite
import sys
import time

con = lite.connect("hotspot.db")

with con:
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Participant (Participant_id INTEGER PRIMARY KEY, Name TEXT, Age INTEGER, Gender TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Destination (Dest_id INTEGER PRIMARY KEY, Dest_name TEXT, State TEXT, City TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Event (Event_id INTEGER PRIMARY KEY, Event_name TEXT, Dest_id INTEGER, Start_time DATETIME, End_time DATETIME, Description TEXT, Cat_id INTEGER, Cost FLOAT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Attendance (Att_id INTEGER PRIMARY KEY, Participant_id INTEGER, Event_id INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Category (Cat_id INTEGER PRIMARY KEY, Name TEXT)")

    
    
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (1, 'Andrea', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (2, 'Cindy', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (3, 'Ben', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (4, 'Omid', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (5, 'John', 19, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (6, 'Mary', 24, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (7, 'Jeffrey', 25, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (8, 'Sam', 28, 'Male')")

    cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES (1, 'Union Square', 'California', 'San Francisco')")
    cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES (2, 'Alcatraz Island', 'California', 'San Francisco')")
    cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES (3, 'Bindlestiff Studio', 'California', 'San Francisco')")
    cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES (4, 'Shelton Theater', 'California', 'San Francisco')")
    cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES (5, 'AT&T Park', 'California', 'San Francisco')")


    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (1, 'Cherry Blossom Festival', 1, null, null, 'Come see the beautiful cherry blossoms!', 0, 0.0)")
    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (2, 'Music Busking', 1, null, null, 'Listen to a variety of musicians play on the streets of SF.', 0, 0.0)")
    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (3, 'Alcatraz Island Tour', 2, null, null, 'Tour the old prison of Alcatraz', 0, 0.0)")
    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (4, 'Geek Show 2: Bindlecon', 3, null, null, 'Movie event', 0, 0.0)")
    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (5, 'Late Night Improv', 4, null, null, 'A fun night of comedy', 0, 0.0)")
    cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time, End_time, Description, Cat_id, Cost) VALUES (6, 'SF Giants Baseball', 5, null, null, 'Baseball yay', 0, 0.0)")

    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (1, 1, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (2, 2, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (3, 3, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (4, 4, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (5, 5, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (6, 6, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (7, 7, 3)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (8, 8, 1)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (9, 1, 2)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (10, 5, 2)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (11, 1, 4)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (12, 2, 4)")
    cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES (13, 1, 2)")



    '''
    cur.execute("INSERT INTO Books (title, author) VALUES ('Info Org', 'Bob')")
    cur.execute("INSERT INTO Books (title, author) VALUES ('Info Law', 'Deidre')")
    cur.execute("INSERT INTO Books (title, author) VALUES ('Math', 'Julie')")
    '''