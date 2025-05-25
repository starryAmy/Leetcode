class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        suffix = []
        res = []
        pre_product = 1
        suff_product = 1
        for i in range(len(nums)):
            if i == 0:
                prefix.append(pre_product)
                suffix.append(suff_product)
            else:
                pre_product *= nums[i - 1]
                suff_product *= nums[i * -1]
                prefix.append(pre_product)
                suffix.append(suff_product)
        reversed_suffix = suffix[::-1]
        for i in range(len(prefix)):
            res.append(prefix[i] * reversed_suffix[i])
        return res
