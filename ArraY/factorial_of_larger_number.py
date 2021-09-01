## update number:list in every function call
## append value at the end at last jst reverse the list before printing..
def multiply(n,number):
    carry = 0
    for i in range(len(number)):
        num = n * number[i]
        number[i] = (num + carry) % 10
        carry = (num + carry) // 10

    while carry:
        number.append(carry % 10)
        carry = carry // 10

## main function....
def factorial(N):
    number = []
    number.append(1)
    for i in range(2,N+1):
        multiply(i, number)
    return number[::-1]

## Driver code...!!!!
if __name__ == "__main__":
    N = int(input())
    print(*factorial(N))
