/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  let maxSum = nums[0];
  let currentSum = 0;
  for (i = 0; i < nums.length; i++) {
    currentSum += nums[i];
    if (currentSum > maxSum) {
      maxSum = currentSum;
    } {
      // if currentSum < 0, then we reset it to 0 which means we ignore previous numbers and start fresh
      if (currentSum < 0){
        currentSum = 0;
      }
    }
  };
  return maxSum;
};
