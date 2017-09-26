# -*- coding:utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 建立反索引字典: dict[num] = index
        num_dict = {}
        for index, num in enumerate(nums):
            num_dict[num] = index
        
        for index1, num in enumerate(nums):
            index2 = num_dict.get(target - num) # dict.get() 访问一个不存在的键时，没有任何异常，得到None值
            if index2 is not None and index1 != index2:
                return [index1, index2]
