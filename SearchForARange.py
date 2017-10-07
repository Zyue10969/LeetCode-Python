class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #思路：二分查找，找到nums[mid] = target的索引mid
        #然后，找mid的左边界left,右边界right
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                if nums[low] == target and nums[high] == target:
                    return [low, high]
                if nums[low] != target:
                    low += 1
                if nums[high] != target:
                    high -= 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return [-1, -1]
