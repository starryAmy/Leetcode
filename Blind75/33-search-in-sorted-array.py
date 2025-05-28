class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # if this num is smaller than nums[l] and nums[m]: search right
        # if this num is >= nums[l] but <= nums[m]: search left
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                res = m
            if nums[m] >= nums[l]: # if nums[m] in the left group
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # if nums[m] in the right group
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return res
