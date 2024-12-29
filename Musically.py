import mysql.connector
import tabulate
from datetime import date
from pygame import mixer
import time
def createdatabase():
    mydb=mysql.connector.connect(host='localhost', user='root', passwd='kkss')
    mycursor=mydb.cursor()
    mycursor.execute('create database if not exists Album')
    mycursor.execute('show databases')
    for i in mycursor:
        print(i)
def createtable():
    mydb=mysql.connector.connect(host='localhost', user='root', passwd='kkss', database='Album')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('Create table Musically (S_CODE int(3), primary key,S_NAME varchar(20), ARTIST varchar(20),R_DATE Date ,PLAYS int(10),)')
    mycursor.execute('desc Musically')
    for i in mycursor:
        print(i)
def display_song():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        mycur.execute("select * from Musically ORDER BY S_CODE")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['S_CODE','S_NAME','ARTIST','R_DATE','PLAYS'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def display_playlist():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        pl_name=input("Enter playlist name:")
        mycur.execute("select * from {} ORDER BYS_CODE".format(pl_name))
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['S_CODE','S_NAME', 'ARTIST','R_DATE','PLAYS'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def display_membership():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        pl_name=input("Enter playlist name:")
        mycur.execute("select * from membership")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['M_CODE','LEVEL', 'PRICE'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def display_Password():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        pl_name=input("Enter playlist name:")
        mycur.execute("select * from password")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['P_CODE','U_Name', 'PSSWRD','TYPE'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()

def display_users():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        pl_name=input("Enter playlist name:")
        mycur.execute("select * from users")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['P_CODE','SU_Name', 'DOJ','M_SHIP','LASTDOP'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def display_users_playlists():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        pl_name=input("Enter playlist name:")
        mycur.execute("select * from users_playlists")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['P_CODE','playlistname'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()

def display_backup():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        mycur.execute("select * from songbackup ORDER BY S_CODE")
        rs=mycur.fetchall()
        print(tabulate.tabulate(rs,headers=['S_CODE','S_NAME', 'ARTIST', 'R_DATE','PLAY'],tablefmt='fancy_grid'))
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def sign_admin():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        mycur.execute("select * from password where TYPE='ADMIN'")
        rs=mycur.fetchall()
        uname=input("Enter the U_Name: ")
        for r in rs:
            if r[1]==uname and r[3]=="ADMIN":
                Pass_Word=input("Enter the password: ")
                if r[2]==Pass_Word:
                    print("Log In Successful !!")
                    break
                else:
                    print("Sorry, Wrong Password")
                    print()
                    sign_admin()
                    return
            else:
                print("Sorry, Cannot Log in as an Admin")
                print()
                sign_admin()
    except Exception as e:
         print(e)
    mycur.close()
    mycon.close()
def update_song():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        display_song()
        no=int(input("Enter the Song Code of the Song to be Updated: "))
        q="select * from Musically where S_CODE={}".format(no)
        mycur.execute(q)
        rs=mycur.fetchone()
        if rs==None:
            print("Song Does Not Exist")
        else:
            print(rs)
            udate=input("Enter the Updated Release Date: ")
            uplays=int(input("Enter Updated Number of Plays: "))
            q1="update Musically set R_DATE='{}',PLAYS={} where S_CODE={}".format(udate, uplays, no)
            mycur.execute(q1)
            mycon.commit()
            display_song()
            print(mycur.rowcount,"Song Has Been Updated Successfully!!")
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def del_song():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        display_song()
        n=int(input("Enter the Number of Musically to be Deleted:"))
        for i in range(n):
            n=int(input("Enter the Song Code of the Song to be Deleted: "))
            q="select * from Musically where S_CODE={}".format(n)
            mycur.execute(q)
            rs=mycur.fetchone()
            if rs==None:
                print("Song Does Not Exist")
            else:
                ans=input('Are you sure you want to delete? (Y/N)')
                if ans.lower()=='y':
                    S_CODE=rs[0]
                    S_NAME=rs[1]
                    ARTIST=rs[2]
                    R_DATE=rs[3]
                    PLAYS=rs[4]
                    q0='Select * from SONGBACKUP whereS_CODE={}'.format(n)
                    mycur.execute(q0)
                    res=mycur.fetchall()
                    if rs==None:
                        q1="insert into SONGBACKUP values('{}','{}','{}','{}','{}')".format(S_CODE, S_NAME,ARTIST, R_DATE, PLAYS)
                        mycur.execute(q1)
                    else:
                        q3='delete from SONGBACKUP where S_CODE={}'.format(n)
                        mycur.execute(q3)
                        q4="insert into SONGBACKUP values('{}','{}','{}','{}','{}')".format(S_CODE, S_NAME,ARTIST, R_DATE, PLAYS)
                        mycur.execute(q4)
                        q2="delete from Musically where S_CODE={}".format(n)
                        print(mycur.rowcount, "Musically Have Been Deleted Sucessfully !!")
                        mycur.execute(q2)
                        mycon.commit()
                else:
                    print('Deletion unsucessful')
                    display_backup()
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()

def add_song():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        display_song()
        S_CODE=int(input("Enter the Song Code: "))
        S_NAME=input("Enter the Song Name: ")
        ARTIST=input("Enter the Artist Name: ")
        R_DATE=input("Enter the Release Date (YYYY-MM-DD): ")
        PLAYS=int(input("Enter the Number of Plays: "))
        q="insert into Musically values('{}','{}','{}','{}','{}')".format(S_CODE, S_NAME, ARTIST, R_DATE, PLAYS)
        mycur.execute(q)
        mycon.commit()
        display_song()
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
    

def get_db_connection():
    return mysql.connector.connect(host="localhost", user="root", password="kkss", database="Album")

def cancel_mem():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        display_users()
        cun = input("Enter the U_Name whose membership is to be cancelled: ")
        q = "SELECT * FROM users WHERE U_Name = %s"
        mycur.execute(q, (cun,))
        rs = mycur.fetchall()
        if rs:
            U_M_SHIP = 'NO MEMBERSHIP'
            mycur.execute("UPDATE users SET M_SHIP = %s WHERE U_Name = %s", (U_M_SHIP, cun))
            mycon.commit()
            print("Membership cancelled successfully!")
            display_users()
        else:
            print("User not found!")
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def update_memdet():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        display_membership()
        uno = int(input("Enter the Membership Code you want to update: "))
        q = "SELECT * FROM memberships WHERE M_CODE = %s"
        mycur.execute(q, (uno,))
        rs = mycur.fetchone()
        if rs:
            print("Current Details:", rs)
            PRICE = int(input("Enter updated price: "))
            mycur.execute("UPDATE memberships SET PRICE = %s WHERE M_CODE = %s", (PRICE, uno))
            mycon.commit()
            print("Membership details updated successfully!")
            display_membership()
        else:
            print("Invalid Membership Code!")
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def sign_user():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        mycur.execute("SELECT * FROM password WHERE TYPE = 'USER'")
        rs = mycur.fetchall()
        U_Name = input("Enter the U_Name: ")
        for r in rs:
            if r[1] == U_Name and r[3] == "USER":
                Pass_Word = input("Enter the Password: ")
                if r[2] == Pass_Word:
                    print("Login Successful!")
                    return
                else:
                    print("Wrong Password!")
                    return sign_user()
        print("Cannot log in as a User.")
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def update_mem():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        U_Name = input("Enter your U_Name: ")
        q = "SELECT * FROM USERS WHERE U_Name = %s"
        mycur.execute(q, (U_Name,))
        rs = mycur.fetchall()
        if not rs:
            print("User not found!")
        else:
            nmem = input("Enter your new membership plan: ").upper()
            if nmem in ("SILVER", "GOLD", "PLATINUM"):
                mycur.execute("UPDATE USERS SET M_SHIP = %s WHERE U_Name = %s", (nmem, U_Name))
                mycon.commit()
                print("Membership updated successfully!")
                display_users()
            else:
                print("Invalid membership plan!")
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def search_artist():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        display_song()
        art = input("Enter Artist to search for: ")
        q = "SELECT * FROM Musically WHERE ARTIST = %s"
        mycur.execute(q, (art,))
        rs = mycur.fetchall()
        if not rs:
            print("Artist not found!")
        else:
            print(tabulate(rs, headers=['S_CODE', 'S_NAME', 'ARTIST', 'R_DATE', 'PLAYS'], tablefmt='fancy_grid'))
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def create_pl():
    try:
        mycon = get_db_connection()
        mycur = mycon.cursor()
        U_Name = input("Enter your U_Name: ")
        q = "SELECT * FROM USERS WHERE U_Name = %s"
        mycur.execute(q, (U_Name,))
        rs = mycur.fetchone()
        if not rs:
            print("User not found!")
        else:
            p_code = rs[0]
            pl_name = input("Enter a name for your playlist: ")
            q = f"CREATE TABLE {pl_name} (S_CODE INT NOT NULL, S_NAME VARCHAR(30) NOT NULL, ARTIST VARCHAR(20) NOT NULL)"
            mycur.execute(q)
            mycon.commit()
            print("Playlist created! Add songs to it.")
            display_song()
            n = int(input("Enter the number of songs you want to add: "))
            for _ in range(n):
                song_code = int(input("Enter Song Code: "))
                q1 = "SELECT * FROM Musically WHERE S_CODE = %s"
                mycur.execute(q1, (song_code,))
                rss = mycur.fetchone()
                if rss:
                    S_CODE, S_NAME, ARTIST = rss[0], rss[1], rss[2]
                    q2 = f"INSERT INTO {pl_name} VALUES (%s, %s, %s)"
                    mycur.execute(q2, (S_CODE, S_NAME, ARTIST))
            mycon.commit()
            q3 = "INSERT INTO USER_PLAYLISTS (P_CODE, PL_NAME) VALUES (%s, %s)"
            mycur.execute(q3, (p_code, pl_name))
            mycon.commit()
            display_playlist(pl_name)
    except Exception as e:
        print("Error:", e)
    finally:
        mycur.close()
        mycon.close()

def add_songpl():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        U_Name=input("Enter your U_Name: ")
        q="SELECT * FROM USERS WHERE U_Name='{}'".format(U_Name)
        mycur.execute(q)
        rs=mycur.fetchone()
        if rs==None:
            print("USER NOT FOUND")
        else:
            apl_name= input("Enter the playlist name you want to add Musically to:")
            q1="SELECT FROM USER PLAYLISTS WHERE PL_NAME='{}'".format(apl_name)
            mycur.execute(q1)
            ps=mycur.fetchone()
            if ps==None:
                print("Playlist not found")
            else:
                n=int(input("Enter the number of Musically you want to add: "))
                display_song()
                for i in range(n):
                    song=int(input("Enter Song Code of the Song You Would Like to Add to Your Playlist: "))
                    q2="select * from Musically where S_CODE={}".format(song)
                    mycur.execute(q2)
                    rss=mycur.fetchall()
                    for r in rss:
                        S_code=r[0]
                        S_name=r[1]
                        artist_name=r[2]
                        q3="insert into {} values('{}','{}','{}')".format(apl_name,S_code,S_name,artist_name)
                        mycur.execute(q3)
                        print('done!')
                        mycon.commit()
                        x=apl_name
                        display_playlist(x)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()

def del_songpl():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        U_Name=input("Enter your U_Name:")
        q="SELECT * FROM USERS WHERE U_Name='{}'".format(U_Name)
        mycur.execute(q)
        rs=mycur.fetchone()
        if rs==None:
            print("USER NOT FOUND")
        else:
            dpl_name=input("Enter the playlist name you want to delete Musically from:")
            ql="SELECT * FROM USER_PLAYLISTS WHERE PL_NAME='{}'".format(dpl_name)
            mycur.execute(q1)
            ps=mycur.fetchone()
            if ps==None:
                print("Playlist not found")
            else:
                n=int(input('Enter the number of Musically you want to delete:'))
                display_song()
                for i in range(n):
                    dsong=int(input("Enter Song Code of the Song You Would Like to delete: "))
                    q2="delete from {} where S_code={}".format(dpl_name,dsong)
                    ch=input('Are you sure you want to delete this song from playlist?(Y/N)')
                    if ch.upper()=='Y':
                        mycur.execute(q2)
                        q3="select * from Musically where s_code={}".format(dsong)
                        mycur.execute(q3)
                        rec=mycur.fetchall()
                        for r in rec:
                            S_CODE=r[0]
                            S_NAME=r[1]
                            ARTIST=r[2]
                            R_DATE=r[3]
                            PLAYS=r[4]
                            q4="insert into SONGBACKUP values('{}','{}','{}','{}','{}')".format(S_CODE,S_NAME, ARTIST, R_DATE, PLAYS)
                            mycur.execute(q4)
                            mycon.commit()
                            print("Deleted sucessfully")
                            print('Archive of deleted song:')
                            display_backup()
                    else:
                        print("Deletion unsucessful")
                        mycon.commit()
                        x=dpl_name
                        print('Your updated playlist: ')
                        display_playlist(x)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def del_pl():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        U_Name=input("Enter your U_Name: ")
        q="SELECT FROM USERS WHERE U_Name='{}'".format(U_Name)
        mycur.execute(q)
        rs=mycur.fetchone()
        if rs==None:
            print("USER NOT FOUND")
        else:
            dpl_name=input("Enter the playlist name you want to delete:")
            q1="drop table {}".format(dpl_name)
            q2="delete from user playlists where PL_NAME='{}'".format(dpl_name)
            ch=input('Enter Are you sure you want to delete this playlist?(Y/N)')
            if ch.upper()=='Y':
                mycur.execute(q1)
                mycur.execute(q2)
                print('Deleted sucessfully')
            else:
                print("Deletion cancelled'")
                mycon.commit()
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
def songplayer():
    try:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="Album")
        mycur=mycon.cursor()
        display_song()
        no = int(input("Enter the Song Code of the Song whose snippet is to be played: "))
        q= "select * from Musically where S_CODE={}".format(no)
        mycur.execute(q)
        rs=mycur.fetchone()
        if rs==None:
            print("Song Does Not Exist")
        else:
            Sname = rs [1]
            print("The song has started playing...")
            play(Sname)
    except Exception as e:
        print(e)
    mycur.close()
    mycon.close()
#MAIN
#MAIN
def main():
    print('-'*20, "Welcome to Musically !!",'-'*20)
    print()
    print("Enter 1 to Sign in as an Admin")
    print("Enter 2 to Sign in as a User")
    print("Enter 3 to Create a New User Account")
    print("Enter X to exit Musically")
    sign=input("Enter your Choice: ")
    if sign.upper()=='X':
        exit()
    elif sign=='1':
        while True:
            print()
            print("1. Update Song Information (Plays, Years...etc)")
            print("2. Delete Musically")
            print("3. Add Musically")
            print("4. Check Cancellation of User's Membership")
            print("5. Update Membership Details")
            print("6. Display User Information")
            print("7. LOG OUT")
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                update_song()
            elif ch==2:
                del_song()
            elif ch==3:
                add_song()
            elif ch==4:
                cancel_mem()
            elif ch==5:
                update_memdet()
            elif ch==6:
                display_users()
            elif ch==7:
                ansl=input('Do you want to log out? (y/n)')
                if ans1.lower()=='y':
                    main()
    elif int(sign)==2:
        sign_user()
        while True:
            print()
            print("1. Updating Membership")
            print("2. Search for All Musically by an Artist")
            print("3. Create a Playlist and Add Musically")
            print("4. Add Musically to an existing Playlist")
            print("5. Delete Musically from a Playlist")
            print("6. Delete Playlist")
            print("7. Play Musically")
            print("8. LOG OUT")
            ch=int(input("Enter Your Choice: "))
            if ch==1:
                update_mem()
            elif ch==2:
                search_artist()
            elif ch==3:
                create_pl()
            elif ch==4:
                add_songpl()
            elif ch==5:
                del_songpl()
            elif ch==6:
                del_pl()
            elif ch==7:
                songplayer()
            elif ch==8:
                ans2=input('Do you want to log out? (y/n)')
                if ans2.lower()=='y':
                    main()
                    print("Logged out sucessfully")
    elif int(sign)==3:
        mycon=mysql.connector.connect(host="localhost", user="root",password="kkss", database="album")
        mycur=mycon.cursor()
        U_Name=input("Enter U_Name: ")
        U_ID=int(input("Enter the user code:"))
        Pass_W=input("Enter Password: ")
        Pass_We=input("Enter Your Password Again for Confirmation: ")
        print()
        if Pass_W!=Pass_We:
            print("Password does not match!")
            main()
        else:
            print('Enter')
            q="insert into password values('{}','{}','{}')".format(U_ID,Pass_W,U_Name)
            mycur.execute(q)
            mycon.commit()
            doj=date.today()
            print('Do you want a Musically membership?')
            display_membership()
            ch=input('Enter membership level if interested and * is membership is not needed: ')
            if ch.upper()=='SILVER':
                M_SHIP ='SILVER'
            elif ch.upper()=='GOLD':
                M_SHIP='GOLD'
            elif ch.upper()=='PLATINUM':
                M_SHIP='PLATINUM'
            elif ch=='*':
                M_SHIP ='NULL'
                q1="insert into users values('{}','{}','{}','{}'}".format(U_ID,U_Name,doj,M_SHIP)
                mycur.execute(q1)
                mycon.commit()
                while True:
                    print()
                    print("1. Updating Membership")
                    print("2. Search for All Musically by an Artist")
                    print("3. Create a Playlist and Add Musically")
                    print("4. Add Musically to an existing Playlist")
                    print("5. Delete Musically from a Playlist")
                    print("6. Delete Playlist")
                    print("7. Play Musically")
                    print('8. Log out')
                    ch=int(input("Enter Your Choice: "))
                    if ch==1:
                        update_mem()
                    elif ch==2:
                        search_artist()
                    elif ch==3:
                        create_pl()
                    elif ch==4:
                        add_songpl()
                    elif ch==5:
                        del_songpl()
                    elif ch==6:
                        del_pl()
                    elif ch==7:
                        songplayer()
                    elif ch==8:
                        ans3=input('Do you want to log out? (y/n)')
                        if ans3.lower()=='y':
                            break
                        else:
                            print("Invalid Option")
                            main()
main()
