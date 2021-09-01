## For spiral traversal follow some basic genric code to get spiral matrix..
'''
        left      right
         :        :
top--  [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
bottom- [13, 14, 15, 16]]

## Before starting implementation initialization of some pointers... and also initialise direction...
## how to approach the question...

    -- 1 2 3 4      :: direction = 0 ;left to right index
    -- 8 12 16      :: direction = 1 ;right to bottom index
    -- 15 14 13     :: direction = 2 ;right to left index
    -- 13 9         :: direction = 3 ;bottom to left index

## jst iterate in every direction using for loop and a while loop..
    if d == 0:
        --iterate in 1st direction
        update top pointer
    elif d == 1:
        --iterate in 2nd direction
        update right pointer
    elif d == 2:
        --iterate in 3rd direction
        update bottom pointer
    elif d == 3:
        --iterate in 4th direction
        update left pointer

## Note--> Example if we traverse in one particular direction then,
            used one fix pointer for the particular row/column and,
            iterate over printing item using remaining two pointer of that row/column
'''
## A brief introduction for spiral matrix implementation...
def print_spiral(matrix):
    
    row = len(matrix)
    col = len(matrix[0])
    if row == 0:
        return matrix
    ## initialize some pointers..
    left = 0
    top = 0
    right = col-1
    bottom = row-1
    d = 0
    res = []

    while left<=right and top<=bottom:          ## Keep track of fixed element and it's updation..
        if (d==0):
            for i in range(left,right+1):
                res.append(matrix[top][i])
            d=1
            top+=1
        elif (d==1):
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            d=2
            right-=1
        elif(d==2):
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
            d=3
        elif(d==3):
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            d=0
    return res

## Driver code...!!!!
