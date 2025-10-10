def max_sub_squares(mat):
    if not mat:
        return 0
    
    if (len(mat) == 1) and not mat[0]:
        return 0
    
    n, m = len(mat), len(mat[0])

    dp = [([0]*m) for _ in range(n)] # max length with bottom right corner i,j

    for i in range(m):
        dp[0][i] = mat[0][i]
    for j in range(n):
        dp[j][0] = mat[j][0]

    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 0

    best = 0

    for i in range(n):
        for j in range(m):
            best = max(best, dp[i][j])
    return best 

if __name__ == "__main__":
    # list of (matrix, expected_side)
    TESTS = [
        # empty matrix
        ([], 0),

        # empty-row matrix
        ([[]], 0),

        # single cell 0
        ([[0]], 0),

        # single cell 1
        ([[1]], 1),

        # all zeros
        (
            [
                [0,0,0],
                [0,0,0]
            ],
            0
        ),

        # all ones (2x3) -> max side is min(rows,cols) = 2
        (
            [
                [1,1,1],
                [1,1,1]
            ],
            2
        ),

        # the example we've used several times (3x3) -> best = 2
        (
            [
                [1,1,0],
                [1,1,1],
                [0,1,1]
            ],
            2
        ),

        # rectangular case (3x4) with 2x2 largest
        (
            [
                [1,0,1,1],
                [1,1,1,1],
                [0,1,1,1]
            ],
            2
        ),

        # single row
        (
            [[1,1,1,1]],
            1
        ),

        # single column
        (
            [[1],[1],[1],[1]],
            1
        ),

        # larger mixed case: there's a 3x3 of ones in bottom-right
        (
            [
                [0,1,1,0,0],
                [1,1,1,1,0],
                [1,1,1,1,1],
                [0,1,1,1,1]
            ],
            3
        ),
    ]

    # run tests
    from copy import deepcopy
    for idx, (matrix, expected) in enumerate(TESTS, 1):
        # run non-mutating versions
        res1 = max_sub_squares(deepcopy(matrix))

        ok = (res1 == expected)
        status = "PASS" if ok else "FAIL"
        print(f"Test {idx:02d}: expected={expected} -> standard={res1}  [{status}]")
        if not ok:
            print("  input:")
            for row in matrix:
                print("   ", row)
            # Stop on first failure for easier debugging
            raise AssertionError(f"Test {idx} failed: got {res1} expected {expected}")

    print("\nAll tests passed!")