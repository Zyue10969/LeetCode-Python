class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 思路１：
#         nums_dict = dict()
#         for id, num in enumerate(numbers):
#             nums_dict[num] = id
        
#         for id1, num in enumerate(numbers):
#             id2  = nums_dict.get(target - num)
#             if id2 is not None and id2 > id1:
#                 return [id1 + 1, id2 + 1]
        # 思路２：
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            if sum > target:
                high -= 1
            else:
                low += 1
        
