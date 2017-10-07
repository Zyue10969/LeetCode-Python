class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #思路:回溯(深度优先搜索,DFS)。先对数组进行排序，然后从小到大递归累加，>= target时回溯
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    def dfs(self, nums, target, index, curPath, res):
        if target < 0: #终止条件：target<0或者target<nums[0]
            return
        if target == 0:
            res.append(curPath)
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, curPath + [nums[i]], res)
