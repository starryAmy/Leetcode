class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums) # no duplicate numbers
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set: # check if there are numbers if we keep adding
                    length += 1
                if length > longest:
                    longest = length
        return longest
