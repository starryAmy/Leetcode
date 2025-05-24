/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// create a hash table
var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        if(map.has(diff)){
            return [map.get(diff), i]
        }
        map.set(nums[i], i)
    }
}
