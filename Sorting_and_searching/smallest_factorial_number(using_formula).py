## avoid factorial jst find the count of 5's for a number range between low and high...
def check(prime,n):
    temp = prime
    count = 0 
    f = 5
    while f<=temp:
        count+=temp//f
        f = f*5
    return (count >= n)


def findNum(n):
	if n ==1:
		return 5
	low = 0				## initial the search space..
	high = 5*n
	while (low<high):
		mid = (low+high)>>1
		if (check(mid,n)== True):
			high = mid
		else:
			low = mid+1
	return low

## Driver function...
if __name__ == "__main__":
	n = int(input())
	print("prime number for trailing zeroes is-->",findNum(n))