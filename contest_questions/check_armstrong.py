# program sovled in function manure..
num = int(input("Enter the number would you check is it armstrong or not...!!:"))
def armstrong(num):
    num = i
    result =0
    n = len(str(num))
    while(i!=0):
        digit = i%10                        # written last digit of the number
        result = result + digit**n
        i = i//10                           # truncate operation return integer values  
        if result == num:
            print("Number is armstrong:",result)
        else:
            print("not a armstrong")
           