def printFirstNegativeInteger( A, N, K):
    # code here
    ans = []
    l = []
    i =  0
    j = 0
    
    while j<N:
        if (A[j]<0):
            l.append(A[j])
        
        if j-i+1 < K:
            j +=1
        elif j-i+1 == K:
            if len(l) == 0:
                ans.append(0)
                i+=1
                j+=1
            else:
                ans.append(l[0])
                if (A[i] == l[0]):
                    l.pop(0)
                i+=1
                j+=1
        
    return ans

## Driver code...!!!!
if __name__ == "__name__":
	arr = list(map(int,input().split()))
	K,N = list(map(int,input().split()))
	# k --> window size
	# N --> no.of element
	print(printFirstNegativeInteger( A, N, K))

'''
sample input
-8 2 3 -6 10
2 5
'''