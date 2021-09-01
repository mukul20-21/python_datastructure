def fun(n):
    if n%10 ==0:
        return 0
    else:
        return fun(n//10) + n%10





## main function execution...!!!!!

if  __name__ == "__main__":
    
   # n = int(input("Enter no. of recursion ..."))
    print(fun(987))