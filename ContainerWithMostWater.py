class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        if len(height) < 2:
            exit("Error: length of height is at least 2.")
        for i in range(len(height)):
            ai = height[i]
            for j in range(i + 1, len(height)):
                aj = height[j]
                max_water = max(max_water, (j - i) * min(ai, aj))
        return max_water
        
                
