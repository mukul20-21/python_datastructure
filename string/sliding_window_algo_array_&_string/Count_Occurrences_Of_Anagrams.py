# This function returns true if contents of arr1[] and arr2[] are same, otherwise false. 
def compare(arr1, arr2): 
	MAX=256
	for i in range(MAX): 
		if arr1[i] != arr2[i]: 
			return False
	return True
		
# This function search for all permutations of pat[] in txt[] 
def search(pat, txt): 
	MAX=256
	M = len(pat) 
	N = len(txt) 

	# countP[]: Store count of all characters of pattern..
	#countTW[]: Store count of current window of text 
	countP = [0]*MAX
	countTW = [0]*MAX

	for i in range(M): 
		(countP[ord(pat[i]) ]) += 1
		(countTW[ord(txt[i]) ]) += 1
	ans=0
	# Traverse through remaining characters of pattern 
	for i in range(M,N): 
	# Compare counts of current window of text with counts of pattern[] 
		if compare(countP, countTW): 
			ans+=1;

		# Add current character to current window 
		(countTW[ ord(txt[i])]) += 1
		# Remove the first character of previous window 
		(countTW[ ord(txt[i-M])]) -= 1
		
		# Check for the last window in text	 
	if compare(countP, countTW): 
		ans+=1
	return ans

## Driver code...!!!!
if __name__ == "__main__":
	txt = input()
	pat = input()
	print("total no of anagram present",search(pat, txt))

'''
sample input..
forxxorfxdofr
for
o/p -- 3
'''