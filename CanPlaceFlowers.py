class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #贪心法：找到连续仨个0的位置，在中间插个１
        #在原数组两边各添加0，统一一下边界问题
        #flowerbed = [1, 0, 0, 0, 1]
        #首尾添加0:[0,1, 0, 0, 0, 1, 0]
        #只有一个连续3个0的情况
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        return n <= count
