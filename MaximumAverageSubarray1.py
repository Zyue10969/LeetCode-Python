class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #思路：先求元素的前缀和，然后利用滑窗求最大平均值
        #index= [0, 1, 2, 3, 4,5]
        #nums = [1,12,-5,-6,50,3]
        #sums = [1,13, 8, 2,52,55]
        #所有连续四元组的和为：2, (52 - 13), (55 - 8)
        #平均值为：0.5, (52 - 13)/4.0, (55 - 8)/4.0
        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(num + sums[-1])
        
        res = sums[k-1]
        for i in range(k, len(sums)):
            res = max(res, sums[i] - sums[i - k])
        return res / float(k)
