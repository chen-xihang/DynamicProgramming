# suppose you can roll a six-sided die n times your earning is the last roll, what is the expected earning?
import math
def dice_game(n):
    if n == 0:
        return 0
    if n == 1:
        return 3.5
    dp = [0] * (n + 1)
    dp[1] = (1/2)*(1+6)
    for i in range(2, n + 1):
        k = (6-(math.floor(dp[i-1])))/6
        dp[i] = (math.ceil(dp[i-1])+6)*k*(1/2)+(1-k)*dp[i-1]
    return dp[n]

dice_game(0)
dice_game(1)
dice_game(2)