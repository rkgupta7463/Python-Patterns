row=int(input("Enter the row number\n"))

c=ord("A")
for i in range(row):
      for j in range(row-i):
            print(end=" ")
      for j in range(i):
            print(chr(c)," ", end="")
            c=c+1
      print(" ")        