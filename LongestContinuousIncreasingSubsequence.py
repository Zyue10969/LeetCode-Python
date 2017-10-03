class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #动态规划法
        #从头到尾遍历数组nums，为每个元素维护两个变量：
        #一个局部变量localLen,一个全局变量globalLen
        #如果nums[i] < nums[i+1]，localLen += 1
        #否则，localLen = 1从当前元素从新开始计数
        if len(nums) < 1:
            return 0
        localLen = globalLen = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                localLen += 1
            else:
                localLen = 1
            globalLen = max(globalLen, localLen)
        return globalLen
