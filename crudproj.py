import pyodbc 
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Table,Integer,String
from sqlalchemy.ext.declarative import declarative_base

server = "HPLAPCHN045\SSISSQLSERVERMDX"
database = "testdb"
driver   = "ODBC Driver 11 for SQL Server"

livedbconn = f'mssql://@{server}/{database}?driver={driver}'
engine = create_engine(livedbconn,echo = True)
conn = engine.connect()


Base = declarative_base()

Session=sessionmaker(bind=engine)

session = Session()

class Employee(Base):
    __tablename__   = 'Employee_master'

    empid       = Column(String(10), primary_key = True)
    empname     = Column(String(40))
    empaddr     = Column(String(80))
    empmobile   = Column(String(10))

# print(engine)

Base.metadata.create_all(engine)   #For create a new table in database

# To add a record in employee master table

try:

    empmas = Employee(empid = 'M03889',empname = 'SELVAKUMAR M',empaddr = 'CHENNAI',empmobile = '9994799648')
    session.add(empmas)

    # To add multiple record in employee master table
    session.add_all([
                    Employee(empid='M03994',empname = 'MOHANRAJ',empaddr = 'BANGALORE',empmobile = '9944494555'),
                    Employee(empid='9084',empname = 'KARTHIKUMAR S',empaddr = 'CHENNAI',empmobile = '9999999648'),
                    Employee(empid='M03665',empname = 'PAVAN',empaddr = 'HYDERABAD',empmobile = '9994899648')
                    ])
    session.commit()
    print('Record inserted successfully...')
except Exception as err:
    session.rollback()
    print('Can not inserted the values.please check the input statement.')




# To fetch all data from employee master table 

result = session.query(Employee).all()
for row in result:
    print("empid : " , row.empid,"emp name : " , row.empname, "emp address : " , row.empaddr, "emp mobile : " ,row.empmobile)
    
# To fetch one record from employee master table
result2 = session.query(Employee).filter(Employee.empid == 'M03889')
for row in result2:
    print("empid : " , row.empid,"emp name : " , row.empname, "emp address : " , row.empaddr, "emp mobile : " ,row.empmobile)
    