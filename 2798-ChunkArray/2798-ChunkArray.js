// Last updated: 12/18/2025, 1:50:10 PM
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let res = [];
    let cur = [];
    for (let i = 0; i < arr.length; i++){
        cur.push(arr[i])
        if (cur.length === size || i === arr.length - 1){
            res.push(cur);
            cur = [];
        }
    }
    return res
};
