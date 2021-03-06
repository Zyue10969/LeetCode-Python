# -*- coding:utf-8 -*-
def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 思路：１．排序
        # 2. 类似与夹逼定理, 从两端开始遍历
        nums.sort()
        closet_sum = nums[0] + nums[1] + nums[2]
        for i in xrange(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                if abs(target - sum) < abs(target - closet_sum):
                    closet_sum = sum
                if sum < target:  # 增加sum的值
                    j += 1
                if sum > target:  # 降低sum的值
                    k -= 1
        return closet_sum
