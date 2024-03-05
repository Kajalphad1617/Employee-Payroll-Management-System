import mysql.connector
import sys
import Emainmenu
import Etables
mydb = mysql.connector.connect(host="localhost",user="root",passwd="python",database="basicdb")
mycursor = mydb.cursor()

#---------------------------------------------------------------------------------------------------------
def login_to_HR() : # HR Login
        print("\n")
        print("|                       ~**~  T  H  E    A M D E V     C O M P A N Y  ~**~                   |")
        print()
        print("                            */  LOGIN  TO YOUR ACCOUNT  /*                                   \n")
        HRID=input("\t  HR Enter your ID : ")   
        password=input("\t HR Enter your Password : ")
        
        print()
        mycursor.execute("SELECT Password from HRrecord where HRID={0}".format("\'"+HRID+"\'"))
        result=mycursor.fetchone()
        if result:
            temp,=result #coverting tuple to integer for comparing password
            if temp==password: # authenticated HRIDs and passwords
                print("\n\t\t    WELCOME {0} to THE  AMDEV  COMPANY  \n ".format("\'"+HRID+"\'"))
                Emainmenu.HRmenu()
                
            else :
                print("\t INVALID PASSWORD OR HRID ! TRY AGAIN ")
                
                # continue

        else :
                print("\t NO SUCH HRID ! TRY AGAIN ")
                # continue
                

        print("*---------------------------------------------------------------------------------* \n")
#---------------------------------------------------------------------------------------------------------
def Employee_login(): # Emp login
    
    print("\n")
    print("|                       ~~  T  H  E    A  M D E V  C O M P A N Y  ~~                   |")
    print()
    print("1.Employee Registration")
    print("2.Employee Login")

    
    ch=int(input("Enter choice--> "))
    if ch==1:
        Hr=()
        EMPID=input("Enter your EMPID:- ")
        EMPNAME=input("Enter your Name:- ")
        Password=input("Enter Password to be set:- ")
        Hr=(EMPID,EMPNAME, Password)
        query="INSERT INTO LogRecord VALUES (%s, %s,%s)"
        mycursor.execute(query,Hr)
        mydb.commit()
        mycursor.execute("SELECT EMPID from LogRecord where EMPID={0}".format("\'"+EMPID+"\'"))
        result=mycursor.fetchone()
        if result:
            print("Account successfully created")
        else:
            print("Account already Exists")
        Employee_login()

    elif ch==2:
            EMPID=input("\t  Enter EMPID : ")   
            password=input("\t  Enter Password : ")
            print()
            mycursor.execute("SELECT Password from LogRecord where password={0}".format("\'"+password+"\'"))
            result=mycursor.fetchone()
            if result:
                temp,=result 
                if temp==password: # authenticated HRIDs and passwords
                    print("\n\t\t    WELCOME {1} to THE AMDEV COMPANY  \n ".format("\'"+EMPID+"\'"))
                    Emainmenu.Employeemenu()
                    
                else :
                    print("\t INVALID PASSWORD OR HRID ! TRY AGAIN ")
                    # continue

            else :
                print("\t NO SUCH HRID ! TRY AGAIN ")
                
                # continue

       
            print("*---------------------------------------------------------------------------------* \n")
    else:
        print("Enter valid choice")
        Employee_login()
#---------------------------------------------------------------------------------------------------------       
def menu() :
    
    print("****************************************************************************")
    print("*                                                                          *")
    print("*             Welcome to  T H E    A M D E V    C O M P A N Y              *")
    print("*                                                                          *")
    print("****************************************************************************")

   
    print("     ======================= MENU =======================                \n")
    print(" 1. Login as a HR")
    print(" 2. Login as a Employee")
    print(" 3. EXIT \n\n ") 

    while True :
        ch= input(" Select [ 1/2/3 ] :-  ")
        print()
        if ch== "1" :
            login_to_HR()
            break
        elif ch== "2" :
            Employee_login()
            break
        elif ch== "3" :
            cancel_request = input(" DO YOU WISH TO EXIT... [yes/no ] :-  ")
            if cancel_request in ["yes","Yes","YES"] :
                sys.exit()
            break
        else :
            print(" INVALID COMMAND ")
            print(" RETRY \n")
            continue
#------------------------------------------------------------------------------------------

menu()
