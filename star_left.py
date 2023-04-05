row=int(input("Enter the row number!\n"))
print("")
num=1
for i in range(row):
        for j in range(i+1):
            print("*",end=" ")
            num = num + 1
        print(" ")