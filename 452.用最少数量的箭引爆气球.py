#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points):
        count = 0
        def takeSecond(elem):
            return elem[1]
        points.sort(key=takeSecond)
        temp = points[0]
        # 遍历所有已排序的子区间，如果区间重叠，计数，若无重叠，更新比较的子区间。
        for index, item in enumerate(points):
            if index == 0:
                continue
            elif (item[0] <= temp[1]):
                count += 1
            else:
                temp = points[index]
        return len(points)-count
# @lc code=end

