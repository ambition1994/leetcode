#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        previous = [0] * len(flowerbed)
        flowerbed_copy = (len(flowerbed)+2) * [0]
        flowerbed_copy[1:-1] = flowerbed[:]
        for index in  range(len(flowerbed_copy)-2):
            if flowerbed_copy[index] == flowerbed_copy[index+1] == flowerbed_copy[index+2] == 0:
                if previous[index-1]:
                    continue
                else:
                    count += 1
                    previous[index] = 1
        return (count >= n)
        # return count, flowerbed_copy
# @lc code=end
solution = Solution()
solution.canPlaceFlowers([1,0,0,0,0,0,1], 2)
