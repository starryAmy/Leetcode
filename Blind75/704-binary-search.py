class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (r + l) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
        return -1
