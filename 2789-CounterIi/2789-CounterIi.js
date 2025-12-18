// Last updated: 12/18/2025, 1:50:11 PM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let cur = init;
    return {
        increment(){
            cur += 1;
            return cur;

        },
       decrement(){
            cur -= 1;
            return cur;
       },
       reset(){
            cur = init;
            return init;
       }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */