try:
    with open("D:\\python\\MyData.txt","r") as x:
        print(x.read())
    print(x.closed)
except FileNotFoundError:
    print("File not Present")
