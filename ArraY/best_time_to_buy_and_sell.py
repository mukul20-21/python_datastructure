## simple store first element and traverse remaining array and find the maximum diffrence....
def max_profit(prices):
    mx = 0
    mini = prices[0]
    for i in range(1,len(prices)):
        if prices[i] < mini:
            mini = prices[i]
        else:
            mx = max(mx,prices[i]-mini)

    return mx

## Driver code...!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print("maximum profit",max_profit(arr))
