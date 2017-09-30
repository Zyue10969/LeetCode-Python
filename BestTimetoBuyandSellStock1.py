class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划问题
        #　对于prices中的每个元素，维护两个变量：当前价格最低值(minPrice)和全局利润最高值(max_profit)
        # 从前到后遍历prices,　记录当前元素为止的最低价格(minPrice)，并作为购入价格
        # 并计算当前元素作为售出价格的收益: prices[i] - minPrice
        if len(prices) < 1:
            return 0
        
        minPrice = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            max_profit = max(max_profit, prices[i] - minPrice)
        return max_profit
            
