def customerlogin():
    
    import mysql.connector as m
    mydb=m.connect(host="localhost",user="root",passwd="tirth2510",database="hmanagement")
    con=mydb.cursor()
    n=input("Enter your name:")
    r=str(input("Enter your room number:"))
    con.execute("select Name,Room_No from booking")
    x=con.fetchall()
    if (n,r,) in x:
        con.execute("select expenses from booking where Room_No='%s'"%(r))
        s=con.fetchall()
        print("Your Total Expense is:",s[0][0])
    else:
        print("Room Number and Name Don't match")
        
    
