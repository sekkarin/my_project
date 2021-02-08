msg = "hello world! I'm ironman "
try:
    file = open(r"FileIO\data_file\Newfile.txt","w")
    file.write(msg)
    file.close()
except FileNotFoundError:
    print("Not Fond ")
else:
    print("Write success")