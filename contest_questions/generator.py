
def fib(mymax):
    a,b = 0,1
    while True:
        c = a+b
        if c < mymax:
            print("Before yield function calling..!!")
            yield c
            print("After yield function calling..!!")
            a=b
            b=c 
        else:
            break