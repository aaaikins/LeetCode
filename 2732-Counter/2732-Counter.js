// Last updated: 12/18/2025, 1:50:20 PM
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = 0;
    return function() {
        let num = n + count;
        count ++;
        return num;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */