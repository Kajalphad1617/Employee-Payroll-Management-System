import mysql.connector
import Etables

mydb=mysql.connector.connect(host="localhost",user="root",passwd="python",database="basicdb")
mycursor=mydb.cursor()

#---------------------------------------------------------------------------------------------------------                 
def displayHR():
    print()
    print(" HR Records: \n")
    mycursor.execute("SELECT * FROM HRrecord")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("-"*20,"Row no.",row_no,"-"*20)
        print("\t             HRID: ", rows[0])
        print("\t            Password: ", rows[1])
        print()
    x=input("Press Enter to continue: ")
    return
#---------------------------------------------------------------------------------------------------------         
def insertHR():
    while True :
        Hr=()
        print()
        HRID=input("Enter HRID:-  ")
        Password=input(" Enter Password to be set:-  ")
        Hr=(HRID,Password)
        query="INSERT INTO HRrecord VALUES (%s, %s)"
        mycursor.execute(query,Hr)
        mydb.commit()
        print()
        print("****** HR ADDED SUCCESSFULL ******")
        ch=input("Do you wish to do add more HR ?[Yes/No] :-  ")
        if ch=="yes" or ch=="Yes" or ch=="yes":
            continue
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#---------------------------------------------------------------------------------------------------------         
def deleteHR():
    while True:
        print()
        HRID=input(" Enter HRID whose details to be deleted :-  ")  
        mycursor.execute("DELETE from HRrecord where HRID={0}".format("\'"+HRID+"\'"))
        mydb.commit()
        print("****** HR DELETED SUCCESSFULLY *******")
        ch=input("Do you wish to delete more HR ?[Yes/No] :-  ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#---------------------------------------------------------------------------------------------------------     
def searchHR():
    while True:
        print()
        Search=input(" Enter HRID to be Searched:-  ")  
        mycursor.execute("SELECT * FROM HRrecord where HRID={0}".format("\'"+Search+"\'"))
        reco
        rds=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print("-"*20,"Searched HR Record","-"*20)
                print("\t             HRID: ", rows[0])
                print("\t            Password: ", rows[1])
                print()
        else:
            print("Search Unsuccesfull")
            
        ch=input("Do you wish to Search more HR ?[Yes/No] :-  ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------- 
def UpdateHR():
    while True:
        print()
        Hr=()
        HRID=input(" Enter HRID for whose details need to be updated :-  ")
        Password=input(" Enter new Password :- ")
        query="UPDATE HRrecord SET Password = %s WHERE HRID=%s"
        Hr=(Password,HRID)
        # query="INSERT INTO HRrecord VALUES (%s, %s)"
        mycursor.execute(query,Hr)
        mydb.commit()
        print("****** HR DETAILS UPDATED SUCCESSFULLY ******")
        ch=input("Do you wish to Search more HR ?[Yes/No] :-  ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return


       
#--------------------------------------------------------------------------------------------------------------------------------        
def displayEmp():
        print()
        mycursor.execute("SELECT * FROM EmpRecord")
        results = mycursor.fetchall()
        print("**************************************************")
        print('%5s'%"EMPID",'%15s'%'EMPNAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
        print("**************************************************")
        count=0
        for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
        count+=1
        print("-"*20, "TOTAL RECORD : ",count,"-"*20)
        x=input("Press any key to return to the employee Menu")
        return


#----------------------------------------------------------------------------------------------------------------
def addEmp():
        print("-"*20," ADD NEW EMPLOYEE", "-"*20)
        eno = int(input("Enter employee number :- "))
        en = input("Enter employee name :- ")
        dp = input("Enter department:-  ")
        sl = int(input("Enter Salary :- "))
        query="insert into EmpRecord values("+str(eno)+",'"+en+"','"+dp+"',"+str(sl)+")"
        mycursor.execute(query)
        mydb.commit()
        # print(query)
        print("-----------------------------------------------------")
        print("\n---------- RECORD ADDED SUCCESSFULLY!----------")

#----------------------------------------------------------------------------------------------------------------
def searchEmp():
        print("-----------------------------------------------------")
        print("       ******SEARCH EMPLOYEE  ******")
        print("-----------------------------------------------------")
        en = int(input("Enter Employee number to search :- "))
        query="select * from EmpRecord  where EMPID="+str(en)
        mycursor.execute(query)
        results = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
        
            print("**************************************************")
            print('%5s'%"EMPID",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
            print("**************************************************")
            for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
        print("-"*50)

#----------------------------------------------------------------------------------------------------------------
   
def updateEmp():
        print("-----------------------------------------------------")
        print("       ****** EMPLOYEE EDIT FORM ******")
        print("-----------------------------------------------------")
        en = int(input("Enter Employee number to update :- "))
        query="select * from EmpRecord where EMPID="+str(en)
        mycursor.execute(query)
        results = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
        
            print("**************************************************")
            print('%5s'%"EMPID",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
            print("**************************************************")
            for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
        print("-"*50)
        ans = input("Are you sure to update ? (y/n)")
        if ans=="y" or ans=="Y":
            d = input("Enter new department to update (enter old value if not to update) :- ")
            s = int(input("Enter new salary to update (enter old value if not to update) :- "))
            query="update EmpRecord set department='"+d+"',salary="+str(s) + " where EMPID="+str(en)
            mycursor.execute(query)
            mydb.commit()
            print("\n## RECORD UPDATED  ##")
            print(query)

#----------------------------------------------------------------------------------------------------------------
                    
def delEmp():
        print("-----------------------------------------------------")
        print("       ****** DELETE EMPLOYEE INFO ******")
        print("-----------------------------------------------------")
        en = int(input("Enter Employee number to delete :- "))
        query="select * from EmpRecord where EMPID="+str(en)
        mycursor.execute(query)
        results = mycursor.fetchall()
        if mycursor.rowcount<=0:
            print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
        
            print("**************************************************")
            print('%5s'%"EMPID",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY')
            print("**************************************************")
            for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3])
        print("-"*50)
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from EmpRecord where EMPID="+str(en)
            mycursor.execute(query)
            mydb.commit()
            print("\n*****  RECORD DELETED *****")


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

            
#--------------------------------------------------------------------------------------------------------- 

     
