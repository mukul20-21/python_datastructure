def primefact(N):
    i = 2
    while (i*i <= N):
        if N %i == 0:
            cnt = 0
            while (N % i == 0):
                cnt +=1
                N = N//i
            print(i ,'^',cnt)
        i+=1

    if N > 1:
        print(i,'^',1)

## Driver code..!!!
if __name__ == "__main__":
    N = int(input('Enter number--'))
    primefact(N)
