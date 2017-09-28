class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 思路：采用俩指针，一个指针j指向当前数组元素，另一个指针i指向添加入新数组的新元素
        #　如果指针j指向当前数组元素　== val：指针j后移一位　
        # 如果指针j指向当前数组元素　！= val:　讲当前值赋值于指针i，然后指针i, j后移一位
        # 直到指针j遍历完nums数组，这时，指针i指向新数组最后一位的下一位的空元素
        # 所以，新数组长度== i
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 
