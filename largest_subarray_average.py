def largest_subarray_average(arr, k):
    if not arr:
        return None
    if k <= 0:
        raise ValueError("k must be greater than 0")
    
    if len(arr) < k:
        raise ValueError("k cannot be larger than array length")
    
    max_av = sum(arr[0:k])/k

    for i in range(1, len(arr)-k+1):
        av = sum(arr[i:i+k])/k
        max_av = max(max_av, av)
    return max_av

def largest_subarray_average_optimised(arr, k):
    if not arr:
        return None
    if k <= 0:
        raise ValueError("k must be positive")
    if len(arr) < k:
        raise ValueError("length of your arr must be at least as large as k")
    
    cum_sum = sum(arr[:k])
    current_max = cum_sum

    for i in range(1, len(arr)-k+1):
        cum_sum = cum_sum + arr[i+k-1]-arr[i-1]
        current_max = max(cum_sum, current_max)
    
    return current_max/k

if __name__ == "__main__":
    # Each test: (array, k, expected_average)
    tests = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),           # [12, -5, -6, 50]
        ([1, 12, -5, -6, 50, 3], 1, 50.0),            # [50]
        ([1, 12, -5, -6, 50, 3], 2, 26.5),            # [50, 3]
        ([1, 12, -5, -6, 50, 3], 3, 15.666666666667), # [-6,50,3]
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 2, 1.5),    # [2,1]
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 3, 1.666666666667), # [4,-1,2]
        ([-8, -3, -6, -2, -5, -4], 2, -3.5),
        ([-8, -3, -6, -2, -5, -4], 3, -3.666666666667),
        ([2, 3, 5, 8, 13, 21], 2, 17.0),             # [13,21]
        ([2, 3, 5, 8, 13, 21], 3, 14.0),             # [8,13,21]
        ([5], 1, 5.0),
    ]

    for arr, k, expected in tests:
        result = largest_subarray_average(arr, k)
        print(f"arr={arr}, k={k} -> result={result:.6f}, expected≈{expected:.6f}")
