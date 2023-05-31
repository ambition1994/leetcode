# use dynamic programming way to solve this problem
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        return dp[-1]
