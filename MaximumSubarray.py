class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划: 全局最优和局部最优
        localMax  = globalMax = nums[0]
        for num in nums[1:]:
            localMax  = max(num, num + localMax)
            globalMax  = max(localMax, globalMax)
        return globalMax
        
        
