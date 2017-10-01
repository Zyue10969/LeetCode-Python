class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 思路１：类似与快速排序
        # 维护两个指针，指针zero记录nums中第一个0元素的位置
        # 指针i记录nums中指针zero之后第一个非0元素的位置
        # 通过交换nums[i]和nums[zero]，将0元素后移
        # i  = zero = 0
        # while i < len(nums):
        #     if nums[i] != 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero += 1
        #     i += 1
            
        # 思路2:从后往前遍历
        # 如果当前元素=0，则删除当前元素，并在数组尾部添加0
        # 这样保证第i个元素的前i - 1个元素的位置不变，不影响接下来的遍历
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
