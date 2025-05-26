class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r] - prices[l])
                r += 1
            else:
                l += 1
        return res
