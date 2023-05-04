def restraunt():
    import mysql.connector as m
    mydb=m.connect(host="localhost",user="root",passwd="tirth2510")
    con=mydb.cursor()
    con.execute("use hmanagement;")
    print("_"*133)
    print("                                                      WELCOME TO HOTEL '♥ADAMO♥'")
    print("_"*133)
    print("                                                              FOOD MENU")
    print("_"*133)
    print("-----------------------------------          -----------------------------------\n"
          "            BEVERAGES                                          DAL\n"
          "-----------------------------------          -----------------------------------\n"
          "1.REGULAR TEA.................Rs.20          25.DAL FRY...................Rs.140\n"
          "2.MASALA TEA..................Rs.25          26.DAL DHOKLI................Rs.150\n"
          "3.COFFEE......................Rs.25          27.DAL TADKA.................Rs.150\n"
          "4.COLD COFFEE.................Rs.30\n"
          "")
    print("-----------------------------------          -----------------------------------\n"
          "            BREAKFAST                                        ROTI               \n"
          "-----------------------------------          -----------------------------------\n"
          "5.BREAD BUTTER................Rs.30          28.PLAIN ROTI.................Rs.15\n"
          "6.BREAD JAM...................Rs.30          29.BUTTER ROTI................Rs.15\n"
          "7.VEG. SANDWICH...............Rs.50          30.POORI......................Rs.20\n"
          "8.CHEESE TOAST SANDWICH.......Rs.50          31.BUTTER NAAN................Rs.25\n"
          "9.GRILLED SANDWICH............Rs.70          32.GARLIC NAAN................Rs.25\n"
          "")
    print("------------------------------------         ------------------------------------\n"
          "              SOUPS                                          RICE                \n"
          "------------------------------------         ------------------------------------\n"
          "10.TOMATO SOUP................Rs.100         33.PLAIN RICE..................Rs.90\n"
          "11.HOT ANS SOUR...............Rs.100         34.JEERA RICE..................Rs.90\n"
          "12.VEG. NOODLES SOUP..........Rs.110         35.VEG PULAV..................Rs.110\n"
          "13.SWEETCORN SOUP.............Rs.110         36.VEG BIRYANI................Rs.110\n"
          "14.MANCHOW SOUP...............Rs.120         37.SCHEZWAN RICE..............Rs.125\n"
          "")
    print("------------------------------------         ------------------------------------\n"
          "            MAIN COURSE                                  SOUTH INDIAN            \n"
          "------------------------------------         ------------------------------------\n"
          "15.SHAHI PANEER...............Rs.110         38.PLAIN DOSA.................Rs.100\n"
          "16.KADHAI PANEER..............Rs.110         39.MASALA DOSA................Rs.130\n"
          "17.PALAK PANEER...............Rs.120         40.MYSORE MASALA DOSA.........Rs.130\n"
          "18.CHILLI PANEER..............Rs.140         41.JINI DOSA..................Rs.130\n"
          "19.MIX. VEG...................Rs.140         42.CHINESE DOSA...............Rs.130\n"
          "20.MALAI KOFTA................Rs.140         43.PANEER DOSA................Rs.120\n"
          "21.CHOLE......................Rs.140         44.MIX.VEG ROLL...............Rs.125\n"
          "22.ALOO MATAR.................Rs.140         45.IDLI.......................Rs.140\n"
          "23.DAL MAKHNI.................Rs.140         46.SAMBHAR VADA...............Rs.140\n"
          "24.MATAR MUSHROOM.............Rs.140         47.SWEET CORN CHEESE..........Rs.110\n"
          "                                                MYSORE\n"
          "\n"
          "")
    print("---------------------------------------------------------------------------------\n"
          "         ICE CREAM                                       COLD DRINKS             \n"
          "-----------------------------------         -------------------------------------\n"
          "48.VANILLA....................Rs.60         53.PEPSI........................Rs.60\n"
          "49.STRAWBERRY.................Rs.60         54.COCA COLA....................Rs.60\n"
          "50.CHOCOLATE..................Rs.80         55.FROOTI.......................Rs.50\n"
          "51.MANGO......................Rs.75         56.MOUNTAIN DEW.................Rs.70\n"
          "52.BUTTER SCOTCH..............Rs.75         57.SPRITE.......................Rs.70\n"
          "\n"
          "Press 0 when you finish your Order")
    O=1
    r=0
    while(O!=0):
        O=int(input("Enter your order:-"))
        if O==1 or O==30:
            rs=20
            r=r+rs 
        elif O==2 or O==3 or O==31 or O==32:
            rs=25
            r=r+rs
        elif O==4 or O==5 or O==6:
            rs=30
            r=r+rs
        elif O==7 or O==8 or O==55:
            rs=50
            r=r+rs 
        elif O==9 or O==56 or O==57: 
            rs=70
            r=r+rs 
        elif O==10 or O==11 or O==38: 
            rs=100
            r=r+rs 
        elif O==12 or O==13 or O==15 or O==16 or O==35 or O==36 or O==47: 
            rs=110
            r=r+rs 
        elif O==14 or O==17 or O==43: 
            rs=120
            r=r+rs 
        elif (O<=25 and O>=18) or O==45 or O==46: 
            rs=140
            r=r+rs 
        elif O==26 or O==27: 
            rs=150
            r=r+rs 
        elif O==28 or O==29: 
            rs=15
            r=r+rs 
        elif O==33 or O==34: 
            rs=90
            r=r+rs 
        elif O==37 or O==44: 
            rs=125
            r=r+rs 
        elif O<=42 and O>=39: 
            rs=130
            r=r+rs
        elif O==48 or O==49 or O==53 or O==54: 
            rs=60
            r=r+rs
        elif O==50: 
            rs=80
            r=r+rs
        elif O==51 or O==52: 
            rs=75
            r=r+rs     
        elif O==0: 
            pass
        else: 
            print("No Such Item Number found!!")
    con.execute("select Room_No from booking")
    rooms=con.fetchall()
    while True:
        room=int(input("Enter your room number:"))
        if (str(room),) not in rooms:
            print("Give a valid room number")
        else:
            con.execute("update booking set expenses=expenses+'%d' where Room_no='%s'"%(r,room))
            mydb.commit()
            print("Order has been placed")
            break
    print("Total Bill:Rs.%s"%r)
    print("☻Enjoy your meal!!!☻")
    n=int(input("Press 0 to Exit:-")) 
    while n!=0:
        n=int(input("Press 0 to Exit:-"))
