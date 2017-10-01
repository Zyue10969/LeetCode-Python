class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #　思路：丢失的那个数值　= (0 + 1 + ... + n) - sum(nums)
        # 其中(0 + 1 + ... + n) = n * (n + 1) / 2
        # 且有题意可知 n = len(nums) 数组最后一位n与数组长度相等
        n  = len(nums)
        return n*(n + 1) / 2 - sum(nums)
