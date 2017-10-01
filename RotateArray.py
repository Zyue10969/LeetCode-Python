class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 思路：分片1
        # nums = [1, 2, 3, 4, 5, 6, 7]
        # index=  0, 1, 2, 3, 4, 5, 6
        # 到索引3为止的分片(包括索引3) = nums[: 4] = nums[: 7 - 3] = nums[: len(nums) - k] 
        # 索引3之后的分片(不包括索引3) = nums[4 :] = nums[: 7 - 3] = nums[len(nums) - k :]
        # nums[:] = nums[n - k:] + nums[:n - k]
        
        # 分片２
        #　nums = [1, 2, 3, 4, 5, 6, 7]
        # index=  0, 1, 2, 3, 4, 5, 6
        # index = -7,-6,-5,-4,-3,-2,-1
        # 到索引3为止的分片(包括索引3) = nums[:-3] = nums[: -k]
        # 索引3之后的分片(不包括索引3) = nums[-3:] = nums[-k: ]
        nums[:] = nums[-k: ] + nums[: -k]
        #　注意：1.分片特点：第一个索引的元素包含在分片内，第二个索引的元素不包含在分片内（左闭右开）
        #        2.必须写成nums[:]而不是直接nums,是因为前者是在原数组上进行改变，而后者是抽取原数组里面的元素然后赋值给一个新数组nums
