// Last updated: 12/18/2025, 1:50:09 PM
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let run = false;
    return function(...args){
        if (!run){
            run = true;
            return fn(...args);
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
