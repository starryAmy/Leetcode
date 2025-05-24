class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # set up two hash tables and run through each alpha
        # store them in tables and record times of alpha
        first_hash = {}
        second_hash = {}
        for i in s:
            if i in first_hash:
                first_hash[i] += 1
            else:
                first_hash[i] = 1
        for j in t:
            if j in second_hash:
                second_hash[j] += 1
            else:
                second_hash[j] = 1
        if first_hash == second_hash:
            return True
        else:
            return False
