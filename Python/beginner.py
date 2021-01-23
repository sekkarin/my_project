print("ลงเขียนโปรแกรมสร้างชนิดข้อมูลดิกชันนารีเก็บรายชื่อ 3 คน ค่า value คือ ชื่อ นามสกุล ชื่อเล่น และเบอร์")
study_1 = {
    "ken_1":[
        ["name","sekkarin"],["lastname"],["Singhayoo"],["nickname","ken"]
        ],
    "ken_2":[
        ["name","ken_2"],["lastname","last2"],["nickname","kennnn_2"]
        ] ,     
}

print(study_1["ken_1"][0][1])
print(study_1["ken_2"][0][1])
print(study_1.keys())
print(study_1.get("ken_1")[0][1])

