## solution take O(log(n)+log(m)) time and O(1) space...

def findMedianSortedArrays(nums1,nums2):
	if(len(nums2) < len(nums1)):
		return findMedianSortedArrays(nums2, nums1)
	n1 = len(nums1)
	n2 = len(nums2)
	low = 0
	high = n1
	INT_MIN = -9999999
	INT_MAX = 9999999

	while(low <= high):
		cut1 = (low+high) // 1
		cut2 = (n1 + n2 + 1) // 2 - cut1
		## Cover corner cases...
		if cut1 == 0:
			left1 = INT_MIN
		else:
			left1 = nums1[cut1-1]

		if cut2 == 0:
			left2 = INT_MIN
		else:
			left2 = nums2[cut2-1]

		if cut1 == n1:
			right1 = INT_MAX
		else:
			right1 = nums1[cut1]

		if cut2 == n2:
			right2 = INT_MAX
		else:
			right2 = nums2[cut2]


		if(left1 <= right2 and left2 <= right1):
			if( (n1 + n2) % 2 == 0 ):
				return (max(left1, left2) + min(right1, right2)) / 2 # if length is even
			else:
				return max(left1, left2) # if lengthid odd

		elif(left1 > right2):
			high = cut1 - 1

		else:
			low = cut1 + 1



## Driver code...!!!!!
if __name__ == "__main__":
	arr1 = list(map(int,input().split()))
	arr2 = list(map(int,input().split()))
	print("median of two sorted array",findMedianSortedArrays(arr1,arr2))

"""
sample input--
1. EVEN length
1 3 4 7 10 12
2 3 6 9
o/p - 5
...
2. ODD length
1 3 4 7 10 12 16
2 3 6 9
o/p - 6
"""
