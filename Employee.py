import Etables
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="python",database="basicdb")
mycursor=mydb.cursor()
       
#--------------------------------------------------------------------------------------------------------------------------------        
def displayEmp():
        print()
        empid=int(input("Enter Employee Id: "))
        mycursor.execute("SELECT * FROM EmpRecord WHERE EMPID={}".format(empid))
        results = mycursor.fetchone()
        # print(results)
        print("************** YOUR PROFILE **************")
        for i in results:
                print("     EMPID: ",  results[0])
                print("     EMPNAME: ",  results[1])
                print("     DEPARTMENT: ", results[2])
                print("     SALARY:",  results[3])
                break
        return


#----------------------------------------------------------------------------------------------------------------
# def clear():
#         for i in range(1,50):
#             print()
            
def generateSlip():
        import datetime
        
        
        
        en = int(input("Enter Employee number to print salary slip :-  "))
        ab = int(input("Enter absent days of above Employee :  "))
        print("-"*80)
        print("             ************  SALARY SLIP  ************")
        print("-"*80)
        
        query="select * from EmpRecord where EMPID="+str(en)
        mycursor.execute(query)
        results = mycursor.fetchone()
        if mycursor.rowcount<=0:
            print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            x=datetime.datetime.now()
            present_Day=30-ab
            print("*"*80)
            print("EMPID :",results[0]," "*10,"NAME :",results[1]," "*10,"present_Day :",present_Day)
            print("DEPARTMENT:",results[2]," "*8,"Date :",(x.strftime("%c")))
            print("*"*80)
            
            s = int(results[3])
            absent=int(results[3])*ab/30
            print("absent:",absent)
            hra = s * 12/100
            da = s * 15/100
            it = 200
            nps = (s+hra)*10/100
            gross = s +hra+da+nps
            ded = it + nps
            net = gross - ded -absent
            tded=it + nps
            print("%19s"%"EARNING","%27s"%"DEDUCTION")
            print("-"*80)
            print("%20s"%"Basic  :"+str(s),"%22s"%"INC TAX :"+str(it))
            print("%20s"%"HRA    :"+str(hra),"%20s"%"NPS    :"+str(nps))
            print("%20s"%"DA     :"+str(da))
            print("%20s"%"NPS    :"+str(nps))
            print("-"*80)
            print("     GROSS :",gross," NET SALARY :",net,"  TOTAL DED :",tded)
        print("-"*80)

        print("=== PRESS ANY KEY ===")
        input()
#----------------------------------------------------------------------------------------------------------------





