#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=False)
        s.sort(reverse=False)
        count = 0
        for i in g:
            for j in s:
                if j >= i:
                    count += 1
                    s.remove(j)
                    break
                else: 
                    continue
        return count
# @lc code=end


