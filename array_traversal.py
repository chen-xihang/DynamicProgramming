def array_traversal(arr):
    if not arr:
        return -1
    
    n = len(arr)

    if n == 1:
        return 0
    
    dp = [float('inf')] * n 
    dp[-1] = 0 # dp[n-1] = 0
    for i in range(n-2, -1, -1):
        if arr[i] == 0:
            dp[i] = float('inf')
        else:
            min_i = float('inf')
            for j in range(i+1, min(i+arr[i]+1, n)):
                min_i = min(min_i, dp[j])
            dp[i] = 1 + min_i
    return dp[0] if dp[0] != float('inf') else -1

array_traversal([0])

class JumpGameTests:
    def __init__(self):
        self.test_cases = [
            # (input array, expected result)
            ([2, 3, 1, 1, 4], 2),       # normal case
            ([0], 0),                   # single element
            ([1, 0], 1),                # one jump
            ([3, 2, 1, 0, 4], -1),  # stuck (unreachable)
            ([2, 0, 2, 0, 1], 2),       # zeros but reachable
            ([1, 1, 1, 1, 1], 4),       # linear movement
            ([10, 1, 1, 1, 1], 1),      # large jump at start
            ([1, 3, 5, 1, 1, 1, 1], 3), # multiple options
            ([0, 1, 2, 3], -1) # zero at start (unreachable)
        ]

    def run_tests(self, func):
        for i, (arr, expected) in enumerate(self.test_cases, 1):
            result = func(arr)
            print(f"Test {i}: arr = {arr}")
            print(f"Expected: {expected}, Got: {result}")
            print("✅ PASS\n" if result == expected else "❌ FAIL\n")

tests = JumpGameTests()
tests.run_tests(array_traversal)