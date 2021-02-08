with open(r"FileIO\data_file\binary.txt","wb") as file:
    msg = b"heloo i am binary file "
    file.write(msg)
with open(r"FileIO\data_file\binary.txt","rb") as file:
    print(file.read())
# r means raw
# b means bytes
# u means unicode
# f means format