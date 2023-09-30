try:
    x=open("D:\python\MyData.txt",'a')
    print(x)
    x.write("Hai Welcome to Anudip")
    x.write(str(20))
    x.write("\n")
    x.write("Python TTT")
    print("File Created Successfully")
    x.close()
except FileNotFoundError:
    print("File not Present")
