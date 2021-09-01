## solution take O(N) time and O(1) space...!!!
def find_miss_and_repeating(arr,N):
	a = 0
	b = 0
	res = []
	for i in range(N):
		if arr[abs(arr[i]-1)] < 0:
			a = abs(arr[i])
			res.append(a)
		else:
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
	
	for i in range(N):
		if arr[i]>0:
			b = i+1
			res.append(b)
	
	return res



## Driver code...!!!!
if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	print("repeating and missing element is---",find_miss_and_repeating(arr,N))