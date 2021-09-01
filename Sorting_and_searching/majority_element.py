## Moore Voting Algorithm...!!!
def findcandidate(arr):
	ele = 0
	cnt = 1
	for i in range(len(arr)):
		if arr[ele] == arr[i]:
			cnt +=1
		else:
			cnt -=1
		if cnt == 0:
			ele = i
			cnt = 1
	return arr[ele]

def ismajority(arr,cand):
	cnt = 0
	for i in range(len(arr)):
		if arr[i] == cand:
			cnt += 1
	if cnt>len(arr)//2:
		return True
	else:
		return False

def majority_element(arr,N):
	cand = findcandidate(arr)
	
	if ismajority(arr,cand) == True:
		return cand
	else:
		return -1

## Driver code...!!!
if __name__ == "__main__":
	arr = list(map(int,input().split()))
	N = int(input())
	print("majority element in array-->",majority_element(arr,N))

"""
sample input...
2 3 3 3 3 4 2 1
7
"""
	