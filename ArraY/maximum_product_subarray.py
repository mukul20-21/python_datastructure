## similar as maximum subarray sum(kadane_algo).. with some variation...
## Yeah question firr se krna hai ek baar abhi smjh nhi aa rha hai....
def maxProduct(nums):
    # code here
    max_overall = nums[0]
    max_ending_here, min_ending_here = nums[0], nums[0]

    for i in range(1, len(nums)):
        tmp = max_ending_here
        max_ending_here = max({nums[i], nums[i]*max_ending_here, nums[i]*min_ending_here})
        min_ending_here = min({nums[i], nums[i]*tmp, nums[i]*min_ending_here})
        max_overall = max(max_overall, max_ending_here)

    return max_overall

## Driver code...!!!
    arr = list(map(int,input().split()))

'''
sample input..
6 -3 -10 0 2
'''
