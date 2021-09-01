def foursum(arr,target):
	res = []
	if arr == None or len(arr) == 0:
		return res
	n = len(arr)
	arr.sort()
	
	for i in range(n):
		for j in range(i+1,n):
			target2 = target - arr[j] - arr[i]
			
			front = j+1
			back = n-1
			while front<back:
				two_sum = arr[front] + arr[back]
				if two_sum< target2:
					front+=1
				elif two_sum>target2:
					back -= 1
				else:
					temp = []
					temp.append(arr[i])
					temp.append(arr[j])
					temp.append(arr[front])
					temp.append(arr[back])
					temp.append("$")
					res.append(temp)
				
				## skip duplicate of number3
					while(front < back and arr[front] == temp[2]):
						front +=1
				## skip duplicate of number4
					while (front < back and arr[back] == temp[3]):
						back -=1
		
			## skip number2 from j loop if duplicate...!!!
			while(j+1 < n and arr[j+1] == arr[j]):
				j +=1
		## skip number1 for i loop if duplicate...!!!
		while (i+1<n and arr[i+1] == arr[i]):
			i += 1
	
	return res

## Driver code..!!!!
if __name__ == "__main__":
	target = int(input())
	arr = list(map(int,input().split()))
	print(foursum(arr,target))


'''
sample input
3
0 0 2 1 1
'''