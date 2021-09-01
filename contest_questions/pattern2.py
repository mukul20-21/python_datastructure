"""Here the main logic behind the pyramid is looping statement:
    1st loop: print the number of rows.
    2nd loop: number of spaces.
    3rd loop: print the symbol..    """


num = int(input("Enter number of rows:"))

for i in range(0,num):              # this code print straigth pyramid...!!
    for j in range(0,num-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")          
    print()                          
    
for i in range(num,0,-1):           # this code print upside-down pyramid...!!
    for j in range(0,num-i):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()