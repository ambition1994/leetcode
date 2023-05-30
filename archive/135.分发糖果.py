#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings):
    # def candy(self, ratings: List[int]) -> int:
        num_candy = [1] * len(ratings)
        for index1, i in enumerate(ratings):
            if (i > ratings[index1-1] and index1 > 0):
                    num_candy[index1] = num_candy[index1-1] + 1
        ratings.reverse()
        num_candy.reverse()
        for index2, j in enumerate(ratings):
            if (index2 > 0):
                if (num_candy[index2] <= num_candy[index2-1] and j > ratings[index2-1]) :
                    num_candy[index2] = (num_candy[index2-1] + 1)

        count = sum(num_candy)
        return count
# @lc code=end
solution = Solution()
b = solution.candy([1,2,87,87,87,2,1])
print(b)