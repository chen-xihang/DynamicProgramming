def number_of_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = dp[i] + dp[i - 2]
        if i >= 3:
            dp[i] = dp[i] + dp[i - 3]
    return dp[n]

if __name__ == "__main__":
    tests = [
        (0, 1),   # 1 way: do nothing
        (1, 1),   # (1)
        (2, 2),   # (1+1), (2)
        (3, 4),   # (1+1+1), (1+2), (2+1), (3)
        (4, 7),   # sum of previous three: 4+2+1
        (5, 13),  # 7+4+2
        (6, 24),  # 13+7+4
        (7, 44),  # 24+13+7
        (8, 81),  # 44+24+13
        (9, 149), # 81+44+24
        (10, 274) # 149+81+44
    ]

    for n, expected in tests:
        result = number_of_stairs(n)
        print(f"n={n} → {result} (expected {expected}) {'✅' if result == expected else '❌'}")
