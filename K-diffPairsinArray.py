from collections import *
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #　思路一: 利用dict生成 {元素: 索引}字典
        # ret = set()
        # nums_dict = defaultdict(list)
        # for index, num in enumerate(nums):
        #     nums_dict[num].append(index)
        # if k == 0:
        #     for key in nums_dict.keys():
        #         if len(nums_dict[key]) > 1:
        #             ret.add(key)
        # elif k > 0:
        #     for key in nums_dict.keys():
        #         if nums_dict[key] and nums_dict[k + key]:
        #             ret.add(key)
        # return len(ret)
        
        # 思路二 : 利用集合的交集和collections.Counter()
        if k > 0:
            return len(set(nums) & set(i + k for i in nums))
        elif k == 0:
            return len([v for v in Counter(nums).values() if v > 1])
        else:
            return 0
