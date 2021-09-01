## for linear time complexity use hashmap with sliding window concept...
def longestUniqueSubsttr(string):
       
	last_idx = {}
	max_len = 0
 
	# starting index of current window to calculate max_len
	start_idx = 0
 	for i in range(0, len(string)):
   		# Find the last index of str[i] Update start_idx (starting index of current window) as maximum of current value of start_idx and lastindex plus 1
		if string[i] in last_idx:
			start_idx = max(start_idx, last_idx[string[i]] + 1)
		# Update result if we get a larger window
		max_len = max(max_len, i-start_idx + 1)
 		# Update last index of current char.
		last_idx[string[i]] = i
 
	return max_len

## Driver code...!!!!!
if __name__ == "__main__":
	Str = input()
	print("length of largest substring",longestUniqueSubsttr(string))
	
'''
sample input...
geeksforgeeks
'''
	