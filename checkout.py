
def checkingout():
    import mysql.connector as m
    mydb=m.connect(host="localhost",user="root",passwd="tirth2510")
    con=mydb.cursor()
    con.execute("use hmanagement;")
    CRid=input("Enter Your Room No:")
    con.execute("select * from booking where Room_No='%s'"%(CRid))
    result=con.fetchall()
    for i in result:
        print(i)
    ch=input("Are You Sure You want to Check Out?(Y/N):")
    if ch=="Y" or ch=="y":

        con.execute("delete from booking where Room_No='%s'"%(CRid))
        print("Data Deleted Successfully")
        print("Visit Again")
        mydb.commit()
        mydb.close()
        P=int(input("Press 0 to Exit:-"))
        while P!=0:
            print("Invalid!!!!!")
            P=int(input("Press 0 to Exit:-"))
        return
    else:
        return
    
