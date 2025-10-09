def water_drop(arr):
    if not arr:
        return 0 
    n = len(arr)

    left_max = [0]*n #left_max[i] is the maximum from 0 to i
    right_max = [0]*n #right_max[i] is the maximum from i to n-1
    
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])

    right_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])

    water = 0

    for i in range(1, n-1, 1):
        water = water + max(min(left_max[i-1], right_max[i+1]) - arr[i], 0)

    return water

# tests
if __name__ == "__main__":
    tests = [
        ([], 0),                          # empty input
        ([5], 0),                         # single bar
        ([2, 2], 0),                      # two equal bars
        ([0, 0, 0, 0], 0),                # all zero
        ([1, 2, 3, 4, 5], 0),             # increasing
        ([5, 4, 3, 2, 1], 0),             # decreasing
        ([2, 0, 2], 2),                   # simple valley
        ([3, 0, 0, 2, 0, 4], 10),         # multiple valleys
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # classic case
        ([4, 2, 0, 3, 2, 5], 9),          # common example
        ([3, 3, 3, 3, 3], 0),             # flat plateau
        ([0, 5, 0, 0, 5, 0], 10),         # big walls
        ([0, 2, 0, 2, 0, 2, 0], 4),       # repeating valleys
        ([10, 0, 0, 0, 10], 30),          # deep pit
        ([1000] + [0]*10 + [1000], 1000*10)  # large-scale check
    ]

    for arr, expected in tests:
        result = water_drop(arr)
        print(f"{arr} → {result} (expected {expected}) {'✅' if result == expected else '❌'}")