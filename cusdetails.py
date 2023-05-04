
def cusdetails():
    
    import mysql.connector as m
    mydb=m.connect(host="localhost",user="root",passwd="tirth2510")
    con=mydb.cursor()
    con.execute("use hmanagement")
    con.execute("select * from booking")
    x=con.fetchall()
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Name","Phone Number","Room Number","Days Of Stay","Total Expense"))
    for i in x:
        a=i[0]
        b=i[1]
        c=i[2]
        d=i[3]
        e=i[4]
        print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(a,b,c,d,e))
        
