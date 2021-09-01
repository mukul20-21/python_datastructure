'''
## Approach..
    step1 -- find the search space by taking low == mimimum value in array and high == sum of whole array..
    step2 -- find the middle using that low and high value and treat mid as a assume barrier for minimum allocation--
            A.. if mid barrier not fullfil the total no.of student book requirement then we jst increase the value of low = mid+1
            B.. if its satisfied the count of student allocate count within the range but reduce the value to find the minimum from maximum value..
    
    ** here we use binary function and for execute step2 we just create a another func for above functionality..

'''
## utility function..!!!
#n--> no. of books..
#m --> no. of student..
#curr_min --> store current value of minimum pages..

def isvalid(arr, n, m, curr_min):
    studentsRequired = 1
    curr_sum = 0
     # iterate over all books
    for i in range(n):
        if (curr_min < arr[i]):         # corner case..
            return False
 
        if (curr_min < curr_sum + arr[i]):
            studentsRequired += 1
            curr_sum = arr[i]
            if (studentsRequired > m):
                return False
        else:
            curr_sum += arr[i]
    return True
    
#Function to find minimum number of pages.
def findPages(arr, m):
    n = len(arr)
    summ = 0
    if (n < m):
        return -1
    # Count total number of pages
    for i in range(n):
        summ += arr[i]
        
    start = 0
    end = summ
    result = 10**9
 
    # traverse until start <= end
    while (start <= end):
        # check if it is possible to distribute books by using mid as current minimum
        mid = (start + end) // 2
        if (isvalid(arr, n, m, mid)):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
 
    # at-last return minimum no. of pages
    return result
 
    
    
## Driver code..!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    stud = int(input())
    
    print('minimum no of pages maximum pages..!!!',findPages(arr,stud))

'''
sample input...
12 34 67 90
2
'''