// Last updated: 12/18/2025, 1:50:17 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let res = [];
     for (let i = 0; i < arr.length; i++){
        if (fn(arr[i], i)){
            res.push(arr[i]);
        }
     }
    return res
};