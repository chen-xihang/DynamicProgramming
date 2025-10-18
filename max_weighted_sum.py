def max_weighted_sum(arr):
    if not arr:
        return 0
    n = len(arr)
    if n == 1:
        return arr[0] * 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = arr[0] * 1  # first element at position 0 gets weight 1
    
    for i in range(2, n + 1):
        # i represents considering first i elements (indices 0..i-1)
        # No swap at position i-2, i-1
        no_swap = dp[i-1] + arr[i-1] * i
        
        # Swap at position i-2, i-1
        swap = dp[i-2] + arr[i-1] * (i-1) + arr[i-2] * i
        
        dp[i] = max(no_swap, swap)
    
    return dp[n]

# Test
arr = [1, 3, 2]
print(max_weighted_sum(arr))  # Should output 14

    