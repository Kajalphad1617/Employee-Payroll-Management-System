import Employee
import Emainmenu
import HR
import Etables
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="python",database="basicdb")
mycursor=mydb.cursor()

#----------------------------------------------------------------------------------------
def EmployeeManagement():
    while True:
        print("\t\t\t Employee Record Management\n")
        print("==============================================================")
        print("1. Display Employee Records ")
        print("2. Generate payment slip")
        print("3. Return to Main Menu")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 3-------> : "))
        if choice==1:
            Employee.displayEmp()
        elif choice==2:
            Employee.generateSlip()
        elif choice==3:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")
#----------------------------------------------------------------------------------------
def HRManagement():
    while True:
        print("\t\t\t HR Record Management\n")
        print("==============================================================")
        print("1. Add HR Record")
        print("2. Display HR Records")
        print("3. Search HR Record")
        print("4. Delete HR Record")
        print("5. Update HR Record")
        print("==============================================================")
        print("6. Display Employee Records ")
        print("7. Add Employee Record")
        print("8. Search Employee Record")
        print("9. Update Employee Record")
        print("10. Delete Employee Record")
        print("11. Generate payment slip")
        print("12. Return to Main Menu")
        print("===============================================================")
        
        choice=int(input("Enter Choice between 1 to 12-------> :  "))
        if choice==1:
            HR.insertHR()
        elif choice==2:
            HR.displayHR()
        elif choice==3:
            HR.searchHR()
        elif choice==4:
            HR.deleteHR()
        elif choice==5:
            HR.UpdateHR()
        elif choice==6:
            HR.displayEmp()
        elif choice==7:
            HR.addEmp()
        elif choice==8:
            HR.searchEmp()
        elif choice==9:
            HR.updateEmp()
        elif choice==10:
            HR.delEmp()
        elif choice==11:
            HR.generateSlip()
       
        elif choice==12:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue:")

