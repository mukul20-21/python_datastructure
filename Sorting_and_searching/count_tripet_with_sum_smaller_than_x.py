## sorting + two pointer approach to find sum under one loop..
def counttriplet(arr,n,target):
	res = []
	arr.sort()
	count = 0
	for i in range(n-2):
		start = i+1
		end = n-1
		while start<=end:
			if arr[i]+arr[start]+arr[end] < target:
				count += end-start
				temp = []
				temp.append(arr[i])
				temp.append(arr[start])
				temp.append(arr[end])
				res.append(temp)
				start +=1
			else:
				end -=1
	return res,count


## Driver code...!!!
if __name__ == "__main__":
	n,target = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	print("count no of triplet smaller than given element",counttriplet(arr,n,target))

'''
sample input...
4 2
-2 0 1 3
'''