class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
#         if len(height) < 2:
#             exit("Error: length of height is at least 2.")
#         for i in range(len(height)):
#             ai = height[i]
#             for j in range(i + 1, len(height)):
#                 aj = height[j]
#                 max_water = max(max_water, (j - i) * min(ai, aj))
#         return max_water
        #　前面思路错了，时间复杂度太大
        # 换个思路类似于夹逼定理
        low = 0
        high = len(height) - 1
        while low < high:
            if height[low] <= height[high]:
                max_water = max(max_water, (high - low) * height[low])
                low += 1
            else:
                max_water = max(max_water, (high - low) * height[high])
                high -= 1
        return max_water
                
