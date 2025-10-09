def largest_subarray_sum(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [float('-inf')] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    return max(dp)

def largest_subarray_sum_optimised(arr):
    if not arr:
        return 0
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:        
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(largest_subarray_sum(arr))  # Output: 6
    print(largest_subarray_sum_optimised(arr))  # Output: 6
    arr = [1]
    print(largest_subarray_sum(arr))  # Output: 1
    print(largest_subarray_sum_optimised(arr)) # Output: 1
    arr = [5,4,-1,7,8]
    print(largest_subarray_sum(arr))  # Output: 23
    print(largest_subarray_sum_optimised(arr))  # Output: 23
# This function finds the largest sum of a contiguous subarray using dynamic programming.   