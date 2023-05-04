def booking():
    import random
    print("-"*133)
    print("                                                    WELCOME TO ROOM BOOKING PORTAL")
    print("-"*133)
    import mysql.connector as m
    mydb=m.connect(host="localhost",user="root",passwd="tirth2510")
    con=mydb.cursor()
    con.execute("use hmanagement;")
    con.execute("select Name from booking")
    cusname=con.fetchall()
    con.execute("select Room_No from booking;")
    rooms=con.fetchall()
    if ("1",)in rooms and ("2",) in rooms and ("3",) in rooms and ("4",) in rooms and ("5",) in rooms and ("6",) in rooms and ("7",) in rooms and ("8",) in rooms and ("9",) in rooms and ("10",) in rooms and ("11",) in rooms and ("12",) in rooms:
        print("No Rooms available")
        
    else:
        custname=input("Enter Your Name:")
        while True:
            if (custname,) in cusname:
                print("Name already exists")
            elif custname=="":
                print("Empty Query")
            else:
                break
            custname=input("Enter Your Name:")
        custphno=input("Enter Your Phone Number:")
        while custphno=='':
            print("You cannot leave this Empty!!!")
            custphno=input("Enter Your Phone Number:")
        days=int(input("Enter Number of days of your stay:"))
        while days=='':
            print("Cant leave this Empty:")
            days=int(input("Enter Number of days of your stay:"))
        print("               SELECT ROOM TYPE")
        print("               ----------------")
        print("1.)STANDARD NON-AC..............Rs.3500") 
        print("2.)STANDARD AC..................Rs.4000") 
        print("3.)3-BED NON-AC.................Rs.4500") 
        print("4.)3-BED AC.....................Rs.5000")  
        print("Press 0 to Book")
        u=int(input("->"))
        while u!=0:
            print("Invalid!!!!!")
            u=int(input("->"))
        while True:
            roomchoice=int(input("Enter the Type of Room:-"))
            if roomchoice=='':
                print("Cant leave this Empty:")
            elif roomchoice not in range(1,5):
                print("Enter a valid Room Type!!")
            elif roomchoice==1:
                if ("1",)in rooms and ("2",) in rooms and ("3",) in rooms:
                    print("No rooms available")
                else:
                    roomid=random.randint(1,3)
                    while True:
                        if (str(roomid),) in rooms :
                            roomid=random.randint(1,3)
                        else:
                            break
                    room=print("Your Room No is:",roomid)
                    m=days*3500
                    print("Your Rent is:",m)
                    break
            elif roomchoice==2:
                if ("4",)in rooms and ("5",) in rooms and ("6",) in rooms:
                    print("No rooms available")
                else:
                    roomid=random.randint(4,6)
                    while True:
                        if (str(roomid),) in rooms :
                            roomid=random.randint(4,6)
                        else:
                            break
                    room=print("Your Room No is:",roomid)
                    m=days*4000
                    print("Your Rent is:",m)
                    break
            elif roomchoice==3:
                if ("7",)in rooms and ("8",) in rooms and ("9",) in rooms:
                    print("No rooms available")
                else:
                    roomid=random.randint(7,9)
                    while True:
                        if (str(roomid),) in rooms :
                            roomid=random.randint(7,9)
                        else:
                            break
                    room=print("Your Room No is:",roomid)
                    m=days*4500
                    print("Your Rent is:",m)
                    break
            elif roomchoice==4:
                if ("10",)in rooms and ("11",) in rooms and ("12",) in rooms:
                    print("No rooms available")
                else:
                    roomid=random.randint(10,12)
                    while True:
                        if (str(roomid),) in rooms :
                            roomid=random.randint(10,12)
                        else:
                            break
                    room=print("Your Room No is:",roomid)
                    m=days*5000    
                    print("Your Rent is:",m)
                    break
            
        con.execute("insert into Booking values('%s','%s','%s','%s','%d')"%(custname,custphno,roomid,days,m))
        mydb.commit()
        con.close()
    P=int(input("Press 0 to Exit:-"))
    while P!=0:
        print("Invalid!!!!!")
        P=int(input("Press 0 to Exit:-"))
