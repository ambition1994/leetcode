# use dynamic programming way to solve this problem
# 1. init dp list is important, cause 1 was the smallest number for square number,
#    so dp[i] at most equal to i
# 2. the transition formula in the inner loop of two loops,
#    dp[i] equal to dp[i-k] plus 1, which k was a square number less than i
# But due to two for loop, time complexity is high, which is O(n*sqrt(n))


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        return dp[-1]
