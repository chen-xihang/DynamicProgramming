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

# O(n^2) using dynamic programming
def largest_subarray_sum_0(arr):
    if not arr:
        return []
    n = len(arr)
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = arr[0]
    start_index = -1
    end_index = -1
    length = end_index-start_index 
    for i in range(2, n+1):
        dp[i] = dp[i-1] + arr[i-1]
        for j in range(i):
            if dp[i] == dp[j] and (i-j>length):
                start_index = j
                end_index = i
                length = max(length, i-j)
    return arr[start_index:end_index]

# O(n) using Hashmap
def largest_subarray_sum_0_optimised(arr):
    if not arr:
        return []
    hashmap = {0:-1}
    prefix_sum = 0
    max_length = 0
    best_start = -1
    best_end = -1
    for i, n in enumerate(arr):
        prefix_sum = prefix_sum + n
        if prefix_sum in hashmap:
            current_length = i-hashmap[prefix_sum]
            if current_length > max_length:
                max_length = current_length
                best_start = hashmap[prefix_sum]
                best_end = i
        else:
            hashmap[prefix_sum] = i
    return arr[best_start+1:best_end+1]

largest_subarray_sum_0_optimised([-1,1,-1,1, 0, 0, 2])


tests = [
    {"arr": [1, -1], "expected": [1, -1], "reason": "whole array sums to 0"},
    {"arr": [1, 2, -3, 3], "expected": [1, 2, -3], "reason": "middle section sums to 0"},
    {"arr": [15, -2, 2, -8, 1, 7, 10, 23], "expected": [-2, 2, -8, 1, 7], "reason": "classic example"},
    {"arr": [1, 2, 3], "expected": [], "reason": "no zero-sum subarray"},
    {"arr": [4, -1, -3], "expected": [4, -1, -3], "reason": "whole array sums to 0"},
    {"arr": [], "expected": [], "reason": "empty input"},
    {"arr": [0, 0, 0, 0], "expected": [0, 0, 0, 0], "reason": "all zeros → full array"},
    {"arr": [3, -3, 2, 1], "expected": [-3, 2, 1], "reason": "longest zero-sum subarray is [-3,2,1] (length 3)"},
    {"arr": [2, 1, -3], "expected": [2, 1, -3], "reason": "whole array sums to 0"},
    {"arr": [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7],
     "expected": [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7],
     "reason": "entire array sums to 0 (longest)"},
]


if __name__ == "__main__":
    for i, t in enumerate(tests, 1):
        arr = t["arr"]
        expected = t["expected"]
        result = largest_subarray_sum_0(arr)
        status = "✅" if result == expected else "❌"
        print(f"Test {i}: {status}")
        print(f"  Input:     {arr}")
        print(f"  Expected:  {expected}")
        print(f"  Got:       {result}")
        print(f"  Reason:    {t['reason']}\n")

from bisect import bisect_left

# Basically creating a hashmap where the key is the prefix_sum and the value is the indices 
# Find global maximal
# Then compute lst[-1]-lst[0]
def all_max_zero_sum_subarrays(arr):
    # 1) Build list of indices for each prefix sum using hashmap (for speed)
    prefix_index_lists = {}          # prefix_sum -> list of indices
    prefix_sum = 0
    prefix_index_lists = {0: [-1]}  # prefix sum 0 at "index -1"
    for i, v in enumerate(arr):
        prefix_sum += v
        prefix_index_lists.setdefault(prefix_sum, []).append(i) #if prefix_sum is already in prefix_index_lists then append to it if not create an empty list and then append to it

    # 2) Compute global max_length 
    max_length = 0
    for lst in prefix_index_lists.values():
        if len(lst) >= 2:
            length = lst[-1] - lst[0]   # latest - earliest
            if length > max_length:
                max_length = length

    # 3) Collect all pairs of indices (i, j) with j - i == max_length
    results = []
    if max_length == 0:
        return []
    
    for lst in prefix_index_lists.values():
        if len(lst) >= 2 and (lst[-1] - lst[0] == max_length):
            start = lst[0] + 1
            end = lst[-1]
            results.append((start, end, arr[start:end+1]))

    return results
