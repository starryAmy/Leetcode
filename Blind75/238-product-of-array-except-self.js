var productExceptSelf = function(nums) {
  // We initialize result with 1s because we will be multiplying values into this array later.
  result = new Array(nums.length).fill(1);

  // count number from left side first
  let prefix = 1;
  for ( i = 0; i < nums.length; i++ ){
    // will count the product from beginning to the one before target
    result[i] = prefix;
    prefix *= nums[i];
  };

  // Compute suffix products and multiply with prefix products
  let suffix = 1;
  for ( i = nums.length - 1; i >= 0; i-- ){
    result[i] *= suffix;
    suffix *= nums[i];
  };
  return result;
}
