# -*- coding:utf-8 -*-
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 1.排序
    # 2.从0开始遍历第一个数nums[i] ０<= i <= len(nums) - 2
    # 3.从i + 1开始遍历第二个数nums[j],　从 len(nums) - 1开始遍历第三个数nums[k],　找到 nums[i] + nums[j] + nums[k] == 0的值
    # 4.注意消除重复
    triplets = set()  # 防止重复
    nums.sort()  # 排序
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
    return list(map(list, triplets))
