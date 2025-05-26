class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        # becuase this is sorted
        left = 0
        right = len(numbers) - 1
        while left < right:
            totalSum = numbers[left] + numbers[right]
            if totalSum > target:
                right -= 1
            elif totalSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
