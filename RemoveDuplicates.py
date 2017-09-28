class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：采用俩指针，一个指针j指向原数组需要判断的元素，另一个指针i指向新数组新加入的元素
        # 由于是有序列表，每次判断指针j指向的元素是否与指针i指向的元素重复：
        # 如果没有重复，指针i前移一位，并讲指针j指向的元素赋值(即，添加当前元素进新数组，新数组长度 + 1)，然后j前移一位
        # 如果重复，j前移一位
        # 直到j遍历完nums数组为止，这时指针i指向新数组的最后一个元素
        # 所以，新数组的长度为i + 1
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
