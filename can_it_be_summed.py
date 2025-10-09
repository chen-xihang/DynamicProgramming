def can_it_be_summed(arr, k): 
    if not arr and k == 0:
        return True
    
    if not arr and k >0:
        return False
    
    if k == 0:
        return True

    if k < 0:
        raise ValueError("Error, k must be a non-negative integer")
    
    if any(x < 0 for x in arr):
        raise ValueError("Error, all elements in the array must be non-negative integers")
    
    dp = [False]*(k+1)

    dp[0] = True

    for i in range(1, k+1, 1):
        for num in arr:
            if i-num>=0 and dp[i-num]:
                dp[i] = True
                break
    
    return dp[k]



if __name__ == "__main__":
    tests = [
        # Basic / trivial
        (([], 0), True),                    # no coins, only 0 achievable
        (([], 5), False),                   # no coins, can't make 5
        (([1], 0), True),                   # always make 0
        (([1], 7), True),                   # 1 used 7 times
        (([2], 7), False),                  # only even sums possible

        # Classic coin-change-style tests (unbounded)
        (([2, 3, 5], 7), True),             # 2 + 5 or 2 + 2 + 3 etc.
        (([2, 3, 5], 1), False),            # can't make 1
        (([4, 5], 7), False),               # impossible
        (([4, 5], 8), True),                # 4 + 4
        (([5, 7], 12), True),              # 12 = 5+7
        (([5, 7], 14), True),               # 7 + 7

        # contains coin '1' -> all targets reachable
        (([1, 3, 4], 100), True),

        # duplicates in coin list (shouldn't matter)
        (([2, 2, 3], 7), True),             # 2+2+3

        # zeros in coin list
        (([0], 0), True),                   # only 0 achievable
        (([0], 5), False),                  # can't make positive with only zero
        (([0, 3, 4], 6), True),             # 3+3 (zero ignored)
        (([0, 3, 4], 1), False),            # impossible

        # larger examples
        (([6, 9, 20], 43), False),          # classic postage-style example (43 not reachable)
        (([6, 9, 20], 44), True),           # 20+6+6+6+6

        # edge cases
        (([100], 300), True),               # 100*3
        (([7, 14], 1), False),              # gcd=7, 1 not reachable
    ]

    for (nums, target), expected in tests:
        result = can_it_be_summed(nums, target)
        ok = "✅" if result == expected else "❌"
        print(f"nums={nums}, target={target} → {result} (expected {expected}) {ok}")