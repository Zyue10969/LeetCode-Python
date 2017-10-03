import heapq
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #结论:三个数的乘积的最大值 = max(min1 * min2 * max, max1 * max2 * max3)
        #思路一：排序后获得TopN值
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
    
        #思路二：用heapq堆数据结构获得TopN值
        min2 = heapq.nsmallest(2, nums)
        max3 = heapq.nlargest(3, nums)
        return max(min2[0] * min2[1] * max3[2], max3[0] * max3[1] * max3[2])
