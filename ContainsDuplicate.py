class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        m = len(set(nums))
        if n - m == 0:
            return False
        else:
            return True
#  还有一种一行套路：
#       return len(nums) != len(set(nums))
