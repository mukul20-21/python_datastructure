''' here the program split into three part : 1st find pivot value,
2nd : after get pivot rearrange the list by divide into sublist
3rd: main function callable..'''

def  pivot_place(list1,first,last):             # this function get variables first & last is index value of list1 which is passed
    pivot= list1[first]                                 # assume first element at index first is our initial pivot..
    left = first+1
    right = last                                        # both left & right variable use to get correct index position for pivot.
    
    while True:
        while left <= right and list1[first]<= pivot:
            left = left+1
        while left<=right and list1[right]>=pivot:
            right = right -1
        if right < left:
            break                                           # here the last condition which all condition get false swap right index value with pivot value because we take first element as our assume pivot..
        else:                                                   # if above both while get false then swap left index value with right index value..
            list1[left] , list1[right] = list1[right] , list1[left]
    
    list1[first] , list1[right] = list1[right] , list1[first]               
    return right                                        # get correct index value for pivot element..

def quicksort(list1,first,last):                    # this function do not return anything because we only rearange the list with the help of pivot value..
    if first<last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)                      # here the recursive call of function again & again.. first and last variable plays a major role here..
        quicksort(list1,p+1,last)
       
# main
list1 = [77,44,11,2,88]
n = len(list1)

quicksort(list1,0,n-1)
print("sorted_list:",list1)        