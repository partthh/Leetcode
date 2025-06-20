class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        current=prices[0]
        for i in prices:
            if i<current:
                current=i
                continue
            # if i>current:
            maxprofit=max(maxprofit,i-current)
        return maxprofit
            
        