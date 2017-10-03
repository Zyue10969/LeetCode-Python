class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #结论:三个数的乘积的最大值 = max(min1 * min2 * max, max1 * max2 * max3)
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
