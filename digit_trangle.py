row=int(input("Enter the row number!\n"))

num=1
for i in range(row):
        for j in range(row-i):
              print(end=" ")
        for j in range(i+1):
            print(num,end=" ")
            num = num + 1
        print(" ")


     