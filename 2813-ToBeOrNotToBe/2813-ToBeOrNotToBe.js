// Last updated: 12/18/2025, 1:50:07 PM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe(par) {
            if (val === par){
                return true;
            }
            throw Error("Not Equal");
        },
        notToBe(par){
            if (val !== par){
                return true;
            }
            throw Error("Equal");
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */