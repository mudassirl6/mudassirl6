import mysql.connector
import pandas as pd

# connection is established...
mysqldb = mysql.connector.connect(
    host = "localhost",user='root',
    password = "MudassirL6", database = "m")
mysqldbcursor = mysqldb.cursor()
mysqldbcursor.execute("select * from m")
# performing crud operations...
#1.create..---------------------------------------------------------------
# mysqldbcursor.execute("create table Accounts(id int,account_number int,amount int,account_name varchar(30),account_type varchar(30),balance float,opening_date date,last_transaction_date date,status varchar(20),branch_name varchar(20))")
# mysqldb.commit()
# print("Accounts table is created..")
# mysqldbcursor.execute("desc Accounts")
result = mysqldbcursor.fetchall()
print(result)

# # #2. insert into the table...------------------------------------------------------------------
# try:
    
#     mysqldbcursor.execute("insert into Accounts values (12,234,24000,'johnwick','savings',12000,'2014-12-22','2024-01-12','active','SBI'),(13,235,30000,'benjamin','current',4000,'2015-05-23','2024-02-21','active','HDFC');")
#     mysqldb.commit()
#     print("Rcord inserted into the table")
# except:
#     print("Error in the query")
#     mysqldb.rollback()

# #3.display record.-----------------------------------------------------------------------------

# mysqldbcursor.execute("select * from Accounts")
# column_names = [i[0] for i in mysqldbcursor.description]

# result = mysqldbcursor.fetchall()

# df = pd.DataFrame(result,columns=column_names)
# print(df.head())

# #4.update the record.---------------------------------------------------------------------------
# try:
#     mysqldbcursor.execute("update accounts set account_name =  'Mudassir' Where id = 12" )
#     mysqldb.commit()
# except:
#     mysqldb.rollback()
# print("After performing Update Operation.")
# mysqldbcursor.execute("select * from Accounts")

# result = mysqldbcursor.fetchall()

# df = pd.DataFrame(result,columns=column_names)
# print(df.head())
# #5 deleting the record..------------------------------------------------------------------------
# try:
#     mysqldbcursor.execute("delete from accounts Where id = 12" )
#     mysqldb.commit()
# except:
#     mysqldb.rollback()
# print("After performing delete Operation.")
# mysqldbcursor.execute("select * from Accounts")

# result = mysqldbcursor.fetchall()

# df = pd.DataFrame(result,columns=column_names)
# print(df.head())


# mysqldb.close()

