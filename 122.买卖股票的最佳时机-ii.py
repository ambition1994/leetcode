#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for index, price in enumerate(prices[:-1]):
            if price < prices[index+1]:
                profit += prices[index+1] - price
        return profit
# @lc code=end


# 遍历数组，如果后面一个数比前面大，就求差值，并累计求和
