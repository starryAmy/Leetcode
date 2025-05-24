class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # every word has their own hash table
        # turn table into a tuple ans store them
        # return
        res = {}
        for str in strs:
            word = [0] * 26
            for s in str:
                word[(ord(s) - ord("a"))] += 1
            if tuple(word) not in res:
                res[tuple(word)] = []
            res[tuple(word)].append(str)
        return res.values()
