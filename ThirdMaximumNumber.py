class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路1:　去重复，然后升序排序
        # nums = sorted(list(set(nums)))
        # if len(nums) >= 3:
        #     return nums[-3]
        # else:
        #     return nums[-1]
        
        # 思路2: 去重复，然后去掉前两个最大值
        nums = set(nums)
        if len(nums) >= 3:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        else:
            return max(nums)
