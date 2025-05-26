class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        char = set()
        l, r = 0, 0
        max_length = 0
        while r < len(s):
            while s[r] in char: # keep looping until there is no duplicate
                char.remove(s[l])
                l += 1
            max_length = max(max_length, r - l + 1)
            char.add(s[r])
            r += 1
        return max_length
