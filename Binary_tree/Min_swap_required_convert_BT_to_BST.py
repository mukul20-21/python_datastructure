def inorder(a, n, index):
    global v
    if (index >= n):
        return
     
    inorder(a, n, 2 * index + 1)
 # Push elements in vector
    v.append(a[index])
    inorder(a, n, 2 * index + 2)
 
# Function to find minimum swap to sort an array
## basically create a nested list which store value and index of element
def minSwaps():
     
    global v
    t = [[0, 0] for i in range(len(v))]
    ans = -2
    ## store element using nested list consist[value,index] together...
    for i in range(len(v)):
        t[i][0], t[i][1] = v[i], i
 
    t = sorted(t)
    i = 0
    while i < len(t):
         ## now we swap based on index value
        # second element is equal to i
        if (i == t[i][1]):
            i += 1
            continue
        else:
             
            # Swaping of elements
            t[i][0], t[t[i][1]][0] = t[t[i][1]][0], t[i][0]
            t[i][1], t[t[i][1]][1] = t[t[i][1]][1], t[i][1]
 
        # Second is not equal to i
        if (i == t[i][1]):
            i -= 1
 
        i += 1
 
        ans += 1
 
    return ans
 
# Driver Code
if __name__ == '__main__':
     
    v = []
    a = [ 5, 6, 7, 8, 9, 10, 11 ]
    n = len(a)
    inorder(a, n, 0)
 
    print(minSwaps())