// Last updated: 12/18/2025, 1:50:18 PM
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        let res = x
        for (let i = functions.length - 1; i > -1; i--) {
            res = functions[i](res);
            console.log(res)
        }
        return res
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */