row=int(input("Enter the row number!\n"))

num=65
for i in range(row):
        for j in range(i+1):
            ch = chr(num)
            print(ch,end=" ")
        num = num + 1
        print(" ")


     