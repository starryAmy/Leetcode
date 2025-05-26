class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first, sort the array
        # so we can use two pointers
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0: # if it's positive, sum = 0 never gonna happen
                break
            if nums[i] == nums[i - 1] and i > 0: # duplicate, so skip
                continue
            l = i + 1
            r = len(nums) - 1
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
                while nums[l - 1] == nums[l] and l < r: # check if second element is duplicate
                    l += 1
        return res
