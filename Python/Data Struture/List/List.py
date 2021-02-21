list_number = [0,1,2,3,4,5,6,7,8,9]
list_eng = ['A','B','C','D','E']

# print(list_number)
# print(list_eng)

print("จํานวนข้อมูล list eng",len(list_eng))
print("จํานวนข้อมูล list number",len(list_number))

#การเข้าถึง
# var[Start:stop:step]
print("index 0  =",list_number[0])
print("index 8  =",list_number[8])
print("index -1 =",list_number[-1])
print("index -5 =",list_number[-5])
print("index -4 =",list_number[-4])
print("index :5 =",list_number[:5])
print("index 5: =",list_number[5:])
print("index Step[0:9:2] =",list_number[0:9:2])