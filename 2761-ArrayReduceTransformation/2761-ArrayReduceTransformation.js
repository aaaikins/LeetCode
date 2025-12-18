// Last updated: 12/18/2025, 1:50:14 PM
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let val = init;
    if (nums.length === 0){
        return val;
    }
    for (num of nums){
        val = fn(val, num);
    }
    
    return val;
};