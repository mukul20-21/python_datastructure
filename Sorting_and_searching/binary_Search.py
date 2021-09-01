def iter_binary_search(arr,ele):
	start = 0
	end = 0
	end = len(arr)-1
	while start<=end:
		mid = (start + end)//2
		if ele == arr[mid]:
			return mid
		elif ele < arr[mid]:
			end = mid-1
		else:
			start = mid+1
	return -1

def recur_binary_search(arr,ele):
	pass

## Driver code..!!!!
if __name__ == "__main__":
	arr = []
	ele = 
	