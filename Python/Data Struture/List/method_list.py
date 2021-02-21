list_number = [0,1,2,3,4,5,6,7,8,9]

list_number.append(10)
print("list number",list_number)
print("list_number.append(10)", list_number)
list_new = list_number.copy()
print("list_new = list_number.copy() ",list_new)

print("list_new.count(5)",list_new.count(5))

list_number.extend(list_new)
print("list_number.extend(list_new)",list_number)

list_number.insert(10,"mind")
print("list_number.insert(10,\"mind\")",list_number)

list_number.pop(10)
print("list_number.pop(10)",list_number)

list_number.reverse()
print("list_number.reverse()",list_number)

list_number.sort(reverse=False)
print("list_number.sort(reverse=False)",list_number)

print("len(list_number)",len(list_number))



