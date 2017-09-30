class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划: 全局最优和局部最优
        # 基本思路：对数组nums中的每个元素num[i]维护两个变量：一个全局最优globalMax，一个局部最优localMax
        # globalMax：当前元素为止的最优解
        # localMax: 必须包含当前元素的最优解
        # 假设对于nums[i],已知上一步的全局最优(globalMax)和局部最优(localMax)
        # 则有 locabMax = max(nums[i], localMax + nums[i])
        #     globalMax = max(globalMax, localMax)
        # 注意：这里的localMax必包含nums[i],而globalMax要么是当前元素局部最优（包含当前元素），要么是原来的全局最优(不包含当前元素)
        localMax  = globalMax = nums[0]
        for num in nums[1:]:
            localMax  = max(num, num + localMax)
            globalMax  = max(localMax, globalMax)
        return globalMax
        
        
