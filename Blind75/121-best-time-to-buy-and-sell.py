class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # sliding window
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r # we found prices[r] is lower, so use prices[r] instead
            r += 1 # no matter what, right pointer always needs to move one step further
        return res
