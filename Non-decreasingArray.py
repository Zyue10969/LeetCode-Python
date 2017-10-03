from copy import *
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #思路：首先找到排序错误的索引
        # 然后，有两种可能：要么把前一个数变小(赋值为后一个数)
        # 要么把后一个数变大(赋值位前一个数)
        # 因为只能操作一次，所以break跳出循环
        #最后判断，修改之后的列表与排序后的列表是否相等
        copy1, copy2 = deepcopy(nums), deepcopy(nums)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                copy1[i] = copy1[i + 1]
                copy2[i + 1] = copy2[i]
                break
        return copy1 == sorted(copy1) or copy2 == sorted(copy2)
