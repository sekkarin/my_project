import pymysql 
try:
    con = pymysql.connect(host ="localhost",user = "root",password ="125478963",db ='')
    cs = con.cursor()
    cs.execute("CREATE DATABASE register")
except pymysql.err.OperationalError:
    print("can not connect")
except pymysql.err.ProgrammingError:
    print("คําสั่งผิด ...") 
else:
    print("Create database success")
    con.close()
    cs.close()