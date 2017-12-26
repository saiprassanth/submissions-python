'''
DB connectivity
saiprassanth.ramesh@accenture.com
'''
import sqlite3
def test():#test function
    try:
        print "this is a test function"
        con=connection()
        c=con.cursor()#creating an object for cursor which has the execute method
        createtableinsert(con,c)
        threemoreineachdept(con,c)
        displayingtherecords(c)
        reportforguild(c)
        update(c, con)
    except Exception as e:
        print "error in test",e
def connection():
    try:
        con=sqlite3.connect("C:/Users/Sai/Desktop/sqlite/sample.db")#connecting to the database
    except Exception as e:
        print "error in db connectivity",e
    return con
def createtableinsert(con,c):
    try:
        c.execute("drop table if exists employee;")#dropping if the table already exists
        c.execute("create table employee(employeeId integer,firstname varchar2(10),lastname varchar2(10),dept varchar2(10));")#creating the specified table within the database
        c.execute("insert into employee values(100,'Sunil','Shetty','Cinema');")#inserting values into the tables
        c.execute("insert into employee values(200,'Srini','Mahalingam','IT');")
        c.execute("insert into employee values(300,'Adam','Sanders','IT');")
        c.execute("insert into employee values(400,'Tommy','Mancenty','Guild');")
        c.execute("insert into employee values(500,'Hovis','M',NULL);")
        con.commit()
    except Exception as e:
        print "error in create and insert statements",e    
def threemoreineachdept(con,c):#inserting three more records in each dept
    try:
        c.execute("insert into employee values(600,'Saiprassanth','Ramesh','Cinema');")
        c.execute("insert into employee values(700,'Harishkumar','Chandrasekar','Cinema');")
        c.execute("insert into employee values(800,'Jaikumar','Srinivasan','Cinema');")
        c.execute("insert into employee values(900,'Manojkumar','Bala','IT');")
        c.execute("insert into employee values(1000,'Karthickraja','Rakesh','IT');")
        c.execute("insert into employee values(1100,'Winsals','Arumaidurai','IT');")
        c.execute("insert into employee values(1200,'Bharathwaj','Mahalingam','Guild');")
        c.execute("insert into employee values(1300,'Sandiya','Ramesh','Guild');")
        c.execute("insert into employee values(1400,'Ramesh','Mani','Guild');")
        con.commit()
    except Exception as e: 
        print "error in adding three in each dept",e   
def displayingtherecords(c):#reading and displayong the records
    print "displaying all the records"
    for res in c.execute("select * from employee;"):#storing the retrieved rows one bye on and printing them
        print res
def reportforguild(c):#report for guild
    print "report for guild"
    try:
        for res in c.execute("select * from employee where dept like 'Guild';"):
            print res
    except Exception as e:
        print "error in displaying the records",e
def update(c,con):#updating the IT dept employees to a dept defined by the user
    a=raw_input("enter the dept with which you want to update IT department")
    try:
        c.execute("update employee set dept='%s' where dept='IT';"%a)    
        con.commit()
        print "after update"
        for res in c.execute("select * from employee;"):
            print res
    except Exception as e:
        print "error in the update and display statements",e
    con.close()
con=connection()
c=con.cursor()#creating an object for cursor which has the execute method
createtableinsert(con,c)
threemoreineachdept(con,c)
displayingtherecords(c)
reportforguild(c)
update(c, con)
test()