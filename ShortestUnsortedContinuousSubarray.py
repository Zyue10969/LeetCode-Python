class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路:　原数组与排序后的数组相减，然后找两端不为0的元素的位置
        # 原数组:[2, 6, 4, 8, 10, 9, 15]
        # 排序后:[2, 3, 4, 8, 9, 10, 15]
        # 相减后:[0, 3, 0, 0, 1, -1, 0]
        # 结果:   5 - 1 + 1 = 5 
        margin = [i - j for i, j in zip(nums, sorted(nums))]
        low = 0
        high = len(nums) - 1
        while low < high:
            if margin[low] == 0:
                low += 1
                continue
            if margin[high] == 0:
                high -= 1
                continue
            return high - low + 1
        return 0    
