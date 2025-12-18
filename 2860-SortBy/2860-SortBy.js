// Last updated: 12/18/2025, 1:50:04 PM
/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    // let sortedArr = fn(arr);
    return arr.sort((a,b) => fn(a) - fn(b))
};