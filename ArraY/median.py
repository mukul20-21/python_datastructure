'''
In case of even number of
elemebts average of two middle elements
is the median
'''
def find_median(V):

	V.sort()
	ans = 0
	s = len(V)
	if(len(V)%2==1):
		ans = v[s // 2];
	else:
		ans = (V[s // 2] + v[(s//2) - 1]) // 2
	return ans

## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
