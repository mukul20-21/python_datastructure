## Method1 --> using count array..
# utility function...!!!!
def fillcountarray(count:list,string):
    for i in string:
        count[ord(i)] +=1
    return count

## main function check count of duplicate element...
def duplicate(string):

    count = [0] * 256
    count = fillcountarray(count,string)

    k = 0
    for i in count:
        if int(i) > 1:
            print(chr(k) ,',count using count array-->',str(i))   ## chr() function convert ascci code into alphabets..
        k+=1


'''
Drawback -->  Space Complexity is potentially high for such cases.
            So, to avoid any discrepancies and to improve Space Complexity, maps are generally preferred over long-sized arrays.
'''
'''
Method 2: Using Maps

Approach: The approach is the same as discussed in Method 1, but, using a map to store the count. time --> O(1) using get function..
                                                                                                    --> O(N) use in operator to check.

'''
def duplicate_dict(strr):
    m = {}
    for i in strr:
        m[i] = m.get(i,0) + 1

    for i in m:
        if m[i] > 1:
            print(i ,',count using hashmap-->',m[i])

## Driver code...!!!!
if __name__ == "__main__":
    s = input()
    duplicate_dict(s)
    duplicate(s)
