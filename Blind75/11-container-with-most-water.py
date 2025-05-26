class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_res = 0
        while l < r:
            container = (r - l) * min(height[l], height[r])
            max_res = max(max_res, container)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_res
