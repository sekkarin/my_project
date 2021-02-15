import pymysql
try:
    con = pymysql.connect(host="localhost", user="root",
                          password="125478963", db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("""INSERTINTO students(student_id,f_name,l_name,e_mail,tel)VALUES(00001,"sekkarin","singhayoo","sekkri1234@gmail.com","0800000000")""")
except pymysql.err.OperationalError:
    print("NOT CONNECT")
except pymysql.err.ProgrammingError:
    print("คําสั่งผิด")
else:
    
    print("SUCCESS")
    con.close()
    cs.close()
