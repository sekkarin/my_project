import pymysql
# ทําการเชื่อมต่อ
con = pymysql.connect(host="localhost", user="root",
                      password="125478963", db='')
# คําสั่งที่ใช้จัดการกับฐานข้อมูล select insert delete updata ผ่านตัว ออบเจ็ค cursor ()
cs = con.cursor()
# execute ประมวณผลคําสั่ง จาก SQL 
cs.execute("show databases")
# นําข้อมมูลจากคําสั่ง SQL มาแสดง หนึ่งเรคอร์ด
sv = cs.fetchone()

print(sv)
# ยกเลิกคําสั่งการเชื่อมต่อ
con.close()
cs.close()
