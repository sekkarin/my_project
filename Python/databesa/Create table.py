import pymysql
try:  # ตรวจจับคำสั่งที่คาดว่าจะเกิดข้อผิดพลาด

    con = pymysql.connect(host="localhost", user="root",
                          passwd="125478963", db="register")
    cs = con.cursor()
    # ประมวลผลคำสั่ง sql สร้างตาราง students
    cs.execute("""CREATE TABLE students (student_id INT(5) NOT NULL, 
                f_name CHAR(30) COLLATE utf8_bin, 
                l_name CHAR(30) COLLATE utf8_bin,
                e_mail VARCHAR(30) COLLATE utf8_bin,
                tel VARCHAR(10) COLLATE utf8_bin, 
                PRIMARY KEY(student_id))""")
    # ส่วนประมวลผลคำสั่ง sql สร้างตาราง teachers
    cs.execute("""CREATE TABLE teachers (teacher_id INT(3) NOT NULL, 
                f_name CHAR(30) COLLATE utf8_bin, 
                l_name CHAR(30) COLLATE utf8_bin,
                e_mail VARCHAR(30) COLLATE utf8_bin,
                tel VARCHAR(10) COLLATE utf8_bin, 
                PRIMARY KEY(teacher_id))""")
    # ส่วนประมวลผลคำสั่ง sql สร้างตาราง subjects
    cs.execute("""CREATE TABLE subjects (subject_id INT(3) NOT NULL, 
                subject_name CHAR(50) COLLATE utf8_bin, 
                unit INT(1),
                teacher_id INT(3), 
                PRIMARY KEY(subject_id))""")
    # ส่วนประมวลผลคำสั่ง sql สร้างตาราง registers
    cs.execute("""CREATE TABLE registers (student_id INT(5) NOT NULL, 
                subject_id INT(3) NOT NULL,
                semester INT(1) NOT NULL,
                register_date DATE, 
                PRIMARY KEY(student_id, subject_id, semester))""")
except pymysql.err.OperationalError:
    # แจ้งเตือนข้อผิดพลาดเมื่อไม่สามารถเชื่อมต่อกับฐานข้อมูลได้
    print("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    # แจ้งเตือนข้อผิดพลาดเมื่อเขียนคำสั่ง SQL ไม่ถูกต้อง
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    # แสดงผลเมื่อไม่มีข้อผิดพลาดเกิดขึ้น
    print("สร้างตาราง students, teachers, subjects และ registers เรียบร้อยแล้ว !!!")
    con.close()  # ยกเลิกการเชื่อมต่อฐานข้อมูลด้วยเมธอด close()
    cs.close()  # ยกเลิกคำขอเข้าไปจัดการกับฐานข้อมูลผ่านออบเจ็ค cursor()
