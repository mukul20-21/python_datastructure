# find the common element in the 3 sorted arrays:

t = int(input())

while t>0:
    
    n1,n2,n3 = map(int,input().strip().split())
    matrix = []
    for i in range(3):
        row = list(map(int,input().strip().split()))
        matrix.append(row)
    
    dupl = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i].count(j) > 2:
                dupl.add(j)
    
    print(dupl)
    
    t = t-1