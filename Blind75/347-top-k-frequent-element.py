class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: 計數每個數字出現次數
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1   # O(n)

        # Step 2: 用桶排序方式，把相同頻率的數字放進同一 bucket
        freq = [[] for _ in range(len(nums) + 1)]  # O(n)
        for n, c in count.items():                 # O(n)
            freq[c].append(n)

        # Step 3: 從高頻往低頻掃描，直到找到 k 個元素
        res = []
        for i in range(len(freq) - 1, 0, -1):      # O(n)
            for num in freq[i]:                    # 最多總共 O(n)
                res.append(num)
                if len(res) == k:
                    return res
