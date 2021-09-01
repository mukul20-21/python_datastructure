def longestKSubstr(s, k):
        # code here
    m = dict()
    mx = 0
    i = 0
    j = 0
    
    while j<len(s):
        if len(m)<k:
            if s[j] in m:
                m[s[j]] = m[s[j]]+1
            else:
                m[s[j]] = 1
            j+=1
            
        elif len(m) == k:
            mx = max(mx,j-i+1)
            if s[j] in m:
                m[s[j]] = m[s[j]]+1
            else:
                m[s[j]] = 1
            j+=1
            
        elif len(m) >k:
            while len(m)>k:
                if s[i] in m:
                    m[s[i]] = m[s[i]]-1
                    if m[s[i]] == 0:
                        m.pop(s[i])
                i+=1
            j+=1
    return mx
    
## Driver code...!!!!
if __name__ == "__main__":
    strr = input()
    K = int(input())
    print(longestKSubstr(strr, K))
'''
sample input...
aabacbebebe
3