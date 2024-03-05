import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="python",database="basicdb")
mycursor=mydb.cursor()

mycursor.execute("SHOW TABLES LIKE 'HRrecord' ")
result=mycursor.fetchone()
if result : 
    pass
else: #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE HRrecord(HRID varchar(10) PRIMARY KEY, Password varchar(20))""")
    Hr=("kajal1617","456")
    query2="INSERT INTO HRrecord VALUES(%s, %s)"
    mycursor.execute(query2,Hr)
    mydb.commit()
    
mycursor.execute("SHOW TABLES LIKE 'EmpRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("CREATE TABLE EmpRecord(EMPID int unique,EMPNAME varchar(15),DEPARTMENT varchar(20),SALARY decimal(10,2))")
    query1=("INSERT INTO EmpRecord(EMPID,EMPNAME,DEPARTMENT,SALARY) VALUES(%s, %s, %s, %s)")
    mycursor.execute(query1)
    mydb.commit()

    
    mycursor.execute("SHOW TABLES LIKE 'LogRecord' ")
    result=mycursor.fetchone()
    if result : 
        pass
    else : #if Table doesn't exists then it will be created
        mycursor.execute("CREATE TABLE LogRecord(EMPID int,EMPNAME varchar(15),PASSWORD varchar(10)")
        query3=("INSERT INTO LogRecord(EMPID,EMPNAME,PASSWORD) VALUES(%s, %s, %s)")
        mycursor.execute(query3)
        mydb.commit()
        
