// Last updated: 12/18/2025, 1:50:21 PM
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = new Map();
    let call = 0;
    return function(...args) {
        key = JSON.stringify(args);
        if (!cache.has(key)){
            res = fn(...args);
            cache.set(key, res);
            call += 1
            return res   
        }
        else{
                return cache.get(key);
        }

        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */