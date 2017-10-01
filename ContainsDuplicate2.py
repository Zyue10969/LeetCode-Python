import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # two pass + dict :
        
        # flag = False
        # nums_dict = collections.defaultdict(list)
        # for index, num in enumerate(nums):
        #     nums_dict[num].append(index)
        # for indices in nums_dict.itervalues():
        #     if len(indices) > 1:
        #         for i in range(len(indices) - 1):
        #             if indices[i + 1] - indices[i] <= k:
        #                 flag = True
        # return flag
                    
        # one pass + dict :
        
        nums_dict = dict()
        for index, num in enumerate(nums):
            if num in nums_dict and index - nums_dict[num] <= k:  #　注意　index - nums_dict[num] 是用当前元素索引减去前一个重复元素索引
                return True
            nums_dict[num] = index   #　将当前元素索引加入nums_dict中
        return False
