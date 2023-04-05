name=input("Enter ur name\n")
print("Name Pattern")
for i in range(len(name)):
    for j in range(len(name)-i):
        print(end=" ")
    for j in range(i+1):
        print(name[j],end=" ")
    print(" ")  