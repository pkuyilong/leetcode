import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        res, min_num, max_num = 0, sys.maxsize, 0 
        for i in range(len(prices)):
            min_num =  min(min_num, prices[i])
            res = max(res, prices[i] - min_num)
        print(res)
        return res
