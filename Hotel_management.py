import booking

import restaurant
import info
import customerlogin
import checkout
import random
import cusdetails
import mysql.connector as m
mydb=m.connect(host="localhost",user="root",passwd="tirth2510")
con=mydb.cursor()
con.execute("show databases")
x=con.fetchall()
    


def Exit():
    print("1.MANAGEMENT LOGIN\n"
          "2.CUSTOMER\n"
          "3.EXIT")


def home():
    
    print("*"*133)
    print("                                                      WELCOME TO HOTEL DOTA")
    print("*"*133)
    print("1.HOTEL ROOM INFO\n"
          "2.YOUR TOTAL EXPENSE\n"
          "3.ORDER FOOD\n"
          "4.EXIT")
def mng():
    print("WELCOME")
    print("*"*133)
    print("                                                      WELCOME TO HOTEL DOTA")
    print("*"*133)
    print("1.BOOK A ROOM\n"
          "2.CHECK OUT OF HOTEL\n"
          "3.CUSTOMER DETAILS\n"
          "4.EXIT")



if ("hmanagement",) not in x:
    con.execute("create database hmanagement;")
    con.execute("use hmanagement;")
    con.execute("create table booking(Name varchar(100) not null, phone_no char(15) not null,"
                "Room_No varchar(10) primary key not null, No_of_Days_of_Stay int not null, expenses int not null);")
    mydb.commit()
else:
    con.execute("use hmanagement;")





Exit()
ch=0
while ch!=3:
    ch=int(input("->"))

    i=0
    if ch==1:
        password="management123"
        pm=input("Enter management password:-")
        while True:

            if pm==password:
                
                mng()
                n=0
                while n!=4:
                    n=int(input("->"))
                
              
                    if n==1:
                        print("")
                        booking.booking()
                        mng()
                    elif n==2:
                        print("")
                        checkout.checkingout()
                        mng()
                    elif n==3:
                        print("")
                        cusdetails.cusdetails()
                        mng()
                Exit()
                break
            elif i==5:
                print("You have tried 6 times, try again")
                Exit()
                break
            elif pm!=password:
                print("Invalid Password")

                pm=input("Enter management password:-")
            i+=1

    elif ch==2:
        print("")
        home()

        x=0
        while x!=4:
            x=int(input("WHAT WOULD YOU LIKE TO HAVE:-"))
            
            if x==1:
                print("")
                info.Rooms_Info()
                home()
            elif x==2:
                print("")
                customerlogin.customerlogin()
                home()
            elif x==3:
                print("")
                restaurant.restraunt()
                home()
            
        Exit()
    elif ch==3:
        exit()
        
    else:
        print("Enter a number only")


