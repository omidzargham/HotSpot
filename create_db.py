import sqlite3 as lite
import sys
import random

cats = ['food','music','games','movies','artists','shop','holiday','academic','political']
event = ['find hilfiger', '4/20', 'cute dogs day', 'rock concert', 'gamers unite', 'food for the poor', 'Cherry Blossom Festival', 'Music Busking', 'Alcatraz Island Tour', 'Geek Show 2: Bindlecon', 'Late Night Improv', 'SF Giants Baseball', 'Outside Lands', 'Wicked','The Lion King', 'American Musical Journey', 'Frozen', 'Hamilton', 'Art at the Met', 'Japanese Tea Garden']
cities = ['Berkeley', 'San Francisco', 'Oakland', 'Los Angeles', 'Las Vegas']
state = ['California']


con = lite.connect("hotspot.db")

with con:
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Participant (Participant_id INTEGER PRIMARY KEY, Name TEXT, Age INTEGER, Gender TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Destination (Dest_id INTEGER PRIMARY KEY, Dest_name TEXT, State TEXT, City TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Event (Event_id INTEGER PRIMARY KEY, Event_name TEXT, Dest_id INTEGER, Start_time DATETIME, End_time DATETIME, Description TEXT, Cat_id INTEGER, Cost FLOAT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Attendance (Att_id INTEGER PRIMARY KEY, Participant_id INTEGER, Event_id INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Category (Cat_id INTEGER PRIMARY KEY, Name TEXT)")

    for i in range(0,len(cats)):
        print(i)
        cur.execute("INSERT INTO Category (Cat_id, Name) VALUES ("+str(i)+",\'"+cats[i]+"\')") #{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
        

    for i in range(0,len(cities)):
        did = i
        dname = cities[i]
        state = 'California'
        city = cities[i]
        cur.execute("INSERT INTO Destination (Dest_id, Dest_name, State, City) VALUES ("+str(did)+",\'"+dname+"\',\'"+state+"\',\'"+city+"\')") #{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
            

    aid = 0
    for i in range(0,len(event)):
        eid = i
        ename = event[i]
        did = random.randint(0,len(cities)-1)
        randomhour = random.randint(0,23)
        randomminute = random.randint(10,59)
        randomyear = random.randint(2015,2018)
        randommonth = random.randint(1,9)
        randomday = random.randint(10,28)
        stime = str(randomyear) + "-0" + str(randommonth) + "-" + str(randomday) + " " + str(randomhour) + ":" + str(randomminute)
        etime = '2018-01-01 1:23'
        listofdescriptions = ["a fun event", "a nice event", "a cool event", "a lame event", "best event ever"]
        descrip = listofdescriptions[random.randint(0,len(listofdescriptions)-1)]
        cid = random.randint(0,len(cats)-1)
        cost = 1.0
        participants = [k for k in range(0,100)]
        for j in range(0,random.randint(0,100)):
            r = random.randint(0,len(participants) - 1)
            pid = participants[r]

            participants.remove(pid)
            cur.execute("INSERT INTO Attendance (Att_id, Participant_id, Event_id) VALUES ("+str(aid)+","+str(pid)+","+str(eid)+")") #{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
            aid+=1
        #cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time,End_time, Description, Cat_id, Cost) VALUES ({}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
        cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time,End_time, Description, Cat_id, Cost) VALUES ("+str(eid)+",\'"+ename+"\',"+str(did)+",\'"+stime+"\',\'"+etime+"\',\'"+descrip+"\',"+str(cid)+","+str(cost)+")")#{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
    

    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (1, 'Andrea', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (2, 'Cindy', 21, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (3, 'Ben', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (4, 'Omid', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (5, 'John', 19, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (6, 'Mary', 24, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (7, 'Jeffrey', 25, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (8, 'Sam', 28, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (9, 'George', 28, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (10, 'Paul', 38, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (11, 'Karen', 37, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (12, 'Jim', 28, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (13, 'Lilly', 22, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (14, 'Hannah', 28, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (15, 'Lauren', 26, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (16, 'Jonathan', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (17, 'Kristen', 22, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (18, 'Nathan', 25, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (19, 'Luke', 31, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (20, 'Shelly', 22, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (21, 'Kelly', 37, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (22, 'James', 28, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (23, 'Laila', 22, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (24, 'Harriet', 28, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (25, 'Lucy', 26, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (26, 'Jared', 21, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (27, 'Barbara', 42, 'Female')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (28, 'Max', 25, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (29, 'Larry', 31, 'Male')")
    cur.execute("INSERT INTO Participant (Participant_id, Name, Age, Gender) VALUES (30, 'Shirley', 32, 'Female')")

    #cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time,End_time, Description, Cat_id, Cost) VALUES (0,'hey',0,null,null,'des',0,0)")#{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
    
    #cur.execute("INSERT INTO Event (Event_id, Event_name, Dest_id, Start_time,End_time, Description, Cat_id, Cost) VALUES ("+str(eid)+","+ename+","+str(did)+",null,null,"+descrip+","+str(cid)+","+str(cost)+")")#0,'hey',0,null,null,'des',0,0)")#{}, {},{},{},{},{},{},{})".format(eid,ename,did,stime,etime,descrip,cid,cost))
    