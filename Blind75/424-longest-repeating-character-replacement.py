class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # control sliding window

        l, r = 0, 0
        longest = 0
        char = {}
        while r < len(s):
            char[s[r]] = char.get(s[r], 0) + 1
            while r - l + 1 - max(char.values()) > k: # narrow the window
                char[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1 # extends the window
        return longest
