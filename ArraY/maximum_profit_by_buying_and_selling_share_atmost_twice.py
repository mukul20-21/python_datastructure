method1 --> O(N) time simple approach...

def maxProfit(arr, n):
    profit = [0]*n
    # Get the maximum profit
    # with only one transaction allowed. After this loop,
    #profit[i] contains maximum profit from price[i..n-1] using at most one trans.
    max_price = arr[n-1]

    for i in range(n-2, 0, -1):
        if arr[i] > max_price:
            max_price = arr[i]

        # we can get profit[i] by
        # taking maximum of:
        # a) previous maximum,i.e., profit[i+1]
        # b) profit by buying at price[i] and selling at max_price
        profit[i] = max(profit[i+1], max_price - arr[i])

    # Get the maximum profit with two transactions allowed
    # After this loop, profit[n-1] contains the result
    min_price = arr[0]

    for i in range(1, n):

        if arr[i] < min_price:
            min_price = arr[i]
        # Maximum profit is maximum of:
        # a) previous maximum,i.e., profit[i-1]
        # b) (Buy, Sell) at (min_price, A[i]) and add profit of other trans.stored in profit[i]
        profit[i] = max(profit[i-1], profit[i]+(arr[i]-min_price))

    result = profit[n-1]

    return result
