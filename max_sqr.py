def max_sqr(matrix: list[list[str]]) -> int:
    # Line 1: Get dimensions
    m, n = len(matrix), len(matrix[0])
    # Rows and cols (e.g., 4, 5)

    # Line 2: Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Extra row/col for base cases (e.g., 5×6 zeros)
    max_side = 0
    # Track largest square side (e.g., 0)

    # Line 3: Fill DP table
    for i in range(m):
        # Iterate rows (e.g., 0 to 3)
        for j in range(n):
            # Iterate cols (e.g., 0 to 4)
            if matrix[i][j] == '1':
                # Current cell is 1 (e.g., matrix[2][3])
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                # Min of neighbors + 1 (e.g., min(1,1,1)+1=2)
                max_side = max(max_side, dp[i + 1][j + 1])
                # Update max (e.g., max(1,2)=2)

    # Line 4: Return area
    return max_side * max_side
    # Area of largest square (e.g., 2*2=4)

matrix1 = [["1","0","1","0","0"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"],
           ["1","0","0","1","0"]]
max_sqr(matrix1)

matrix2 = [["0","1"],
           ["1","0"]]
max_sqr(matrix2)

matrix3 = [["1","0","1","0","0"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"],
           ["1","1","1","1","1"],
           ["1","0","1","1","1"]]
max_sqr(matrix3)

matrix4 = [["1","0","1","0","0"],
           ["1","1","1","1","1"],
           ["0","1","1","1","1"],
           ["1","1","1","1","1"],
           ["1","1","1","1","1"]]
max_sqr(matrix4)