# method           Meaning                 Pattern
# getcwd()     disploy name dicectory      os.getcwd()
# mkdir()     create directory             os.mkdir(dir_name)
# chdir()     Access directory             os.chdir(dir_name)
# rename()    rename directory             os.rename(old name ,new name)
# rmdir()     remove directory             os.rmdir(dir name)

import os
print(os.getcwd())
try:
    os.mkdir(r"C:\Users\KEN\Documents\GitHub\my_project\Python\OS\new_os")
except FileExistsError:
    print("มีไฟล์อยู่แล้ว")
else:
    os.chdir(r"C:\Users\KEN\Documents\GitHub\my_project\Python\OS\new_os")
    print(os.getcwd())
    file = open(
        r"C:\Users\KEN\Documents\GitHub\my_project\Python\OS\new_os\text_os.txt", 'w')
    file.write("hello word")
    file.close()
