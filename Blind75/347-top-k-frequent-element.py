class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} # count every alpha
        freq = [[] for i in range(len(nums) + 1)] # sort according to freq
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1 # if num is not in count, count[num] = 0
        # get every pair of count and sort them according to freq
        for n, c in count.items():
            freq[c].append(n)
        # traverse freq from high to low
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
