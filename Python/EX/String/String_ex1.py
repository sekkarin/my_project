#ให้เขียนโปรแกรมแสดงสระภาษาอังกฤษ และ แสดง ตําแหน่งที่อยู่แต่ละตัว
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("แสดงสระ ภาษาอังกฤษ ในตัวแปร s  \n\
    A : {A} ตําแหน่งที่ : {A_index}\n\
    E : {E} ตําแหน่งที : {E_index}\n\
    I : {I} ตําแหน่งที่ : {I_index}\n\
    O : {O} ตําแหน่งที่ : {O_index}\n\
    U : {U} จําแหน่งที่ : {U_index}".format(
        A = s[s.find('A')],A_index = s.find('A'),
        E = s[s.find('E')],E_index = s.find('E'),
        I = s[s.find('I')],I_index = s.find('I'),
        O = s[s.find('O')],O_index = s.find('O'),
        U = s[s.find('U')],U_index = s.find('U')))

print("ให้เขียนโปรแกรมแสดงเฉพาะตัสอักฤษ \"CDEF\" ,\"MNOPOR\" ,\"VWXYZ\"")

print("CDEF   : " , s[s.index('C'):s.index('F')+1])

print("MNOPOR : " , s[s.index('M'):s.index('R')+1])
print("VWXYZ  : " , s[s.find('V'): s.find('Z')+1])

print("เขียนโปรแกรมรับข้อมูลทางคีย์บอร์ด และ จัดรูปแบบตามที่กําหนด")
name        =   input(str("name"))
address     =   input(str("address"))
zip_code    =   input(str("zip_code"))
To_name     =   input(str("To_name"))
To_address  =   input(str("To_address"))
To_zip_code =   input(str("To_zip_code"))
print(f"From\n\
    Name      {name}\n\
    Address   {address}\n\
    Zip code  {zip_code}\n\
        To \n\
            Name        {To_name}\n\
            address     {To_address}\n\
            zip code    {To_zip_code}")

name = input(str("ป้อนชื่อ ให้เว้นวรรค นามสกุล"))
spilt_name = name.split(' ')
print(f"\
    ชื่อ {spilt_name[0]} จํานวนตัวอักษร {len(spilt_name[0])}\n\
นามสกุล {spilt_name[1]} จํานวนตัวอักษร {len(spilt_name[1])}")