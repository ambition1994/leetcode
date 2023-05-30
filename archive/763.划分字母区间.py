#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s):
        '''
        核心思想是先将每个字母的最远出现位置(在输入字符串中的下标或索引)存在一个字典中，
        这里我用的是far_index存储最远位置，然后再遍历一次输入字符串，如果当前索引值和
        对应值的最远位置相同，在此处分割，计算片段长度，这里一个重要的点在于使用一个缓存
        值存储上一个分割点的下标或者位置，我这里使用的是temp这个变量存储，但是要+1，这是
        因为下一个片段是分割点的下一个位置，当然你也可以通过修改计算方式来处理。另一点，我
        同时也用temp做存储片段长度的变量。
        '''
        end = 0  # 计算分割点，不断与遍历值的最远点比较取最大，返回end
        temp = 0  # 存储分割点位置，以及片段长度
        result = []  # 存储返回结果，是每一个片段长度组成的列表
        far_index = {}  # 存储最远位置

        #**************第一轮遍历，构建每个字母对应于输入列表最远位置的字典********************************************#
        for index, value in enumerate(s):
            far_index[value] = index

        #**************第二轮遍历，通过if语句判断是否到达了分割点，并将分割的片段长度暂存并append到result列表中***********#
        for index1, value1 in enumerate(s):
            end = max(end, far_index[value1])
            if (index1 == end):
                temp = end - temp + 1
                result.append(temp)
                temp = end + 1
        return result
# @lc code=end
# solution = Solution()
# solution.partitionLabels("ababcbacadefegdehijhklij")

