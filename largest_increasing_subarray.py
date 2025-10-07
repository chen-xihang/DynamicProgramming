def largest_increasing_subsequence(arr):
    if not arr:
        return []

    n = len(arr)                   # <- fix: do NOT add +1
    max_length = [[] for _ in range(n)]

    for i in range(n):
        best_len = 0
        best_idx = -1
        for j in range(i):        # j = 0..i-1, safe for indexing arr[j]
            if arr[i] > arr[j]:
                if len(max_length[j]) > best_len:
                    best_len = len(max_length[j])
                    best_idx = j

        if best_idx == -1:
            max_length[i] = [arr[i]]
        else:
            # extend the subsequence that ends at best_idx
            max_length[i] = max_length[best_idx] + [arr[i]]

    # pick and return the longest subsequence (ties broken arbitrarily)
    return max(max_length, key=len)


# Example usage:
arr = [1, 2, 3, 2, 7, 5, 6]
largest_increasing_subsequence(arr) # Output: [1,2,3,5,6]

arr = []
largest_increasing_subsequence(arr)  # Output: []

