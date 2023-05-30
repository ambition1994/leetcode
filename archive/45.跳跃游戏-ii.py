#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# class Solution:
#     def jump(self, nums: List[int]) -> int:
class Solution:
    def jump(self, nums):
        if  len(nums) == 1:
            step_counts = 0
        else:
            end_index = len(nums) - 1
            far_index = nums[0]
            far_index_pre = 0
            step_counts = 1
            while (far_index < end_index):
                temp = []
                tempindex = []
                for index, item in enumerate(nums[far_index_pre+1:far_index+1]):
                    tempindex.append(index+item)
                a = far_index_pre
                far_idnex_pre = far_index
                far_index = max(tempindex)+ a + 1
                step_counts += 1
        return step_counts 
# @lc code=end

solution = Solution()
print(solution.jump([2,3,1,1,4]))