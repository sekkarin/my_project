dict_number = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
dict_eng = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'}
dict_test = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
print("dict_test.fromkeys('1')", dict_test.fromkeys('1'))
print("dict_number.get(5)", dict_number.get(2))
print("dict_eng.items() = ", dict_eng.items())
print("dict_number.keys()", dict_number.keys())
print("dict_eng.pop('a')", dict_eng.pop('a'), dict_eng)
print("dict_number.popitem()", dict_number.popitem(), dict_number)
print("dict_number.setdefault(5,'5')",
      dict_number.setdefault(5, '5'), dict_number)
print("dict_number.setdefault(6,[1,2]))",
      dict_number.setdefault(6, [1, 2]), dict_number)
print("dict_number.values()", dict_number.values())
print("len(dict_number)", len(dict_number))
del dict_number[6]
print("del dict_number.[6]",dict_number)