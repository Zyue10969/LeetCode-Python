class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划题
        localMax = globalMax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                localMax += 1
                globalMax = max(globalMax, localMax)
            else:
                localMax = 0
        return globalMax
