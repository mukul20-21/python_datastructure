T = int(input())

def lists_equal(a, b):
    if len(a)!=len(b):
        return False
    for i, j in zip(a, b):
        if i!=j:
            return False
    return True
    

def is_mirror(pairsA, pairsB):
    graphA = defaultdict(list)
    graphB = defaultdict(list)
    
    queueA = deque(pairsA)
    queueB = deque(pairsB)
    
    while(queueA):
        u = queueA.popleft()
        v = queueA.popleft()
        
        graphA[u].append(v)
        
    while(queueB):
        u = queueB.popleft()
        v = queueB.popleft()
        
        graphB[u].append(v)

    for k in graphA:
        a = graphA[k]
        b = graphB[k]
        
        a.reverse()
        if  not lists_equal(a, b):
            return 0
    return 1
    
        

for _ in range(T):
    N , E = input().split()
    pairsA = list(map(int, input().split()))
    pairsB = list(map(int, input().split()))
    print(is_mirror(pairsA, pairsB))
    
    