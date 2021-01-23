mounts =        ["Jan","May","Jul","Aug","Oct","Dec"]
mounts_insert = ["Feb","Mar","Apr","Jun","Sep","Nov"]
print("1 แทรกเดือน  3 แสดงข้อมูลที่เหลือ")
mounts.insert(1,mounts_insert[0])
mounts.insert(2,mounts_insert[1])
mounts.insert(3,mounts_insert[2])
mounts.insert(5,mounts_insert[3])
mounts.insert(8,mounts_insert[4])
mounts.insert(10,mounts_insert[5])
print(mounts)
print("2 ลบเดือนที่ (2 5 9)")
mounts.pop(2)
mounts.pop(5)
mounts.pop(9)
print("3 แสดงข้อมูลที่เหลือ")
print(mounts)

A ={10,12,15,17,19,20,25,22}
B ={9,11,13,15,16,17,18,19,20,}
C ={15,16,18,20,22,26,28,30}

print("A & B",A&B)
print("A & C",A&C)
print("B | C",B|C)
print("A | C",A|C)
print("A - C",A-C)
print("B & A",B-A )
