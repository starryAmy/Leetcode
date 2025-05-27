class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[r] > nums[l]: # if the right bound is higher
                res = min(res, nums[l])
                break
            else:
                m = (l + r) // 2 # count the middle num
                res = min(res, nums[m])
                if nums[m] >= nums[l]: # if the middle is higher than the left bound
                    l = m + 1 # move the left pointer
                else:
                    r = m - 1
        return res
