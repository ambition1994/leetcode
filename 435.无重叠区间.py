#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # 将所有子区间根据结束位置从小到大排序
        count = 0
        def takeSecond(elem):
            return elem[1]
        intervals.sort(key=takeSecond)
        temp = intervals[0]
        # 遍历所有已排序的子区间，如果区间重叠，计数，若无重叠，更新比较的子区间。
        for index, item in enumerate(intervals):
            if index == 0:
                continue
            elif (item[0] < temp[1]):
                count += 1
            else:
                temp = intervals[index]
        return count




# @lc code=end

solution = Solution()
print(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))