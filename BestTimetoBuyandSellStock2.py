class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心法：从前到后遍历prices，只要当天的价格高于前一天的价格，就算入收益
        
        sumProfit = 0
        for i in range(0, len(prices) - 1, 1):
            sumProfit += max(0, prices[i + 1] - prices[i])
        return sumProfit
        
        # 还有一个一行代码的：
        #　return sum([max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)])
