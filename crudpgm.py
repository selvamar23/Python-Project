import pyodbc 
import pandas as pd
from sqlalchemy import create_engine


testserver      = "HPLAPCHN045\SSISSQLSERVERMDX"
testdb          = "testdb"
testdriver      = "ODBC Driver 11 for SQL Server"


testdatabaseconnection = f'mssql://@{testserver}/{testdb}?driver={testdriver}'
testengine = create_engine(testdatabaseconnection)
testdbconn = testengine.connect()


class dataCrud:

    def getDataFromSql(self,qry):
        df  = pd.read_sql(qry,testdbconn)
        # df.to_csv("output.csv")
        print(df)



    def createTable(self,createscript):
        try:
            testdbconn.execute(createscript)
            print('Table has been Created successfully')
        except Exception:
            print('Table already available')


        

    def insertDataToSql(self,insertqry):
        try:
            testdbconn.execute(insertqry)
            print('The records has been inserted successfully')
        except Exception:
            print('please check the insert script')


    def alterTable(self,alterqry):
        try:
            testdbconn.execute(alterqry)
            print('Table altered done..')
        except Exception:
            print('can not alter the table.')


    def deleteRecordToTable(self,qry,value):
        try:
            testdbconn.execute((qry),value)
            print('record deleted successfully')
        except Exception:
            print('can not delete the record...' )



# print(insertrecordtotable)
# createTable(createtableqry)
# alterTable(altertablescript)
# insertDataToSql(insertrecordtotable)


# deleteRecordToTable(deleteRecordqry,empcode)

readqry = 'select * from Lynk_Employee_master'

createtableqry = """
    Create table Lynk_Employee_master
    (   empid        varchar(10)    not null,
        empname      varchar(40),
        empaddr      varchar(80),
        empmobile    varchar(10),
        primary key(empid)
    )
"""

insertqry = """
    Insert into Lynk_Employee_master(empid,empname,empaddr,empmobile) 
    values ('M03889','SELVAKUMAR M','CHENNAI','9994799648')

    Insert into Lynk_Employee_master(empid,empname,empaddr,empmobile) 
    values ('M03994','MOHANRAJ','CHENNAI','9944493555')
"""

altertableqry    = """
    Alter table Lynk_Employee_master add  primary key (empid)
    """

deleteRecordqry     = """
    Delete from  Lynk_Employee_master where empid = ?
"""    
empcode = 'M03994'

objcall = dataCrud()

objcall.createTable(createtableqry)                     #Create a Table
# objcall.deleteRecordToTable(deleteRecordqry,empcode)    # Delete a record from a table
# objcall.getDataFromSql(readqry)                         # Get Data from table
objcall.insertDataToSql(insertqry)                      # Insert new record to table
objcall.getDataFromSql(readqry)                         # Get Data from table

# getDataFromSql(readqry)