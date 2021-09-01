num = int(input("Enter the number to check if it palindromic_prime number:"))
reverse_num = int(str(num)[::-1])
if num == reverse_num:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print("It is not a prime number but it is palindromic")
                break
        else:
            print("Enter num is palindromic_prime:",num)
else:
    if num>1:
        for i in range(2,num):
            if(num%i) ==0:
                print("It is palindromic but not a prime number")
                break
        else:
            print("It is prime number but not palindromic number.")