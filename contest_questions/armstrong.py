# program sovled in iterative manure..

for i in range(0,1001):
    num = i
    result =0
    n = len(str(num))
    while(i!=0):
        digit = i%10                        # written last digit of the number
        result = result + digit**n
        i = i//10                           # truncate operation return integer values  
        if result == num:
            print(result)
           