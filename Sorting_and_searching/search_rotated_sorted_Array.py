def search(nums, target):
	n = len(nums)
	low = 0 
	high = n-1
	while(low<=high):
		mid = (low+high)//2

		if(nums[mid] == target):
			return mid
	#if the starting index of the search space has smaller element than current element
		elif(nums[low]<=nums[mid]):
			## if target lies in non-rotated search space (or subarray)
			if(target >= nums[low] and target < nums[mid]):
				high = mid - 1
			else:
				low = mid + 1
		else:
			##if target lies in non-rotated subarray
			if(target>nums[mid] and target<=nums[high]):
				low = mid + 1
			else:
				high = mid - 1
        
    #if you couldn't find the target element until now then it does not exists
	return -1;
	
## Driver code...!!!!
if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    ele = int(input())
    print('index_of_search_element-->',search(arr,ele))