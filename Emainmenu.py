import Eoperation
import Employee
def HRmenu() :
    while True:
        print("\t\t\t HR Menu \n")
        print("==============================================================")
        print("1. Employee Management")
        print("2. HR management")
        print("3. Logout ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 3 -------> : "))
        if choice==1:
            Eoperation.EmployeeManagement()
        elif choice==2:
            Eoperation.HRManagement()
        elif choice==3:
            print("Thanks for visiting our portal:))")
            
            break
        else:
            print("Wrong Choice......Enter Your Choice again")
            continue
    

def Employeemenu() :
    while True:
        print("\t\t\t Employee Menu \n")
        print("==============================================================")
        print("1. Display employee Record")
        print("2. Generate payment slip")
        print("3. Exit ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 3-------> : "))
        if choice==1:
            Employee.displayEmp()
        elif choice==2:
            Employee.generateSlip()
        elif choice==3:
            print("Thanks for visiting our portal:))")
            
            break
        else:
            print("Wrong Choice......Enter Your Choice again")
            continue
   
