t = int(input())
while t>0:
    num = int(input())
    list1 = list(map(int,input().strip().split()))[:num]
    print("Unsorted list:",list1)
    for j in range(len(list1)-1):
        for i in range(len(list1)-1-j):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]
    print("Sorted list:",list1)