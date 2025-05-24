class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {} # 1. set a new empty dictionary
        for i in nums: # 2. run through the array
            if i in table: # 3. if the number is already in the dictionary, return True
                return True
            else:
                table[i] = 1 # 4. else, add the number to the dictionary
        return False
