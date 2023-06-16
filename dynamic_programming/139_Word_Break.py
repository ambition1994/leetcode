class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # dp[i] represent s[:i] wheather to fit the condition
        # dp[len(s)] ---> s[:len(s)]
        # ---> len(dp) = len(s) + 1
        # dp[1] ---> s[:1] == s[0] ---> length equal to 1
        for i in range(0, len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                # s[:i] ---> dp[i]
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = True
        return dp[-1]
