class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            diff = target - nums[i] # check if diff is in hash table
            if diff in hash_table:
                return [i, hash_table[diff]] # if so, return indices
            else:
                hash_table[nums[i]] = i
