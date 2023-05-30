class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[]] * max(3, numRows)
        dp[0], dp[1], dp[2] = [1], [1, 1], [1, 2, 1]
        if numRows <= 3:
            return dp[:numRows]
        for i in range(3, numRows):
            tmp = [(i + j) for i, j in zip(dp[i - 1][:-1], dp[i - 1][1:])]
            dp[i] = [dp[i - 1][0]] + tmp + [dp[i - 1][-1]]
        return dp[:numRows]
