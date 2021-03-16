import pymysql as msql


class database:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def Createdatabases(self, name_db):
        self.name_db = name_db
        try:
            con = msql.connect(
                host=self.host, user=self.user, passwd=self.passwd)
            cs = con.cursor()
            cs.execute("CREATE DATABASE %s" % (self.name_db))
        except msql.err.OperationalError:
            print("Not connect database")
        except msql.err.ProgrammingError:
            print("The order is not correct.")
        else:
            print("Success")
            con.close()
            cs.close()

    def Createtable(self, table, db):
        self.db = db
        self.table = table
        try:
            con = msql.connect(host=self.host, user=self.user,
                               passwd=self.passwd, db='%s' % self.db)
            cs = con.cursor()
            cs.execute("%s" % table)
        except msql.err.OperationalError:
            print("Not connect database")
        except msql.err.ProgrammingError:
            print("The order is not correct.")
        else:
            print("Success")
            con.close()
            cs.close()

    def InsertDAtabase(self, dbinsert, db, charset='utf8'):
        self.db = db
        self.dbinsert = dbinsert
        self.charset = charset
        try:
            con = msql.connect(host=self.host, user=self.user,
                               passwd=self.passwd, db='%s' % self.db,charset='%s'%self.charset)
            cs = con.cursor()
            cs.execute("%s" % self.dbinsert)
            
        except msql.err.OperationalError:
            print("Not connect database")
        except msql.err.ProgrammingError:
            print("The order is not correct.")
        else:
            print("Success")
            con.commit()
            con.close()
            cs.close()

studenst = """
    CREATE TABLE students(
    student_id INT(5) NOT NULL,
    f_name CHAR(30) COLLATE utf8_bin,
    l_name CHAR(30) COLLATE utf8_bin,
    email VARCHAR(30) COLLATE utf8_bin,
    tell VARCHAR(10) COLLATE utf8_bin,
    PRIMARY KEY(student_id)
);"""
insert_data = """
INSERT INTO students(student_id,f_name,l_name,email,tell)
VALUES(01235,"ken","namelast","sekk@gmail.com","0800000000")
"""

db1 = database('localhost', 'root', '125478963')
# db1.Createtable(studenst, 'rgt')
db1.InsertDAtabase(insert_data,'rgt')
