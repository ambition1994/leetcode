#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        int start = 0
        int end = nums[0]
        int step =0
        for i in (len(nums)-1):
            max_value = max(i+nums[i])



# @lc code=end

# 从第一个位置遍历跳跃一次后的位置，若可以跳到最后一步，停止下一步
#  更新初始位置，重复步骤一