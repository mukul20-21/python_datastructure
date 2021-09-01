num = int(input("Enter the number of rows for triangle:"))
k = 1
for i in range(1,num+1):
    for j in range (1,k+1):
        print("*",end=" ")
    k = k + 2           # to print symbol in isosceles triangle
    print()
    