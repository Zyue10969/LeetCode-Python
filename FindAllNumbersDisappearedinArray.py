class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 取负法 : 将元素对应位置的元素取负
        # nums[nums[i] -1] = -nums[nums[i]-1]
        # 在位置k放了元素i，则在取负的过程中i的取值有两种可能：
        # i为正，表示当前尚未遇到元素k将该位置取负；
        # i为负，表示当前已经有元素k出现，保持负值不变
        # =======================================================
        # 但是我们不关心k，我们关心元素i
        # 元素i既然出现，我们就看一下对应位置i：为正，表示这是元素i第一次出现，我们将位置i取负；
        # 为负，表示元素i已经出现过一次，我们不做任何操作
        # 不管一个元素出现一次还是两次，只要出现它对应的位置就会被取负。
        # 当某个元素不出现的时候，该元素对应的位置始终访问不到，所以还是正值，
        # 通过这种方法我们就可以找到哪些元素没有出现。
        # 在取负的过程中，如果发现要取负的位置已经为负，
        # 说明这个元素已经出现过，也即该元素出现了两次，我们可以将该元素保留下来
        #  index= [0, 1, 2, 3, 4, 5, 6, 7]
        #  nums = [4, 3, 2, 7, 8, 2, 3, 1] 
        #negnums=[-4,-3, -2,-7,8, 2,-3,-1]
        
        # for i in xrange(len(nums)):
        #     index = abs(nums[i]) - 1
        #     nums[index] = - abs(nums[index])
        # return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]
    
        # 标志法
        flags = [-1 for i in range(len(nums))]
        for i in range(len(nums)):
            flags[nums[i] - 1] = nums[i]
        return [i + 1 for i in range(len(flags)) if flags[i] < 0]
