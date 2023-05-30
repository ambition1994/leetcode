class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * max((n + 1), 3)
        dp[0], dp[1], dp[2] = 1, 1, 2
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
