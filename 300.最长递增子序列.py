#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for item in nums:
            if not d or item > d[-1]:
                d.append(item)
            else:
                left, right = 0, len(d) - 1
                location = right
                while left <= right:
                    mid = (left + right) // 2
                    if d[mid] >= item:
                        location = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                d[location] = item
        return len(d) 
# @lc code=end

