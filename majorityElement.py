class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路１：two pass + dict　99ms
        # count_dict = dict()
        # for num in nums:
        #     if count_dict.has_key(num):
        #         count_dict[num] += 1
        #     else:
        #         count_dict[num] = 1
        # for num, count in count_dict.items():
        #     if count > len(nums) / 2:
        #         return num
            
        # 思路２：one pass + dict 88 ms
        count_dict = dict()
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            if count_dict[num] > len(nums) / 2:
                return num
            if num in count_dict:
                count_dict[num] += 1
