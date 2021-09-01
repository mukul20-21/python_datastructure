# print all negative element at the end of the list/array...!!!!!!

def  segregatelement(arr,n):
    temp = [0 for k in range(n)] # store all elements..!!!!
    
     # Traversal array and store +ve element in 
    # temp array 
    j = 0
    for i in range(n):
        if  (arr[i]>=0):
            temp[j] = arr[i]
            j +=1
            
    # if traversal consist only positive or negative number..!!!
    if (j == n or j == 0):
        return
    
    # Store -ve element in temp array 
    for i in range(n): 
        if (arr[i] < 0): 
            temp[j] = arr[i] 
            j +=1
    
    # Copy contents of temp[] to arr[] 
    for k in range(n): 
        arr[k] = temp[k] 
    return(arr)
    
T = int(input('No. of test cases..'))
while (T > 0):
    n = int(input('no of element in array:'))
    a = list(map(int,input("enter element one by one..!!").strip().split()))[:n]
    segregatelement(a,n)
    print(*a)
    
    T -= 1
    
   
if __name__ == "__main__":
    main()