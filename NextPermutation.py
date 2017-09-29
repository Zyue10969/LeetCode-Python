class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 这道题是求当前排列在全排列中的下一个排列是什么
        # 首先要弄清楚全排列：
        # 在python中，这个很简单的实现:
        # from itertools import permutations
        # list(permutations([1, 2, 3, 4], 4))
       #[(1, 2, 3, 4),
       # (1, 2, 4, 3),
       # (1, 3, 2, 4),
       # (1, 3, 4, 2),
       # (1, 4, 2, 3),
       # (1, 4, 3, 2),
       # (2, 1, 3, 4),
       # (2, 1, 4, 3),
       # (2, 3, 1, 4),
       # (2, 3, 4, 1),
       # (2, 4, 1, 3),
       # (2, 4, 3, 1),
       # (3, 1, 2, 4),
       # (3, 1, 4, 2),
       # (3, 2, 1, 4),
       # (3, 2, 4, 1),
       # (3, 4, 1, 2),
       # (3, 4, 2, 1),
       # (4, 1, 2, 3),
       # (4, 1, 3, 2),
       # (4, 2, 1, 3),
       # (4, 2, 3, 1),
       # (4, 3, 1, 2),
       # (4, 3, 2, 1)]

        #　所以题目的意思是，从上面的某一行重排到期下一行，如果已经是最后一行了，则重排成第一行
        # 但是也不能根据给出的数组中的数字列出所有排列，因为要求不能占用额外的空间
        # ==================================分割线＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
        # 但是在全排列中有着一个规律：
        # 1.每一行中从后往前遍历，找到相邻两个元素是升序排列的，如：(1, 2, 4, 3)中的2和4, (2, 1, 4, 3)中的1和4
        # 2.当然，如果遍历完都找不到，如(4, 3, 2, 1),则说明整个序列是递减的，没有下一个排列
        # 3.第一步找到相邻两个升序的元素，为了叙述方便，我们讲前者成为【临界元素】，如：(1, 2, 4, 3)中的2, (2, 1, 4, 3)中的1
        # 4.保持临界元素的前缀元素不变，将临界元素与后缀元素中[大于临界元素的最小值]换位置(注意：后缀元素是降序排列的）
        # 如(1, 2, 4, 3)中2, 3互换--> (1, 3, 2, 4) ,  (2, 1, 4, 3)中1,　3互换--> (2, 3, 1, 4)
        # 5.最后,将后缀元素逆序排列
        if len(nums) <= 1:
            return
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        
        if partition == -1:
            nums.reverse()
            return 
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
            nums[partition + 1: len(nums)] = nums[partition + 1: len(nums)][::-1]
            return 
        

