#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals):
        count = 0
        def takeSecond(elem):
            return elem[1]
        intervals.sort(key=takeSecond)
        temp = intervals[0]
        intervalsz_copy = intervals[:]
        for index, item in enumerate(intervalsz_copy):
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