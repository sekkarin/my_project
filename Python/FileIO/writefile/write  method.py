file = open(r"C:\Users\KEN\Documents\GitHub\my_project\Python\FileIO\data_file\Myfile.txt","r",encoding="utf8")
# print("ตําแหน่งตัวชี้ = ",file.tell())
print("file read =",file.read())
# print("ตําแหน่งตัวชี้ = ",file.tell())
print("method seek : ") 
file.seek(10)
print("file read =",file.read())
file.close()

#open file is write Not found creat new file
file_n = open(r"FileIO\data_file\Newfile_method.txt","w")
file_n.write("saaaaaaaaaaawaddddddeeeeeeeee")
file_n.truncate(5)
file_n.close()
file_n = open(r"FileIO\data_file\Newfile_method.txt")
print("New messages :", file_n.read())
file_n.close()