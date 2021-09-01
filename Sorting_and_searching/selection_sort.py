# Complete selection sort function implement with or without min() and index() function


def selectionsort(list1):                           # function with both min and index function
    for i in range(len(list1)-1):
        m_val = min(list1[i:])
        m_ind = list1.index(m_val,i)
        if list1[i] != list1[m_ind]:                            # make efficient for loop condition
            list1[i],list1[m_ind] = list1[m_ind],list1[i]          # here the element swap by its minimum value in input list

    return list1
    
def selection_without_min(list1):
    for i in range(len(list1)-1):
        m_val = list1[i]                            # here we assume that our 1st element is smallest..
        for j in range(i+1,len(list1)):              # for loop replace the min function
            if list1[j]<m_val:
                m_val = list1[j]
        
        m_ind = list1.index(m_val,i)
        if list1[i] != list1[m_val]:
            list1[i],list1[m_ind] = list1[m_ind],list1[i] 
    return list1

def selection_without_min_index(list1):
    for i in range(len(list1)-1):
        m_ind = i         # here we assume 1st element as a index value
        for j in range(i+1,len(list1)):
            if list1[j] < list1[m_ind]:
                m_ind = j
        
        if list1[i] != list1[m_ind]:
            list1[i],list1[m_ind] = list1[m_ind],list1[i]
    return list1


if __name__ == "__main__":

    num = int(input("enter the number would you wantt enter in list:"))
    list1 = list(map(int,input("Enter the element in array").strip().split()))[:num]
    print("your unorder {list1} with {num} element".format(list1=list1,num=num))
    result=selectionsort(list1)
    print("sorted list:",result)